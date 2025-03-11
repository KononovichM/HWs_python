# Банковский вклад
class Deposit:
    def __init__(self, amount, years, rate=10):
        self.amount = amount
        self.years = years
        self.rate = rate

    def calculate(self):
        return round(self.amount * (1 + self.rate / 12 / 100) ** (self.years * 12), 2)


class Bank:
    def __init__(self):
        self.clients = {}

    def register_client(self, customer_id, name):
        self.clients[customer_id] = {"name": name, "deposit": None}

    def open_deposit_account(self, client_id1, amount, years):
        if client_id1 not in self.clients:
            print("Клиент " + client_id1 + " не зарегистрирован")
            return

        self.clients[client_id1]["deposit"] = Deposit(amount, years)
        print("Депозит успешно открыт")

    def calc_interest_rate(self, client_id1):
        if self.has_deposit(client_id1):
            return None

        deposit = self.clients[client_id1].get("deposit")
        return deposit.calculate() if deposit else None

    def has_deposit(self, client):
        result = self.clients[client]["deposit"] is None
        if result:
            print("Ошибка: У клиента " + client + " нет открытого депозита.")
        return result

    def close_deposit(self, client_id1):
        if self.has_deposit(client_id1):
            return

        self.clients[client_id1]["deposit"] = None


class CurrencyConverter:
    exchange_rates = {
        ('USD', 'BYN'): 3.269,
        ('EUR', 'BYN'): 7.04,
        ('USD', 'EUR'): 0.929,
        ('EUR', 'USD'): 1.076
    }

    def exchange_currency(self, from_currency, amount, to_currency='BYN'):
        if from_currency == to_currency:
            return amount, to_currency

        rate = self.exchange_rates.get((from_currency, to_currency))
        if rate is None:
            raise ValueError(f"Cannot convert from {from_currency} to {to_currency}")

        return round(amount * rate, 2), to_currency


class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


client_id = "0000001"

bank = Bank()
bank.register_client(client_id, "Siarhei")
bank.open_deposit_account(client_id, 1000, 1)

assert bank.calc_interest_rate(client_id) == \
       1104.71, "Ошибка: расчетная сумма по вкладу отличается от ожидаемой!"

bank.close_deposit(client_id)

client_id2 = "0002"
bank.open_deposit_account(client_id2, 100, 5)
bank.register_client(client_id2, "Rita")
bank.calc_interest_rate(client_id2)
bank.close_deposit(client_id2)


converter = CurrencyConverter()

vasya = Person('USD', 10)
petya = Person('EUR', 5)

assert converter.exchange_currency(vasya.currency, vasya.amount) \
       == (32.69, "BYN"), "Conversion error"
assert converter.exchange_currency(petya.currency, petya.amount) \
       == (35.20, "BYN"), "Conversion error"
assert converter.exchange_currency(vasya.currency, vasya.amount, 'EUR') \
       == (9.29, "EUR"), "Conversion error"
assert converter.exchange_currency(petya.currency, petya.amount, 'USD') \
       == (5.38, "USD"), "Conversion error"
