# Python Template

This project is to demonstarte how to create a standard scaffolding along with dockerizing the project and setting up a CI/CD process.

## Project Function
- Add two 'numpy' arrays and store it in a third array
- Create a 'pandas' dataframe to store the aforementioned arrays
- Convert the dataframe to a '.csv' file.

## Project Structure

- `src/`: Contains the source code for the project.
- `tests/`: Contains the unit tests for the project.
- `requirements.txt`: Lists the Python dependencies.
- `Makefile`: Defines common tasks like installing dependencies, running tests, linting, and running docker.
- `.devcontainer/`: Contains `Dockerfile` and VS Code configuration.
- `.github/workflows/`: Contians CI/CD workflows for GitHub.

## Project Setup
### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/nogibjj/arko_bhattacharya_week1.git
cd arko_bhattacharya_week1
```
### 2. Dockerize

Build and Run the Docker image:

```bash
docker build -f .devcontainer/Dockerfile -t <image-name> .
docker run -it --rm -v $(pwd):/app <image-name> /bin/sh
```

## GitHub Ci/Cd Setup
- `.github/workflows/`: Contians CI/CD workflows for GitHub.
  





