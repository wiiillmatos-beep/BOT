# Usa Python 3.11 slim
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do bot
COPY . .

# Comando para iniciar o bot
CMD ["python", "bot_teste.py"]
