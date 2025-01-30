def get_date(date: str) -> str:
    """Функция преобразования формата даты"""
    return f"{date[9:11]}.{date[6:8]}.{date[0:5]}"
date = input()
