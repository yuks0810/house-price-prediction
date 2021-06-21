FROM python:3.8.0
RUN apt-get update -y && apt-get upgrade -y
# COPY Pipfile Pipfile.lock ./
# RUN pip install pipenv \
#  && pipenv install --system --dev

ENTRYPOINT  ["/bin/sh", "-c", "while :; do sleep 10; done"]
