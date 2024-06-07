#!/bin/bash

docker build . -t emolite-image && \
 docker container stop emolite || true && \
 docker container rm emolite || true && \
 docker run --name emolite -p$1:1337 -d emolite-image