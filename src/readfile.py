import pandas as pd


def load_transactions_from_csv(filepath: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV"""
    csv_data = pd.read_csv(filepath)
    transactions = csv_data.to_dict(orient="records")
    return transactions


file_path_csv = "C:/Users/User/PycharmProjects/hw101/data/transactions.csv"
transaction_csv = load_transactions_from_csv(file_path_csv)
print(transaction_csv)


def load_transactions_from_excel(filepath: str) -> list[dict]:
    """Функция считывает финансовые операции из Excel-файла и возвращает список словарей"""
    excel_data = pd.read_excel(filepath)
    transactions = excel_data.to_dict(orient="records")
    return transactions


file_path_excel = "C:/Users/User/PycharmProjects/hw101/data/transactions_excel.xlsx"
transactions_excel = load_transactions_from_excel(file_path_excel)
print(transactions_excel)
