FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "test_app.py"]

EXPOSE 5000

CMD ["python", "app.py"]