from datetime import datetime


class Account:
    def __init__(self) -> None:
        self.client_id: str = ''
        self.agency_number: str = "001"
        self.account_number: int = 0
        self.withdraw_value_limit: int = 500
        self.account_balance: int = 0
        self.account_history: str = " "
        self.withdraw_quantity_limit: int = 3
        self.created_at = datetime.now()

    def get_created_at(self):
        return (f'{self.created_at.day}/{self.created_at.month}/{self.created_at.year}  '
                f'{self.created_at.hour}:{self.created_at.minute}:{self.created_at.second}')

    def set_client_id(self, client_id: int) -> None:
        self.client_id = client_id

    def get_client_id(self) -> str:
        return self.client_id

    def set_account_number(self, account_number: int) -> None:
        self.account_number = account_number

    def get_account_number(self) -> int:
        return self.account_number

    def deposit(self, deposit_amount):
        """"""
        self.account_balance += deposit_amount
        self.account_history += f"-Foi depositado:           + R${deposit_amount:5.2f} \n"
        print(f"-Foi depositado:           + R${deposit_amount:5.2f} \n")

    def withdraw(self, withdraw_value):
        """"""
        if self.withdraw_quantity_limit == 0:
            print(f"Limite de saque excedido. \n")
        else:
            if withdraw_value > self.withdraw_value_limit:
                print(f"Valor por saque excedido! \n")
            elif self.account_balance < withdraw_value:
                print("Não foi possível efetuar o saque por falta de saldo!")
            else:
                self.account_balance -= withdraw_value
                self.withdraw_quantity_limit -= 1
                self.account_history += f"-Foi sacado:               - R${withdraw_value:5.2f}\n"
                print(f"-Foi sacado:               - R${withdraw_value:5.2f}\n")

    def account_history_info(self):
        history = f"""
        \n===================================================="
        \n{self.account_history}
        \nO seu saldo atual é de R${self.account_balance:5.2f}
        \n====================================================\n
        """
        return history
