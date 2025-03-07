import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")


def convert_currency(amount: float, from_currency: str, to_currency: str = "RUB") -> float:
    """
    Функция конвертирует валюты из USD и EUR в рубли с использованием Exchange Rates Data API
    """

    if from_currency == to_currency:
        return amount

    endpoint = f"{URL}convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["result"]

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None
    except KeyError:
        print("Ошибка в структуре ответа API.  Ключ 'result' отсутствует.")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None
