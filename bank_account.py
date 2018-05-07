class User:
    def __init__(self, first_name, last_name, middle_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.bank_accounts = []

    def addBankAccount(self, bank_account):
        self.bank_accounts.append(bank_account)

class BankAccount:
    def __init__(self, user, account_type, balance, status):
        self.user = user
        self.account_type = account_type
        self.balance = balance
        self.status = status

    def open_account(self):
        if self.balance >= 100:
            self.status = "Opened"
            print(self.status, self.balance)

    def transfer_money(self, amount, toAccount):
        toAccount.balance += amount
        checking_acct.balance -= amount
        print(toAccount.balance, checking_acct.balance)

    def withdraw_money(self, amount):
        self.balance -= amount
        print(self.balance)

    def overdraft_charge(self):
        if self.balance <= 0:
            self.balance -= 35
            print(self.balance)

jordan = User("Jordan", "Michaels", "B")
checking_acct = BankAccount(jordan, "checking", 250, "Closed")
savings_acct = BankAccount(jordan, "savings", 0, "Opened")

checking_acct.open_account()

savings_acct.overdraft_charge()

checking_acct.transfer_money(20, savings_acct)

checking_acct.withdraw_money(100)
