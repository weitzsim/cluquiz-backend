
FROM ghcr.io/astral-sh/uv:alpine3.22

# Copy the project into the image
COPY . /app

# Disable development dependencies
ENV UV_NO_DEV=1

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked
ENTRYPOINT ["uv", "run", "flask", "--app", "main", "run"]

# start container with
# docker run --name myflask --rm -d -p 5000:5000 myflask --host=0.0.0.0 --port=5000
# access on localhost:5000 on dev machine


