from typing import List, Dict
import csv


def read_csv_and_retrieve_accounts(file_name: str) -> List[Dict]:
    with open(file_name, mode='r') as arquivo:
        leitor_csv = csv.reader(arquivo, delimiter=";")

        accounts = []
        for i, row in enumerate(leitor_csv):
            if len(row) == 0:
                continue
            dict = {
                "name": row[0],
                "birthday": row[1],
                "cpf": row[2],
                "street_name": row[3],
                "number": row[4],
                "neighborhood": row[5],
                "state": row[6],
            }

            accounts.append(dict)
        return accounts


