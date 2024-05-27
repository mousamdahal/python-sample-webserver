# Hello World Python Web Server

This is a simple Python web server that serves a "Hello, World!" message when you visit the root URL (`/`). The server is designed to be containerized using Docker.

## Requirements

- Docker

## Usage

### Running with Docker

1. Build the Docker image:

  docker build -t hello-world-server .

2. Run the container:

  docker run -p 8080:8000 -e PORT=8080 hello-world-server

This command runs the `hello-world-server` container and maps the host's port `8080` to the container's port `8000`. It also sets the `PORT` environment variable inside the container to `8080`.

3. Visit `http://localhost:8080` in your web browser to see the "Hello, World!" message.

## Configuration

The web server listens on the port specified by the `PORT` environment variable. If the `PORT` variable is not set, it defaults to `8000`.

You can change the default port by setting the `PORT` environment variable when running the container.

## Files

- `hello_world_server.py`: The Python script that runs the web server.
- `Dockerfile`: The Dockerfile used to build the Docker image.
- `README.md`: This file, containing instructions and information about the project.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
