variable "environment" {
  description = "Deployment environment, such as dev, staging, or prod."
  type        = string
}

variable "location" {
  description = "Azure region. Confirm service availability before production."
  type        = string
  default     = "southeastasia"
}

variable "resource_group_name" {
  description = "Target Azure resource group."
  type        = string
}
