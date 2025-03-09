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
        self.clients[client_id1]["deposit"] = Deposit(amount, years)

    def calc_interest_rate(self, client_id1):
        deposit = self.clients[client_id1].get("deposit")
        return deposit.calculate() if deposit else None

    def close_deposit(self, client_id1):
        if self.clients[client_id1]["deposit"] is None:
            print("Ошибка: У клиента нет открытого депозита.")
            return
        self.clients[client_id1]["deposit"] = None


client_id = "0000001"

bank = Bank()
bank.register_client(client_id, "Siarhei")
bank.open_deposit_account(client_id, 1000, 1)

assert bank.calc_interest_rate(client_id) == \
       1104.71, "Ошибка: расчетная сумма по вкладу отличается от ожидаемой!"

bank.close_deposit(client_id)
