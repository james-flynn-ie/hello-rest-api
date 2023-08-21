# Important: RG and ACR must have been deployed first (see ../01-acr/main.tf) 
# and the <acr-name>.azurecr.io/hello-rest-api:latest Docker image must exist within ACR.
data "azurerm_resource_group" "rg" {
  name = var.rg_name
}

data "azurerm_container_registry" "acr" {
  name                = var.acr_name
  resource_group_name = data.azurerm_resource_group.rg.name
}

resource "azurerm_service_plan" "app_service_plan" {
  name                = var.app_svc_plan_name
  location            = data.azurerm_resource_group.rg.location
  resource_group_name = data.azurerm_resource_group.rg.name
  os_type             = var.app_svc_plan_os_type
  sku_name            = var.app_svc_plan_sku_name
}

resource "azurerm_linux_web_app" "webapp" {
  name                = var.web_app_name
  location            = data.azurerm_resource_group.rg.location
  resource_group_name = data.azurerm_resource_group.rg.name
  service_plan_id     = azurerm_service_plan.app_service_plan.id

  https_only = true
  site_config {
    application_stack {
      docker_image_name        = "hello-rest-api:latest"
      docker_registry_url      = "https://${var.acr_name}.azurecr.io"
      docker_registry_username = data.azurerm_container_registry.acr.admin_username
      docker_registry_password = data.azurerm_container_registry.acr.admin_password
    }
    always_on = false
  }

  app_settings = {
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = false
    # Publishes port for Docker container. Azure Web App expects port 80 to be exposed.
    WEBSITES_PORT = var.web_app_websites_port
    WEBSITES_CONTAINER_START_TIME_LIMIT = 300
  }
}
