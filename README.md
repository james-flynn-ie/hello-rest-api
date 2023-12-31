# Hello Rest API

[![hello-rest-api lint and test](https://github.com/james-flynn-ie/hello-rest-api/actions/workflows/main.yml/badge.svg)](https://github.com/james-flynn-ie/hello-rest-api/actions/workflows/main.yml)

A Flask web App that contains two endpoints.

- /api/v1/hello: Returns round-robin responses
- /api/v1/handshake: Demonstrates the use of basic authentication.

## Requirements

- Python v3.11
- Docker
- Terraform
- AZ CLI
- Azure subscription

## Use VirtualEnv

Virtualenv is used to isolate Python environments. For more information, see the [virtualenv docs](https://virtualenv.pypa.io/en/stable/)

To set up virtualenv (for Windows/Git Bash):

```
pip install virtualenv

cd <project root directory>
python -m virtualenv venv

# On Windows PowerShell:
.\venv\Scripts\activate
# Or on Git Bash:
source ./venv/Scripts/activate
```

## Run the application locally

To launch the Flask web server, run the following commands:

```
pip install -r requirements.txt
python hello_rest_api/app.py
```

## Testing 

### Testing the "hello" endpoint

Enter the URL http://127.0.0.1:5000/api/v1/hello in a browser to view the Hello World page. 
Refreshing the browser should alternate the response between "hello" and "Hello from new v1".

### Testing the "handshake" endpoint

The handshake endpoint has basic authentication on place.

Use the following cURL command to access the handshake endpoint with Admin RBAC privileges:

```
curl --request POST --user "admin:admin_password" --url http://127.0.0.1:5000/api/v1/handshake
```


Use the following cURL command to return a 403 Forbidden message for a user without admin RBAC privileges:

```
curl --request POST --user "user:user_password" --url http://127.0.0.1:5000/api/v1/handshake
```

Note that a 401 Unauthorized response will be returned if no username and password are sent:

```
curl --request POST --url http://127.0.0.1:5000/api/v1/handshake
```

### Linting

Linted using PyLint, MyPy and Flake8.

## Docker

### Test container

Run the following command to build the container:

```
docker build hello-rest-api:latest .
```

Start the container locally using the command:

```
docker run -p 80:5000 hello-rest-api:latest
```

Open a browser to access the hello endpoint.

```
http://localhost/api/v1/hello
```

The handshake API can be reached through cURL, run from a different terminal:

```
curl --request POST --user "admin:admin_password" http://127.0.0.1/api/v1/handshake 
```

### Push container to Azure Container Registry (ACR)

To push a container to ACR, first tag the build with the ACR's Fully Qualified Domain Name:

```
docker build -t <<name-of-acr>>.azurecr.io/hello-rest-api:latest .

docker push <<name-of-acr>>.azurecr.io/hello-rest-api:latest
```

## Terraform

Terraform is an infrastructure as code tool that lets you build, change, and version cloud resources safely and efficiently. 

The scripts are broken into two phases for deployment:

- 01-acr: Contains the resource group and ACR that are required for the App service to be deployed.
- 02-app-service: Contains the App Service Plan and Web App that will host the application.

### Commands

```
cd terraform

# Download Terraform providers
terraform init

# Check syntax
terraform validate

# Check plan (For production use, it is recommended to save the file using `-out` and use it in the apply stage)
terraform plan

# Deploy the infrastructure
terraform apply

# Destroy the infrastructure
terraform apply -destroy
```

### Test the App Service

#### Hello API endpoint

Open a browser to access the hello endpoint.

```
https://<<name-of-web-app>>.azurewebsites.net/api/v1/hello
```

#### Handshake API endpoint

To access the web-app's handshake endpoint, run the following command.:

```
curl --request POST --user "admin:admin_password" --url https://<<name-of-web-app>>.azurewebsites.net/api/v1/handshake
```

## Github Actions Workflow

Github Actions workflow will lint and test code on each push. 

Pushes to main will deploy the Docker container on an App Service.

### Requirements for Deploying an Azure App Service

- Azure Managed Identity with:
  - (Federated credentials)[https://github.com/marketplace/actions/azure-login#configure-a-federated-credential-to-use-oidc-based-authentication] linked to Github Actions.
    - AZURE_CLIENT_ID
    - AZURE_TENANT_ID
    - AZURE_SUBSCRIPTION_ID
  - Permissions to deploy an App Service within the resource group or subscription.
  - Credentials stored as (secrets)[https://docs.github.com/en/actions/security-guides/encrypted-secrets] in Github Actions.

- Terraform Backend:
  - Azure Storage Account with:
    - SAS token
    - Resource Group Name
    - Container Name
    - Key name (Name of TF State file within container)
