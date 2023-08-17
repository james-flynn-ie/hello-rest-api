## Requirements

Python v3.11

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

## Test the "hello" endpoint

Enter the URL http://127.0.0.1:5000/api/v1/hello in a browser to view the Hello World page. 
Refreshing the browser should alternate the response between "hello" and "Hello from new v1".

## Test the "handshake" endpoint

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

## Linting

Linted using PyLint, MyPy and Flake8.
