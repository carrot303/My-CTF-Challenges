#!/bin/bash

docker build . -t inspect-element-image && \
 docker container stop inspect-element || true && \
 docker container rm inspect-element || true && \
 docker run --name inspect-element -p$1:80 -d inspect-element-image
