FROM python:3.11-slim
WORKDIR /app
COPY executor.py /app/executor.py
RUN pip install --no-cache-dir redis ccxt python-dotenv
CMD ["python", "executor.py"]
