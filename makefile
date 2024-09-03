# Variables
PYTHON=python3
PIP=pip
VENV=venv
SRC=src

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(VENV)/bin/$(PIP) install --upgrade $(PIP)
	$(VENV)/bin/$(PIP) install -r requirements.txt

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +

dist-clean: clean
	rm -rf $(VENV)

test: install
	$(VENV)/bin/$(PYTHON) -m unittest $(SRC)/test_script.py -v

run: install
	$(VENV)/bin/$(PYTHON) $(SRC)/main.py

help:
	@echo "Available targets:"
	@echo "  venv          - Create a virtual environment"
	@echo "  install       - Install dependencies"
	@echo "  clean         - Remove compiled Python files"
	@echo "  dist-clean    - Remove virtual environment and clean"
	@echo "  run           - Run the application"
	@echo "  help          - Show available targets"
