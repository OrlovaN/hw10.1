import datetime
import logging
import os
from functools import wraps
from typing import Any, Callable


def log(filename: str = "") -> Callable:
    """Функция автоматической регистрации деталей выполнения операций"""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            if filename:
                log_file_path = os.path.abspath(filename)
                logger = logging.getLogger(func_name)
                logger.setLevel(logging.INFO)
                logger.handlers.clear()
                try:
                    file_handler = logging.FileHandler(log_file_path)
                    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
                    file_handler.setFormatter(formatter)
                    logger.addHandler(file_handler)
                except Exception as e:
                    raise

                start_time = datetime.datetime.now()
                log_message = f"Функция '{func_name}' запущена в {start_time.strftime('%Y-%m-%d %H:%M:%S')}"
                logger.info(log_message)
            else:
                start_time = datetime.datetime.now()
                log_message = f"Функция '{func_name}' запущена в {start_time.strftime('%Y-%m-%d %H:%M:%S')}"
                print(log_message)
            try:
                result = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                execution_time = (end_time - start_time).total_seconds()
                log_message = f"Функция '{func_name}' завершена успешно. Результат: {result}, Время выполнения: {execution_time:.4f} сек в {end_time.strftime('%Y-%m-%d %H:%M:%S')}"

                if filename:
                    logger.info(log_message)
                else:
                    print(log_message)
                    return result

            except Exception as e:
                end_time = datetime.datetime.now()
                execution_time = (end_time - start_time).total_seconds()
                log_message = f"Ошибка в функции '{func_name}'. Тип ошибки: {type(e).__name__}, Параметры: args={args}, kwargs={kwargs}, Время выполнения: {execution_time:.4f} сек"
                if filename:
                    logger.error(log_message)
                else:
                    print(log_message)
                    raise

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y
my_function(1, 0)
