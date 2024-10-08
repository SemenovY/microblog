import logging.config

# Имя файла для хранения логов ошибок
ERROR_LOG_FILENAME = "errors.log"

# Конфигурация логирования
LOGGING_CONFIG = {
    "version": 1,  # Версия конфигурации
    "disable_existing_loggers": True,  # Отключаем существующие логгеры, чтобы избежать конфликтов
    "formatters": {  # Форматтеры определяют формат лог-сообщений
        "default": {  # Имя форматтера
            "format": "%(asctime)s:%(name)s:%(process)d:%(lineno)d %(levelname)s %(message)s",  # Формат лог-сообщения
            "datefmt": "%Y-%m-%d %H:%M:%S",  # Формат даты и времени
        },
    },
    "handlers": {  # Обработчики определяют, куда отправлять лог-сообщения
        "logfile": {  # Имя обработчика
            "formatter": "default",  # Используемый форматтер (определен выше)
            "level": "INFO",  # Уровень логирования (записываем сообщения уровня INFO и выше)
            "class": "logging.FileHandler",  # Класс обработчика, который записывает логи в файл
            "filename": ERROR_LOG_FILENAME,  # Имя файла для логов
            "mode": "w",  # Режим записи в файл (перезаписывать файл каждый раз)
        },
        "console": {  # Имя обработчика для вывода в консоль
            "formatter": "default",  # Используемый форматтер (определен выше)
            "level": "DEBUG",  # Уровень логирования (выводим сообщения уровня DEBUG и выше)
            "class": "logging.StreamHandler",  # Класс обработчика, который выводит логи в консоль
            "stream": "ext://sys.stdout",  # Поток вывода (консоль)
        },
    },
    "loggers": {
        "slave": {  # Имя логгера
            "level": "INFO",  # Уровень логирования (записываем сообщения уровня INFO и выше)
            "handlers": ["logfile", "console"],  # Обработчики для этого логгера (используемые обработчики определены выше)
        },
    },
}

# Применяем конфигурацию логирования
logging.config.dictConfig(LOGGING_CONFIG)

# Создаем логгер с именем "slave", который будет использовать конфигурацию, заданную для логгера "slave"
logger = logging.getLogger("slave")

# Пример использования логгера: запись информационного сообщения
logger.info("Логгер %s настроен и готов к использованию", "slave")
