FROM alpine:latest
LABEL maintainer="ben@benweese.dev"

RUN apk --no-cache add \
    curl \
    git \
    vim \
    chromium \
    chromium-chromedriver \
    python3

RUN python3 -m pip install --upgrade pip \
    && pip install pipenv 
