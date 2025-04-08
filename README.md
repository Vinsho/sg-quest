# How to Run

Copy the `.env.template` file to `.env` and provide `GECKO_DEMO_API_KEY`

## Dockerized

- `docker compose build`
- `docker compose up -d`

## Local dev app

### Tailwind

- `npm i`
- `npm run watch-css`

### Python

- `pip install uv`
- `uv sync`
- `cd src && uv run -m main`
