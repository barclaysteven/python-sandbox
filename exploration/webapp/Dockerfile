FROM alpine:latest

RUN apk add --update python py-pip

COPY requirements.txt /src/requirements.txt

RUN pip install -r /src/requirements.txt

COPY helloworldapp /src/helloworldapp

EXPOSE 8000
CMD ["python", "/src/helloworldapp", "-p 8000"]
