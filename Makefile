# Makefile
# Target Framework: NDH-Canvas-Adapter-Enhanced
# Domain: Localized Pipeline Orchestration & Workspace Sovereignty
# Status: Production-Ready Script

.PHONY: help env format test verify build clean

# Shell configuration for consistent execution
SHELL := /bin/bash
VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
PYTEST := $(VENV_DIR)/bin/pytest
BLACK := $(VENV_DIR)/bin/black

help:
	@echo "===================================================================="
	@echo "🏗️  NDH-CANVAS-ADAPTER-ENHANCED PIPELINE ORCHESTRATION"
	@echo "===================================================================="
	@echo "Available commands:"
	@echo "  make env          - Initialize Python venv and install dependencies"
	@echo "  make format       - Run code formatting verification using Black"
	@echo "  make test         - Run Pytest suite for boundary containment metrics"
	@echo "  make verify       - Compile Lean 4 formal math proofs via Lake"
	@echo "  make build        - Comprehensive end-to-end local system verification"
	@echo "  make clean        - Strip compiler artifacts and virtual environments"
	@echo "===================================================================="

# Initialize workspace sovereignty environment
env:
	@echo "[+] Constructing isolated local virtual environment..."
	python3 -m venv $(VENV_DIR)
	@echo "[+] Injecting dependencies from pyproject.toml..."
	$(PIP) install --upgrade pip
	$(PIP) install .
	@echo "[+] Resolving Lean 4 package environment packages..."
	lake update
	@echo "[+] Sovereignty Environment initialized successfully."

# Format code blocks via Black toolhead routines
format:
	@if [ ! -f $(BLACK) ]; then echo "[-] Black toolhead not found. Please run 'make env' first."; exit 1; fi
	@echo "[+] Running stylistic consistency checks across Python routines..."
	$(BLACK) --check src/ tests/

# Execute Pytest suite for boundary containment and SVD metrics
test:
	@if [ ! -f $(PYTEST) ]; then echo "[-] Pytest core engine not found. Please run 'make env' first."; exit 1; fi
	@echo "[+] Launching numeric boundary containment and SVD validation checks..."
	$(PYTEST) -v tests/test_geometry.py

# Execute Lean 4 formal verification build targets
verify:
	@echo "[+] Entering Lean 4 Vault to compile formal mathematical proofs..."
	lake build

# Master end-to-end local workspace orchestration
build: format test verify
	@echo "===================================================================="
	@echo "✅ [SUCCESS] All pipeline invariants verified flawlessly."
	@echo "   - Python code architecture formatted."
	@echo "   - Numeric boundary containment metrics passed."
	@echo "   - Lean 4 continuous hypersphere proofs compiled."
	@echo "===================================================================="

# Strip environment and compiler cache states
clean:
	@echo "[-] Clearing computational artifacts and local environment footprints..."
	rm -rf $(VENV_DIR)
	rm -rf .pytest_cache
	rm -rf .lake
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "[+] Workspace clean."
