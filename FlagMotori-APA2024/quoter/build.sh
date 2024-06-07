#!/bin/bash

docker build . -t quote-image && \
 docker container stop quote || true && \
 docker container rm quote || true && \
 docker run --name quote -p$1:1337 -d quote-image