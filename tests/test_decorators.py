import os

import pytest

from src.decorators import log


def test_log_1(capsys):
    """Тестируем успешное логирование в консоль"""

    @log()
    def my_function(x, y):
        return x + y

    result = my_function(2, 3)
    captured = capsys.readouterr()
    assert "Функция 'my_function' запущена" in captured.out
    assert "Функция 'my_function' завершена успешно. Результат: 5" in captured.out
    assert str(result) in captured.out


def test_log_2(capsys):
    """Тестируем логирование в консоль с исключением"""

    @log()
    def my_function(x, y):
        raise ValueError("Test exception")

    with pytest.raises(ValueError) as excinfo:
        my_function(2, 3)
    captured = capsys.readouterr()
    assert "Функция 'my_function' запущена" in captured.out  # Проверяем вывод в stdout
    assert "Ошибка в функции 'my_function'. Тип ошибки: ValueError" in captured.out  # Проверяем ошибку в stderr
    assert "Test exception" in str(excinfo.value)


def test_log_to_file_success():
    """Тестируем логирование в файл"""
    log_file = os.path.abspath("test_log.txt")

    @log(filename=log_file)
    def my1_function(x, y):
        return x + y

    result = my1_function(2, 3)

    # Проверяем, что файл был создан
    assert os.path.exists(log_file)

    # Проверяем содержимое файла
    with open(log_file, "r") as f:
        log_content = f.read()
        assert "Функция 'my1_function' запущена" in log_content
        assert "Функция 'my1_function' завершена успешно" in log_content
        assert "5" in log_content
