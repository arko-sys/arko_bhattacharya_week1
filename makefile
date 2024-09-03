PYTHON=python3
PIP=pip
VENV=venv
SRC=src
TEST=tests
FORMAT=black
LINT=pylint

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(VENV)/bin/$(PIP) install --upgrade $(PIP)
	$(VENV)/bin/$(PIP) install -r requirements.txt

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +

clean-dist: clean
	rm -rf $(VENV)

format:
	$(VENV)/bin/$(FORMAT) $(SRC)/*.py $(TEST)/*.py

lint:
	$(VENV)/bin/$(LINT) $(SRC)/*.py $(TEST)/*.py || true

test:
	$(VENV)/bin/$(PYTHON) -m unittest discover -s $(TEST) -v

run:
	$(VENV)/bin/$(PYTHON) $(SRC)/main.py

to-test: clean-dist install format lint test

to-run: clean-dist install format lint test run