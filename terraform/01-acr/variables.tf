# Resource Group
variable "rg_name" {
  description = "Resource Group Name"
  type        = string
  default     = "rg-neu-hello-rest-api"
}

variable "rg_location" {
  description = "Azure location. See the full list by executing: az account list-locations"
  type        = string
  default     = "North Europe"
}

# ACR
variable "acr_name" {
  description = "Azure Container Registry Name"
  type        = string
  default     = "acrneuhellorestapi"
}

variable "acr_sku" {
  description = "Azure Container Registry SKU Type"
  type        = string
  default     = "Standard"
}
