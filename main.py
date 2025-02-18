from src.generators import*

# usd_transactions = filter_by_currency(transactions, "USD")
# # print(next(usd_transactions))
# for transaction in usd_transactions:
#     print(transaction)
# #
# usd_transactions = filter_by_currency(transactions, "USD")
# for transaction in usd_transactions:
#     print(usd_transactions)
#
# try:
#         # Фильтрация по USD
#         usd_transactions = list(filter_by_currency(transactions, "USD"))
#         print("USD Transactions:", usd_transactions)
#         # Фильтрация по RUB
#         rub_transactions = list(filter_by_currency(transactions, "RUB"))
#         print("RUB Transactions:", rub_transactions)
#         # Попытка фильтрации с пустым кодом
#         empty_transactions = list(filter_by_currency(transactions, ""))
#         print("Транзакции с пустым кодом", empty_transactions)
#         # Этот код вызовет исключение ValueError
#         gbp_transactions = list(filter_by_currency(transactions, "GBP"))
#         print("GBP Transactions:", gbp_transactions)
#         miss_trans = list(filter_by_currency(transactions, None))
#         print("Miss code:", miss_trans)
#
# except ValueError as e:
#     print("Error:", e)

# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))



start_number = 1234567890123456
end_number = 1234567890123460  # Генерируем несколько номеров для примера

generator = card_number_generator(start_number, end_number)

if generator is not None:
    for card_number in generator:
            print(card_number)
    else:
        print("Некорректный диапазон номеров карт.")

    # Пример с меньшим числом разрядов для проверки добавления нулей
start_number = 1
end_number = 5
generator = card_number_generator(start_number, end_number)

if generator is not None:
    for card_number in generator:
        print(card_number)
    else:
        print("Некорректный диапазон номеров карт.")

#
# x = 10
# print(x)