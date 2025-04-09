import datetime


class BankAccount:
    """
    A class to implement a bank account.
    """

    def __init__(self, account_number, holder_name, account_type, initial_balance=0.0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__account_type = account_type
        self.__balance = initial_balance
        self.__transaction_history = []
        self.__add_transaction("Account created", initial_balance)

    def deposit(self, amount):
        if amount <= 0:
            return False

        self.__balance += amount
        self.__add_transaction(f"Deposit", amount)
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            return False

        self.__balance -= amount
        self.__add_transaction(f"Withdrawal", -amount)
        return True

    def get_balance(self):
        return self.__balance

    def get_account_type(self):
        return self.__account_type

    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def get_transaction_history(self):
        return self.__transaction_history.copy()

    def __add_transaction(self, transaction_type, amount):

        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": amount,
            "balance": self.__balance
        }
        self.__transaction_history.append(transaction)

    def __str__(self):
        return f"Account Number: {self.__account_number}\n" \
            f"Holder Name: {self.__holder_name}\n" \
            f"Account Type: {self.__account_type}\n" \
            f"Current Balance: ${self.__balance:.2f}"


# Test the BankAccount class
if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", "Savings", 1000.0)
    print("Account created successfully:")
    print(account)
    print("\n")

    deposit_amount = 500.0
    if account.deposit(deposit_amount):
        print(f"Successfully deposited ${deposit_amount:.2f}")
    else:
        print("Deposit failed")
    print(f"New balance: ${account.get_balance():.2f}")
    print("\n")

    withdraw_amount = 200.0
    if account.withdraw(withdraw_amount):
        print(f"Successfully withdrew ${withdraw_amount:.2f}")
    else:
        print("Withdrawal failed")
    print(f"New balance: ${account.get_balance():.2f}")
    print("\n")

    if not account.deposit(-100):
        print("Invalid deposit rejected (negative amount)")

    if not account.withdraw(2000):
        print("Invalid withdrawal rejected (amount exceeds balance)")
    print("\n")

    print(f"Account Number: {account.get_account_number()}")
    print(f"Holder Name: {account.get_holder_name()}")
    print(f"Account Type: {account.get_account_type()}")``
    print(f"Current Balance: ${account.get_balance():.2f}")
    print("\n")

    print("Transaction History:")
    for transaction in account.get_transaction_history():
        amount_str = f"${abs(transaction['amount']):.2f}"
        if transaction['type'] == "Account created":
            print(
                f"{transaction['date']} - {transaction['type']} with initial balance of {amount_str}")
        elif transaction['type'] == "Deposit":
            print(
                f"{transaction['date']} - {transaction['type']} of {amount_str}")
        elif transaction['type'] == "Withdrawal":
            print(
                f"{transaction['date']} - {transaction['type']} of {amount_str}")
        print(f"    Balance after transaction: ${transaction['balance']:.2f}")
