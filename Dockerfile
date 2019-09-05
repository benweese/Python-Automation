FROM alpine:latest
MAINTAINER ben.weese@gmail.com

RUN apk update && apk add \
    curl \
    git \
    vim \
    chromium \
    chromium-chromedriver \
    python3
    
RUN python3 -m pip install --upgrade pip \
    && pip install pipenv 
