FROM python:3.9-slim-bullseye
LABEL author="diogoduartec"

ENV PYTHONUNBUFFERED 1

COPY ./poetry.lock /
COPY ./pyproject.toml /

ENV PATH="${PATH}:/root/.poetry/bin"

RUN apt-get update && apt-get install curl -y \
&& curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
&& poetry config virtualenvs.create false \
&& poetry install \
&& apt-get remove curl -y

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# who execs cointainer will only have access to /app directory (security)
RUN adduser --disabled-password user
USER user
