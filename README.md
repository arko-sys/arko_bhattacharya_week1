# Python Project

Welcome to the Python Project! This repository contains a Python application with automated testing, linting, and code formatting. It is configured to use Docker and GitHub Actions for a consistent development environment and continuous integration.

## Project Structure

- `src/`: Contains the source code for the project.
- `tests/`: Contains the unit tests for the project.
- `requirements.txt`: Lists the Python dependencies.
- `Makefile`: Defines common tasks like installing dependencies, running tests, and linting.
- `.devcontainer/`: Contains VS Code configuration for a development container.
- `.github/workflows/`: Contains GitHub Actions workflows for continuous integration.


## Getting Started

### Prerequisites

- **Docker**: [Install Docker](https://www.docker.com/products/docker-desktop) for containerized development.
- **VS Code**: [Download VS Code](https://code.visualstudio.com/) and install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.

### Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Open the Project in VS Code:**

    - Open VS Code.
    - Go to `File` > `Open Folder...` and select the project directory.

3. **Reopen in Container:**

    - Press `F1` to open the Command Palette.
    - Type `Remote-Containers: Reopen Folder in Container` and select it.
    
    This will build the Docker container as specified in `.devcontainer/Dockerfile` and configure VS Code for development inside the container.

### Running the Project

1. **Build the Docker Image:**

    If you prefer to build and run the Docker container manually, you can do so with the following commands:

    ```bash
    docker build -t python-project .
    ```

2. **Run the Docker Container:**

    ```bash
    docker run -it --rm -v $(pwd):/app python-project
    ```

### Using the Makefile

The `Makefile` provides shortcuts for common tasks. Ensure you have `make` installed on your system.

1. **Install Dependencies:**

    ```bash
    make install
    ```

2. **Run Tests:**

    ```bash
    make test
    ```

3. **Lint and Format Code:**

    ```bash
    make lint
    make format
    ```

4. **Clean Artifacts:**

    ```bash
    make clean
    make clean-dist
    ```

### GitHub Actions

The repository uses GitHub Actions for CI/CD. The workflows are defined as follows:

- **`test.yml`**: Runs unit tests on pushes to `master` or `main` and on pull requests.
- **`lint.yml`**: Runs linting and formatting checks on pushes to `master` or `main` and on pull requests.

These workflows ensure that code quality and tests are maintained consistently.

### Contribution

To contribute to this project:

1. **Create a New Branch:**

    ```bash
    git checkout -b feature-branch
    ```

2. **Make Your Changes and Commit:**

    ```bash
    git add .
    git commit -m "Add your commit message"
    ```

3. **Push Your Branch:**

    ```bash
    git push origin feature-branch
    ```

4. **Create a Pull Request:**

    Go to the repository on GitHub and create a pull request from your branch.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

