FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# O mapeamento do docker.sock é essencial aqui (Página 5)
CMD ["python", "app.py"]