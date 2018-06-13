# Changelog Manager

This tool integrates the [changelog entries](changelog.md) produced as part of this
projects development workflow.

## Dependencies

The script is written in Ruby. You will need Ruby `>= 2.3.3`. Gem dependencies are
managed via Bundler.

## Manual task

To run this task manually, begin with a clone of this repository. You must have push
access to the `master` branch.

```sh
git checkout master
git pull master
bundle install
scripts/changelog_manager.rb .
git push
```

## CI Automation

This task will be integrated with CI in the future. It is currently blocked by
[#344](https://gitlab.com/charts/gitlab/issues/344)
