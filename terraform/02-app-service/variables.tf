# Resource Group
variable "rg_name" {
  description = "Resource Group Name"
  type        = string
  default     = "rg-neu-hello-rest-api"
}

# ACR
variable "acr_name" {
  description = "Azure Container Registry Name"
  type        = string
  default     = "acrneuhellorestapi"
}

# App Service Plan
variable "app_svc_plan_name" {
  description = "App Service Name"
  type        = string
  default     = "asp-neu-hello-rest-api"
}

variable "app_svc_plan_os_type" {
  description = "App Service OS Type"
  type        = string
  default     = "Linux"
}

variable "app_svc_plan_sku_name" {
  description = "App Service SKU Name"
  type        = string
  default     = "B1"
}

# Linux Web App
variable "web_app_name" {
  description = "Web App Service Name"
  type        = string
  default     = "app-neu-hello-rest-api"
}

variable "web_app_websites_port" {
  description = "Web App Websites Port app setting. Required for publishing the Docker port."
  type        = string
  default     = "5000"
}

