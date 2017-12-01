# Google credentials are set with this environment variable:
# GOOGLE_CLOUD_KEYFILE_JSON

variable "dns_zone_name" {
  type        = "string"
  description = "The GCP name of the DNS zone to use for this environment"
  default     = "helm-charts-win"
}

variable "project" {
  type        = "string"
  description = "The GCP project name that contains this environment"
  default     = "cloud-native-182609"
}

variable "region" {
  type        = "string"
  description = "The region where this environment will be provisioned"
  default     = "europe-west2"
}

variable "environment" {
  type        = "string"
  description = "The name for this environment"
}

