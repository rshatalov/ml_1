import os

class Config:
    # Общие настройки
    JSON_AS_ASCII = False  # Отключаем ASCII-кодировку для JSON
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Выбор конфигурации
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}