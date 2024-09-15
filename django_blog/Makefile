# Makefile for Django Blog Project

# Variables
PROJECT_NAME = django_blog
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MANAGE = $(PYTHON) manage.py

# Default environment setup
install:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

# Run Django development server
run:
	$(MANAGE) runserver

# Apply migrations
migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

# Create a superuser
superuser:
	$(MANAGE) createsuperuser

# Run tests
test:
	$(MANAGE) test

# Collect static files
collectstatic:
	$(MANAGE) collectstatic --noinput

# Clean up unnecessary Python files
clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

# Format code with black
format:
	$(PYTHON) -m black .

# Lint code with flake8
lint:
	$(PYTHON) -m flake8 .

# Run the debug server with the Django Debug Toolbar enabled
debug:
	DEBUG=True $(MANAGE) runserver

# Set up database and create initial migrations
setup-db:
	$(MANAGE) migrate
	$(MANAGE) createsuperuser
	$(MANAGE) loaddata initial_data.json

# Install or update requirements
requirements:
	$(PIP) freeze > requirements.txt
