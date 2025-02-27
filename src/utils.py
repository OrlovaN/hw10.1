import json
import logging
from typing import Any

from dotenv import load_dotenv

from src.external_api import convert_currency

load_dotenv()


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(r"C:\Users\User\PycharmProjects\hw101\logs\utils.logs", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions_from_json(operations: str) -> list[dict[str, Any]]:
    """Функция преобразования JSON-файла в объект Python"""
    filepath = "data/operations.json"
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.info(f"Файл {filepath} успешно загружен.")

        if not isinstance(data, list):
            logger.warning(f"Файл {filepath} содержит данные не в виде списка.")
            return []
        logger.debug(f"Загружено {len(data)} транзакций.")
        return data

    except FileNotFoundError:
        logger.error(f"Файл не найден: {filepath}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {filepath}")
        return []
    except Exception:
        logger.exception(f"Произошла непредвиденная ошибка при загрузке файла: {filepath}")
        return []


def get_transaction_amount_in_rub(transaction: dict[str, Any]) -> float:
    """Функуия возвращает сумму транзакции в рублях"""
    logger.debug(f"Обработка транзакции: {transaction}")
    amount = transaction.get("amount")
    currency = transaction.get("code")

    if amount is None or currency is None:
        logger.error("Отсутствует 'amount' или 'code' в транзакции.")
        return None
    try:
        if currency == "RUB":
            logger.info(f"Сумма в рублях: {float(amount)}")
            return float(amount)
        elif currency in ("USD", "EUR"):
            logger.info(f"Конвертация из {currency} в RUB.")
            converted_amount = convert_currency(float(amount), currency, "RUB")
            if converted_amount is not None:
                logger.info(f"Сумма после конвертации в рублях: {float(converted_amount)}")
                return float(converted_amount)
            else:
                logger.warning(f"Не удалось конвертировать {currency} в RUB.")
                return None
        else:
            logger.warning(f"Неподдерживаемая валюта: {currency}")
            return None
    except ValueError:
        logger.error(f"Некорректное значение 'amount': {amount}. Ожидается число.")
        return None
    except Exception:
        logger.exception(f"Произошла непредвиденная ошибка при обработке транзакции: {transaction}")
        return None
