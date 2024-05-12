FROM python:3.11

# Создаем директорию в контейнере для приложения
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем все файлы из текущей директории в директорию /app в контейнере
COPY . .

# Указываем команду для запуска приложения
CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
