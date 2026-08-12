"""
pr_export.py
One-time PR export to CSV.
Fetches all PRs created within a date range and writes a CSV with
number, title, author, created date, merged date, and business days to merge.
"""

import csv
import os
import requests
from datetime import datetime, timedelta, timezone


def business_days_between(start: datetime, end: datetime) -> int:
    """Count business days (Mon–Fri) between two datetimes."""
    count = 0
    current = start.replace(hour=0, minute=0, second=0, microsecond=0)
    end_day = end.replace(hour=0, minute=0, second=0, microsecond=0)
    while current < end_day:
        if current.weekday() < 5:
            count += 1
        current += timedelta(days=1)
    return count


def fetch_prs(repo: str, token: str, since: datetime, until: datetime) -> list:
    """Return all PRs (any state) created within [since, until]."""
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    prs = []
    page = 1

    while True:
        resp = requests.get(
            f"https://api.github.com/repos/{repo}/pulls",
            headers=headers,
            params={
                "state": "all",
                "sort": "created",
                "direction": "desc",
                "per_page": 100,
                "page": page,
            },
        )
        resp.raise_for_status()
        data = resp.json()

        if not data:
            break

        for pr in data:
            created_at = datetime.fromisoformat(pr["created_at"].replace("Z", "+00:00"))

            # Stop once PRs are older than our window
            if created_at < since:
                return prs

            if since <= created_at <= until:
                merged_at = None
                business_days = ""
                status = "Open"

                if pr.get("merged_at"):
                    merged_at = datetime.fromisoformat(pr["merged_at"].replace("Z", "+00:00"))
                    business_days = business_days_between(created_at, merged_at)
                    status = "Merged"
                elif pr.get("closed_at"):
                    status = "Closed (not merged)"

                labels = ", ".join(l["name"] for l in pr.get("labels", []))

                prs.append({
                    "PR #": pr["number"],
                    "Title": pr["title"],
                    "Author": pr["user"]["login"],
                    "Status": status,
                    "Labels": labels,
                    "Created": created_at.strftime("%Y-%m-%d"),
                    "Merged": merged_at.strftime("%Y-%m-%d") if merged_at else "",
                    "Business Days to Merge": business_days,
                    "URL": pr["html_url"],
                })

        page += 1

    return prs


def main():
    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ.get("REPO", "mattermost/mattermost-docs")
    start_str = os.environ.get("START_DATE", "2026-02-01")
    end_str = os.environ.get("END_DATE", "2026-04-30")

    since = datetime.fromisoformat(start_str).replace(tzinfo=timezone.utc)
    until = datetime.fromisoformat(end_str).replace(
        hour=23, minute=59, second=59, tzinfo=timezone.utc
    )

    print(f"Fetching PRs from {start_str} to {end_str} in {repo}…")
    prs = fetch_prs(repo, token, since, until)
    print(f"Found {len(prs)} PRs")

    if not prs:
        print("No PRs found for this period.")
        return

    output_file = "pr_export.csv"
    fields = ["PR #", "Title", "Author", "Status", "Labels", "Created", "Merged",
              "Business Days to Merge", "URL"]

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(prs)

    print(f"✓ Exported {len(prs)} PRs to {output_file}")


if __name__ == "__main__":
    main()
