# Sinair Minecraft Admin

Панель управления Minecraft-сервером.

## Требования
* **Python:** 3.14

## Настройка окружения

Перед запуском проекта создайте файл `.env` в корневой директории на основе примера:

```env
UVICORN_HOST=0.0.0.0
UVICORN_PORT=8000
MANAGEMENT_API_BASE_URL=http://test/
```

---

## Быстрый старт (Локально)

1. **Создайте и активируйте виртуальное окружение:**
   ```bash
   # Для Windows:
   py -3.14 -m venv venv
   source venv\Scripts\activate
   # Для Linux/macOS:
   python3.14 -m venv venv
   source venv/bin/activate
   ```

2. **Установите зависимости:**
   * **Для разработки**:
     ```bash
     pip install -r requirements-dev.txt
     ```
   * **Только для продакшена**:
     ```bash
     pip install -r requirements.txt
     ```

3. **Запуск сервера:**
   Проект запускается как модуль Python напрямую из корневой директории:
   ```bash
   python -m app.main
   ```
   *Интерактивная документация API (Swagger UI) откроется по адресу:* `http://localhost:<ваш_порт>/docs`
