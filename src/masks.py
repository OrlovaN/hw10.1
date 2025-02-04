def get_mask_card_number(cart_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    return f"{cart_number[0:4]} {cart_number[4:6]}XX XXXX {cart_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    return f"XX{account_number[-4:]}"
