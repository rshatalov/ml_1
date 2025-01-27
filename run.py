import os
from app import create_app

# Создаем приложение с конфигурацией для продакшна
app = create_app(config_name='production')

if __name__ == '__main__':
    # Запуск приложения
    app.run(host='0.0.0.0', port=5000)