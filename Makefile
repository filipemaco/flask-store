format:
	black .
	isort .


lint:
	black --check ./plasma/ ./tests/ ./scripts/
	isort --check ./plasma/ ./tests/ ./scripts/
	flake8 ./models/ ./resources/ app.py

build:
	pip install -r requirements.txt
	pre-commit install
