FROM python:3.11-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копирование файлов
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py .

# Создаем директорию для БД с правильными правами
RUN mkdir -p /app/data && chmod 777 /app/data

# Запуск с проверкой
CMD ["sh", "-c", "echo 'Directory contents:' && ls -la /app/data && echo 'Starting bot...' && python bot.py"]
