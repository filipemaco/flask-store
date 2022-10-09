format:
	black .
	isort .


lint:
	black --check .
	flake8 .

build:
	pip install -r requirements.txt
