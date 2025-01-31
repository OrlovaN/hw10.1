from masks import get_mask_card_number, get_mask_account

def mask_account_card(account_data: str) -> str:
     """Функция маскировки данных счета или карты"""
     if "Счет" in account_data:
         account_data_ = "Счет " + get_mask_account(account_data[5:])
     elif "Maestro" or "MasterCard" or "Visa Classic" or "Visa Platinum" or "Visa Gold" in account_data:
         account_data_ = account_data[0:-17] + " " + get_mask_card_number(account_data[-16:])
     return account_data_


def get_date(date: str) -> str:
    """Функция преобразования формата даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"




