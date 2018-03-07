data "google_dns_managed_zone" "dns_zone" {
  name    = "${var.dns_zone_name}"
  project = "${var.project}"
}

resource "google_compute_address" "default" {
  name         = "tf-${var.environment}-${var.dns_zone_name}"
  project      = "${var.project}"
  region       = "${var.region}"
  address_type = "EXTERNAL"
}

resource "google_dns_record_set" "gitlab" {
  name = "gitlab-${var.environment}.${data.google_dns_managed_zone.dns_zone.dns_name}"
  type = "A"
  ttl  = 60

  managed_zone = "${data.google_dns_managed_zone.dns_zone.name}"
  project      = "${var.project}"

  rrdatas = ["${google_compute_address.default.address}"]
}

resource "google_dns_record_set" "registry" {
  name = "registry-${var.environment}.${data.google_dns_managed_zone.dns_zone.dns_name}"
  type = "A"
  ttl  = 60

  managed_zone = "${data.google_dns_managed_zone.dns_zone.name}"
  project      = "${var.project}"

  rrdatas = ["${google_compute_address.default.address}"]
}

resource "google_dns_record_set" "minio" {
  name = "minio-${var.environment}.${data.google_dns_managed_zone.dns_zone.dns_name}"
  type = "A"
  ttl  = 60

  managed_zone = "${data.google_dns_managed_zone.dns_zone.name}"
  project      = "${var.project}"

  rrdatas = ["${google_compute_address.default.address}"]
}

output "loadBalancerIP" {
  value = "${google_compute_address.default.address}"
}
