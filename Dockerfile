# -------- Stage 1: Run Tailwind CSS --------
FROM node:slim as build
WORKDIR /build
COPY package*.json ./
RUN npm ci
COPY src/ ./src/
COPY tailwind.config.js .
RUN npm run css

# -------- Stage 2: Run the app --------
FROM python:3.13-slim

RUN apt-get update && apt-get install -y libpq-dev
RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

ENV UV_PROJECT_ENVIRONMENT="/usr/local/"
RUN uv sync --locked --no-dev

COPY --from=build /build/src/static/dist /app/src/static/dist

COPY src/ ./src/

RUN chmod +x ./src/entrypoint.sh

WORKDIR /app/src

EXPOSE 8000

# Run the app
ENTRYPOINT ["./entrypoint.sh"]
