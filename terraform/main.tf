terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.8.0"
    }
    
  }
}

# Configure the Microsoft Azure Provider:
provider "azurerm" {
  features {
    key_vault {
        purge_soft_delete_on_destroy    = true
        recover_soft_deleted_key_vaults = false
        }
    resource_group {prevent_deletion_if_contains_resources = false}    
    }
    
}

# Retrieve information about the currently authenticated Azure client:
data "azurerm_client_config" "current" {}

resource "azurerm_resource_group" "sql_bootcamp_rg" {
  name     = "rg-telefonica-sql-bootcamp-${random_string.random_two.result}"
  location = "UK South"
}


# Work around to get object_id:
data external account_info {
  program  = ["az", "ad", "signed-in-user", "show", "--query", "{object_id:id}", "-o", "json"]
}

# Create random string for SQL server password:
resource "random_string" "random" {
  length           = 16
  special          = true
  override_special = "/@£$"
}

# Create random string for SQL server password:
resource "random_string" "random_two" {
  length           = 5
  special          = false
  lower =           true
  upper = false
}

resource "azurerm_mssql_server" "sql_bootcamp_server" {
  name                         = "sql-bootcamp-server-${random_string.random_two.result}"
  resource_group_name          = azurerm_resource_group.sql_bootcamp_rg.name
  location                     = azurerm_resource_group.sql_bootcamp_rg.location
  version                      = "12.0"
  administrator_login          = "bootcamp_login"
  administrator_login_password = random_string.random.result
  minimum_tls_version          = "1.2"
  tags = {
    environment = "dev"
  }
  public_network_access_enabled = true
  
}

# FIREWALL RULES:
# Add firewall rule to allow connection from Azure services:
resource "azurerm_mssql_firewall_rule" "allow_azure_services" {
  name             = "AllowAzureServices"
  server_id       = azurerm_mssql_server.sql_bootcamp_server.id
  start_ip_address = "0.0.0.0"
  end_ip_address   = "0.0.0.0"
}
# Add firewall rule to allow connection from personal ip address:
data "http" "my_ip" {
# This will dynamically grab the users IP address.
  url = "https://api64.ipify.org?format=text"
}
# Create firewall rule with the individuals ip address:
resource "azurerm_mssql_firewall_rule" "allow_my_ip" {
  name             = "AllowMyIP"
  server_id        = azurerm_mssql_server.sql_bootcamp_server.id
  start_ip_address = data.http.my_ip.response_body
  end_ip_address   = data.http.my_ip.response_body
}

# Write to env file:
resource "local_file" "env_file" {
  filename = "../.env"
  content  = <<EOT
server_name="${azurerm_mssql_server.sql_bootcamp_server.name}.database.windows.net"
server_user = "${azurerm_mssql_server.sql_bootcamp_server.administrator_login}"
server_password = "${random_string.random.result}"
resource_group_name = "${azurerm_resource_group.sql_bootcamp_rg.name}"
connection_string = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:${azurerm_mssql_server.sql_bootcamp_server.name}.database.windows.net,1433;Database=${azurerm_mssql_database.northwind_database.name};Uid=${azurerm_mssql_server.sql_bootcamp_server.administrator_login};Pwd=${azurerm_mssql_server.sql_bootcamp_server.administrator_login_password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

EOT
depends_on = [ azurerm_mssql_server.sql_bootcamp_server,  azurerm_resource_group.sql_bootcamp_rg ]
}


# Setup Northwind database:
resource "azurerm_mssql_database" "northwind_database" {
  name         = "northwind"
  server_id    = azurerm_mssql_server.sql_bootcamp_server.id
  collation    = "SQL_Latin1_General_CP1_CI_AS"
  license_type = "LicenseIncluded"
  max_size_gb  = 1
  sku_name     = "S0"
  
  # Allow database to be destroyed
  lifecycle {
    prevent_destroy = false
  }
  depends_on = [ azurerm_mssql_server.sql_bootcamp_server ]
}
