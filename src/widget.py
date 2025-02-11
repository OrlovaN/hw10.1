from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_data: str) -> str:
    """Функция маскировки данных счета или карты"""
    if "Счет" in account_data:
        account_data: str = "Счет " + get_mask_account(account_data[5:])
    elif "Maestro" in account_data or "MasterCard" in account_data or "Visa" in account_data:
        account_data: str = account_data[0:-17] + " " + get_mask_card_number(account_data[-16:])
    else:
        raise TypeError("Неправильный формат")
    return account_data


def get_date(date: str) -> str:
    """Функция преобразования формата даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
