FROM python:3.11-slim

# Evita perguntas durante instalação e buffering de output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependências Python
COPY requirements.* .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.prod.txt

# Copia código da aplicação
COPY . .

# Porta do Gunicorn
EXPOSE 8000

# Script de inicialização
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]