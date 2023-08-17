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

## Run and test the application locally

To launch the Flask web server, run the following commands:

```
pip install -r requirements.txt
python hello_rest_api/app.py
```

Enter the URL http://127.0.0.1:5000/api/v1/hello in a browser to view the Hello World page. 
Refreshing the browser should alternate the response between "hello" and "Hello from new v1".

Use the following command to access the handshake endpoint:

```
curl --request POST --url http://127.0.0.1:5000/api/v1/handshake
```

## Linting

Linted using PyLint, MyPy and Flake8.
