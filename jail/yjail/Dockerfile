FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR jail

COPY jail.py ./
COPY flag.py ./

RUN pip install --upgrade pip
RUN pip install pyyaml

ENTRYPOINT ["python3", "-B", "jail.py"]
