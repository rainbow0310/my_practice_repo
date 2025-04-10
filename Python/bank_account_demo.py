from bank_account import BankAccount #getting bank account

account1 = BankAccount("1234", 1000)
print(account1)

account2 = BankAccount("13245")
print(account2)

account1.withdraw(20)
print(account1)
account1.deposit(300)
print(account1.get_balance())


