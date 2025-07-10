FROM alpine

WORKDIR  /app

RUN apk update && apk add python3

COPY app.py .

ENTRYPOINT [ "python3", "app.py" ]