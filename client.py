import datetime
from typing import List, Union
from uuid import uuid4

from account import Account


class Address:

    def __init__(self) -> None:
        self.street_name: str = ""
        self.number: int = 0
        self.neighborhood: str = ""
        self.state: str = ""

    def set_street_name(self, street_name) -> None:
        self.street_name = street_name

    def get_street_name(self) -> str:
        return self.street_name

    def set_number(self, number) -> None:
        self.number = number

    def get_number(self) -> int:
        return self.number

    def set_neighborhood(self, neighborhood) -> None:
        self.neighborhood = neighborhood

    def get_neighborhood(self) -> str:
        return self.neighborhood

    def set_state(self, state) -> None:
        self.state = state

    def get_state(self) -> str:
        return self.state

    def get_full_address(self):
        return  f"{self.get_street_name()}, {self.get_number()} - {self.get_neighborhood()} - {self.get_state()}"

class Client:

    def __init__(self) -> None:
        self.id = str(uuid4())
        self.accounts: List[Account] = []
        self.address: Union[Address | None] = None
        self.name: str = ""
        self.birthday: datetime
        self.cpf: str = "sadf"

    def set_address(self, address: Address) -> None:
        self.address = address

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_birthday(self, birthday: str) -> None:
        #"07/04/1989"
        day, month, year = birthday.split("/")
        # "07", "04", "1989"
        birthday = datetime.date(year=int(year), month=int(month), day=int(day))
        self.birthday = birthday

    def get_birthday(self) -> str:
        return f'{self.birthday.day}/{self.birthday.month}/{self.birthday.year}'

    def set_cpf(self, cpf: str) -> None:
        self.cpf = cpf

    def get_cpf(self) -> str:
        return self.cpf

    def set_account(self, account: Account) -> None:
        self.accounts.append(account)

    def get_account(self):
        pass

    def get_full_client_data(self):

        print(f"======= Client: {self.get_name()} ======= ")
        print(f"Data de nascimento: {self.get_birthday()}")
        print("Endereço:")
        print(f"Rua: {self.address.get_street_name()}")
        print(f"Número: {self.address.get_number()}")
        print(f"Bairro: {self.address.get_neighborhood()}")

        print("Contas:")
        for account in self.accounts:
            print(f"Número da conta: {account.account_number} | Criada em: {account.get_created_at()}")

        print("==========================================")




