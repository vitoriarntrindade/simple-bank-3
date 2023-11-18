from account import Account
from client import Address, Client
from utils import read_csv_and_retrieve_accounts
import csv

bank_clients = []
account_incremental_number = 0

while True:
    operation = input("Which operation do you want to do?\n"
                      "[1] Create Account\n"
                      "[2] List Clients\n"
                      "[3] Creat accounts by CSV file\n"
                      "[0] Logout \n")

    if operation == "1":
        name = input("Digit your name: ")
        birthday = input("Digit your birthday: ")
        cpf = input("Digit your cpf: ")
        print("==Now you need to insert your address info==")
        street_name = input("Digit the street name: ")
        number = input("Digite the number: ")
        neighborhood = input("Digit the neighborhood name: ")
        state = input("Digit state name: ")

        account_incremental_number += 1
        account = Account()
        account.set_account_number(account_number=account_incremental_number)

        client_address = Address()
        client_address.set_street_name(street_name=street_name)
        client_address.set_number(number=number)
        client_address.set_neighborhood(neighborhood=neighborhood)
        client_address.set_state(state=state)

        client = Client()
        client.set_name(name=name)
        client.set_birthday(birthday=birthday)
        client.set_cpf(cpf=cpf)
        client.set_account(account=account)
        client.set_address(address=client_address)

        account.set_client_id(client_id=client.id)

        bank_clients.append(client)

        while True:
            result_input = input("Do you want to create another account to this client? Y/N:").lower()

            if result_input == "y":
                account_incremental_number += 1
                extra_account = Account()
                extra_account.set_account_number(account_number=account_incremental_number)
                client.set_account(account=extra_account)

            if result_input == "n":
                break

    if operation == "2":
        for client in bank_clients:
            client.get_full_client_data()

    if operation == "3":

        file_name_input = input("Digite o nome do arquivo csv \n")

        try:
            if ".csv" not in file_name_input:
                accounts = read_csv_and_retrieve_accounts(file_name=file_name_input + ".csv")
            else:
                accounts = read_csv_and_retrieve_accounts(file_name=file_name_input)
        except:
            print('Arquivo não encontrado, verifique o nome do arquivo e tente novamente!')

        for account_ in accounts:
            account_incremental_number += 1

            account = Account()
            account.set_account_number(account_number=account_incremental_number)

            client_address = Address()
            client_address.set_street_name(street_name=account_["street_name"])
            client_address.set_number(number=account_["number"])
            client_address.set_neighborhood(neighborhood=account_["neighborhood"])
            client_address.set_state(state=account_["state"])

            client = Client()
            client.set_name(name=account_["name"])
            client.set_birthday(birthday=account_["birthday"])
            client.set_cpf(cpf=account_["cpf"])
            client.set_account(account=account)
            client.set_address(address=client_address)

            account.set_client_id(client_id=client.id)

            bank_clients.append(client)

    if operation == "4":
        pass

    if operation == "5":
        pass

    if operation == "6":
        break
