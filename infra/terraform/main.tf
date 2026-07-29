resource "azurerm_resource_group" "sentinel" {
  name     = var.resource_group_name
  location = var.location

  tags = {
    application = "sentinel"
    environment = var.environment
    managed_by  = "terraform"
  }
}

# Add network, Key Vault, managed identities, diagnostic settings, API, data,
# Azure AI Search, Azure OpenAI, and device-management resources only after
# SKU, subscription, private networking, and Singapore-region availability are confirmed.
