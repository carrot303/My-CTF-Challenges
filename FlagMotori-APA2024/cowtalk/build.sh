#!/bin/bash

docker build . -t cowtalk-image && \
 docker container stop cowtalk || true && \
 docker container rm cowtalk || true && \
 docker run --name cowtalk -p$1:1337 -d cowtalk-image