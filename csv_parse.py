import csv
import json


def parse_csv(file_path):
    # Empty dictionary to store customers
    customers = {}

    # Use dict reader, so I can use column names rather than indexes
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            customer_id = row['customerId']
            account_id = row['accountId']
            description = row['transactionType']
            amount = float(row['amount'])

            # If the customer is not in the dictionary, add them with an empty accounts list
            if customer_id not in customers:
                customers[customer_id] = {'id': int(customer_id), 'accounts': []}

            # If the account is not in the customer's accounts list, add it with an initial balance of 0
            account_exists = any(acc['accountNumber'] == int(account_id) for acc in customers[customer_id]['accounts'])
            if not account_exists:
                customers[customer_id]['accounts'].append({'accountNumber': int(account_id), 'balance': 0})

            # Update the balance based on the transaction type and amount
            for account in customers[customer_id]['accounts']:
                if account['accountNumber'] == int(account_id):
                    if description == 'deposit':
                        account['balance'] += amount
                    else:
                        account['balance'] -= amount

    return customers


def main():
    file_path = 'resources/secondset.csv'  # Update with your actual file path
    customers = parse_csv(file_path)

    print(customers)

    # Sort customers and their accounts in ascending order
    sorted_customers = sorted(customers.values(), key=lambda x: x['id'])
    for customer in sorted_customers:
        customer['accounts'] = sorted(customer['accounts'], key=lambda x: x['accountNumber'])

    # Create a list of JSON strings with no indent and no trailing space between lines
    json_list = []
    for i, customer in enumerate(sorted_customers):
        json_list.append(json.dumps(customer, separators=(', ', ': ')))

    # Join the list into a single JSON string
    json_output = '[{}]'.format(',\n'.join(json_list))

    with open('resources/output2.json', 'w') as json_file:
        json_file.write(json_output + '\n')


if __name__ == "__main__":
    main()

