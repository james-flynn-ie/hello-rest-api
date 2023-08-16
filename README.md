## Requirements

Python v3.11

## Use VirtualEnv

Virtualenv is used to isolate Python environments. For more information, see the [virtualenv docs](https://virtualenv.pypa.io/en/stable/)

To set up virtualenv (for Windows/Git Bash):

```
pip install virtualenv

cd <project root directory>
python -m virtualenv venv
.\venv\Scripts\activate
```

## Run and test the application locally

```
pip install -r requirements.txt
python hello-rest-api/app.py
```

Enter the URL http://127.0.0.1:5000/api/v1/hello in a browser to view the Hello World page. 

Use the following command to access the handshake endpopint:

```
curl --request POST --url http://127.0.0.1:5000/api/v1/handshake
```
