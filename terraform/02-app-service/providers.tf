terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.70.0"
    }
  }
  required_version = ">= 1.5.5"

  # Must pass storage account credentials on the CLI.
  # Comment this out if you wish to deploy without using a remote backend (not recommended).
  backend "azurerm" {}
}

provider "azurerm" {
  features {}
}
