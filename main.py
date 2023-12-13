import pandas as pd
import csv
import json
from decimal import *


def csv_to_df(file_path):
    df = pd.read_csv(file_path, index_col='transactionId', usecols=[0, 1, 2])
    df = df.drop_duplicates(subset=['customerId', 'accountId'])
    df = df.set_index(['customerId', 'accountId']).sort_index()
    df['balance'] = 0.0
    return df


def calculate_balances(file_path, df):
    with open(file_path, 'r') as csv_file:
        file = csv.DictReader(csv_file)

        for row in file:
            customer_id = int(row['customerId'])
            account_id = int(row['accountId'])
            transaction_type = row['transactionType']
            amount = Decimal(row['amount'])

            target_cell = (customer_id, account_id), ('balance')
            current_balance = Decimal(df.loc[target_cell])

            if transaction_type == 'deposit':
                df.loc[target_cell] = current_balance + Decimal(amount)
            if transaction_type == 'withdrawal':
                df.loc[target_cell] = current_balance - Decimal(amount)

    return df


def format_df_to_list(df):
    customers = {}

    for row in df.itertuples():
        customer_id = row.Index[0]
        account_id = row.Index[1]
        balance = row.balance

        if customer_id not in customers:
            customers[customer_id] = {'id': customer_id, 'accounts': []}

        account_data = {'accountNumber': account_id, 'balance': float(balance)}
        customers[customer_id]['accounts'].append(account_data)

    return list(customers.values())

def list_to_JSON(file_path):
    json_output = json.dumps(customer_list, indent=2)

    with open(file_path, 'w') as output:
        output.write(json_output)




# Convert secondset.csv
df = csv_to_df('resources/secondset.csv')
df = calculate_balances('resources/secondset.csv', df)
customer_list = format_df_to_list(df)
list_to_JSON('resources/output2.json')


# Convert transactions.csv
df = csv_to_df('resources/transactions.csv')
df = calculate_balances('resources/transactions.csv', df)
customer_list = format_df_to_list(df)
list_to_JSON('resources/output1.json')
