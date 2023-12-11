import pandas as pd
import csv
import json


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
            amount = float(row['amount'])

            target_cell = (customer_id, account_id), ('balance')

            if transaction_type == 'deposit':
                df.loc[target_cell] += amount
            if transaction_type == 'withdrawal':
                df.loc[target_cell] -= amount

    return df


def format_df_to_list(df):
    customers = {}

    for row in df.itertuples():
        customer_id = row.Index[0]
        account_id = row.Index[1]
        balance = row.balance

        if customer_id not in customers:
            customers[customer_id] = {'id': customer_id, 'accounts': []}

        account_data = {'account_id': account_id, 'balance': balance}
        customers[customer_id]['accounts'].append(account_data)

    return list(customers.values())




# Convert secondset.csv
df = csv_to_df('resources/secondset.csv')
df = calculate_balances('resources/secondset.csv', df)
customer_list = format_df_to_list(df)

# Convert the list to JSON
json_output = json.dumps(customer_list, indent=2)

# Writing to sample.json
with open('resources/output2.json', 'w') as output:
    output.write(json_output)




# Convert transactions.csv
df = csv_to_df('resources/transactions.csv')
df = calculate_balances('resources/transactions.csv', df)
customer_list = format_df_to_list(df)

# Convert the list to JSON
json_output = json.dumps(customer_list, indent=2)

# Writing to sample.json
with open('resources/output1.json', 'w') as output:
    output.write(json_output)
