import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(r"C:\Users\User\PycharmProjects\hw101\logs\masks.logs", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(cart_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if not isinstance(cart_number, str):
        logger.error(f"Неверный тип данных для номера карты: {type(cart_number)}. Ожидается str.")
        return f"Ошибка: Неверный тип данных для номера карты: {type(cart_number)}. Ожидается str."

    if len(cart_number) != 16:
        logger.warning(f"Номер карты имеет неверную длину: {len(cart_number)}. Ожидается 16.")
    else:
        logger.debug(f"Начало маскировки номера карты: {cart_number}")
        mask_number = f"{cart_number[0:4]} {cart_number[4:6]}XX XXXX {cart_number[-4:]}"
        logger.info("Номер карты успешно замаскирован.")
        logger.debug(f"Замаскированный номер карты: {mask_number}")
        return mask_number


if __name__ == "__main__":
    card_number = "1234567890123456"
    masked_number = get_mask_card_number(card_number)
    print(f"Замаскированный номер карты: {masked_number}")


# def get_mask_account(account_number: str) -> str:
#     """Функция маскировки номера банковского счета"""
# return f"XX{account_number[-4:]}"
def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    if not isinstance(account_number, str):
        logger.error(f"Неверный тип данных для номера счета: {type(account_number)}. Ожидается str.")
        return "Ошибка: Неверный тип данных"

    if len(account_number) < 20:
        logger.warning(f"Номер счета слишком короткий: {len(account_number)}. Требуется ввести 20 цифр номера счета.")
    else:
        logger.debug(f"Начало маскировки номера счета: {account_number}")
        masked_number = f"XX{account_number[-4:]}"
        logger.info("Номер счета успешно замаскирован.")
        logger.debug(f"Замаскированный номер счета: {masked_number}")  # Логируем результат (можно убрать в production)
        return masked_number


if __name__ == "__main__":
    account_number = "12345678901234567890"
    masked_number = get_mask_account(account_number)
    print(f"Замаскированный номер счета: {masked_number}")
