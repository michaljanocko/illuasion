FROM python:3-alpine

WORKDIR /app

RUN apk add --no-cache curl gcc musl-dev

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install

RUN curl -Lo unluac.jar https://sourceforge.net/projects/unluac/files/latest/download
RUN apk add openjdk20-jre --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community

COPY . .

EXPOSE 80

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
