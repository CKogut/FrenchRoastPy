import pandas as pd


class Customer:
    def __init__(self, customerId):
        self.customerId = customerId
        self.accounts = []

    def __str__(self):
        return f"{self.customerId}({self.accounts})"


class Account:
    def __init__(self, accountId):
        self.accountId = accountId
        self.balance = 0

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"{self.accountId}({self.balance})"


# Create df using only needed information
df = pd.read_csv('resources/secondset.csv',
                 index_col='transactionId',
                 usecols=[0, 1, 2, 3, 4])

print(df.head())

customerIdList = []
customerList = []

for index, row in df.iterrows():
    if row['customerId'] not in customerIdList:
        customerList.append(Customer(row['customerId']))
        customerIdList.append(row['customerId'])

print(customerIdList)
print(customerList)


