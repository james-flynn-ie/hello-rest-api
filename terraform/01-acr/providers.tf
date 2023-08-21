terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.70.0"
    }
  }
  required_version = ">= 1.5.5"
}

provider "azurerm" {
  features {}
}
