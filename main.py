from src.generators import card_number_generator, transaction_descriptions, filter_by_currency, transactions


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


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)

x = 10
print(x)
