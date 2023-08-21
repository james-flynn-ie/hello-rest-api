FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app
COPY ./hello_rest_api/app.py /app

RUN pip install --no-cache-dir -r requirements.txt

# Must be set to port 80 for Azure Web App.
EXPOSE 80

CMD ["python", "app.py"]