FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-chache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]