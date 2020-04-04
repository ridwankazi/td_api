FROM python:3.6-alpine3.10
# Create app directory
WORKDIR /td_api

RUN apk add --no-cache gcc musl-dev

COPY requirements.txt /td_api

RUN pip install -r requirements.txt

COPY . /td_api

EXPOSE 8080

CMD ["python", "./app.py"]
