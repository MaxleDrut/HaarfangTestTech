VENV=venv
PYTHON=python3
BASE_URL=http://localhost:8000

$(VENV):
	$(PYTHON) -m venv $(VENV)

install: $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

clear:
	rm -rf $(VENV)
	rm -rf "data/*"

run: install
	$(VENV)/bin/uvicorn src.main:app --reload

tests: install
	$(VENV)/bin/python3.11 -m unittest tests/*.py