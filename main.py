import csv
import json


# Create a dictionary with below format
# {<customer_id> : {"id": 11,
#                       "accounts": [{"accountNumber": 21,
#                                     "balance": 812.45}
#                                    {"accountNumber": 24,
#                                     "balance": -542.67}]},


def parse_csv(path):
    # Empty dictionary for customer information
    # Key is customerId: value is a dictionary
    customers = {}

    # Use dict reader, so I can use column names rather than indexes
    with open(path, 'r') as csv_file:
        file = csv.DictReader(csv_file)

        for row in file:
            customer_id = int(row['customerId'])
            account_id = int(row['accountId'])
            transaction_type = row['transactionType']
            amount = float(row['amount'])

            # Check is customer_id exists, if not add with empty accounts list
            if customer_id not in customers:
                customers[customer_id] = {'id:': customer_id,
                                          'accounts': []}

    print(customers)

    pass


parse_csv('resources/secondset.csv')