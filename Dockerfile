FROM python:3.9-slim-buster
LABEL author="diogoduartec"

ENV PYTHONUNBUFFERED 1

COPY ./poetry.lock /
COPY ./pyproject.toml /

ENV PATH="${PATH}:/root/.poetry/bin"

RUN apt-get update -y && apt-get install curl libjpeg-dev zlib1g-dev -y \
&& curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
&& poetry config virtualenvs.create false \
&& poetry install \
&& apt-get remove curl -y

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# who execs cointainer will only have access to /app directory (security)
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser --disabled-password user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
