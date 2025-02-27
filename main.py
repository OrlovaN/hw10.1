from src.generators import*
import json
from src.utils import load_transactions_from_json, get_transaction_amount_in_rub
import os


data_dir = load_transactions_from_json("")
#print(json.dumps(data_dir, indent=4, ensure_ascii=False))


    #  фиктивные транзакции
transaction_rub = {"amount": 100.0, "code": "RUB"}
transaction_usd = {"amount": 50.0, "code": "USD"}
transaction_eur = {"amount": 20.0, "code": "EUR"}
transaction_unknown = {"amount": 100.0, "code": "XYZ"}
transaction_missing = {"amount": None, "code": "RUB"}

# Test the function
amount_rub = get_transaction_amount_in_rub(transaction_rub)
print(f"Transaction in RUB: {amount_rub}")

amount_usd = get_transaction_amount_in_rub(transaction_usd)
print(f"Transaction in USD: {amount_usd}")

amount_eur = get_transaction_amount_in_rub(transaction_eur)
print(f"Transaction in EUR: {amount_eur}")

amount_unknown = get_transaction_amount_in_rub(transaction_unknown)
print(f"Transaction in XYZ: {amount_unknown}")

amount_missing = get_transaction_amount_in_rub(transaction_missing)
print(f"Transaction with missing {amount_missing}")

# usd_transactions = filter_by_currency(transactions, "USD")
# # print(next(usd_transactions))
# for transaction in usd_transactions:
#     print(transaction)
# # #
# # usd_transactions = filter_by_currency(transactions, "USD")
# # for transaction in usd_transactions:
# #     print(usd_transactions)
# #
# # try:
# #         # Фильтрация по USD
# #         usd_transactions = list(filter_by_currency(transactions, "USD"))
# #         print("USD Transactions:", usd_transactions)
# #         # Фильтрация по RUB
# #         rub_transactions = list(filter_by_currency(transactions, "RUB"))
# #         print("RUB Transactions:", rub_transactions)
# #         # Попытка фильтрации с пустым кодом
# #         empty_transactions = list(filter_by_currency(transactions, ""))
# #         print("Транзакции с пустым кодом", empty_transactions)
# #         # Этот код вызовет исключение ValueError
# #         gbp_transactions = list(filter_by_currency(transactions, "GBP"))
# #         print("GBP Transactions:", gbp_transactions)
# #         miss_trans = list(filter_by_currency(transactions, None))
# #         print("Miss code:", miss_trans)
# #
# # except ValueError as e:
# #     print("Error:", e)
#
# # descriptions = transaction_descriptions(transactions)
# # for _ in range(5):
# #     print(next(descriptions))
#
#
# #
# # start_number = 1234567890123456
# # end_number = 1234567890123460  # Генерируем несколько номеров для примера
# #
# # generator = card_number_generator(start_number, end_number)
# #
# # if generator is not None:
# #     for card_number in generator:
# #             print(card_number)
# #     else:
# #         print("Некорректный диапазон номеров карт.")
#
#     # Пример с меньшим числом разрядов для проверки добавления нулей
# start_number = 1
# end_number = 5
# generator = card_number_generator(start_number, end_number)
#
# if generator is not None:
#     for card_number in generator:
#         print(card_number)
#     else:
#         print("Некорректный диапазон номеров карт.")

#
# x = 10
# print(x)