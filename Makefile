.PHONY: env format test clean

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

env:
	@echo "🏗️ Initializing localized environment..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e .[dev]
	@echo "✅ Environment initialized. Run 'source $(VENV)/bin/activate' to use."

format:
	@echo "🎨 Running formatters and linters..."
	$(PYTHON) -m black src/ tests/
	$(PYTHON) -m ruff check src/ tests/ --fix

test:
	@echo "🧪 Firing verification suite..."
	$(PYTHON) -m pytest tests/

clean:
	rm -rf $(VENV)
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
