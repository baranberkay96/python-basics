# Class örnekleri yapmak için kullanıldı.

class Customer(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.accounts = []
        self.balance = 0

    def open_account(self, account_name):
        self.accounts.append(account_name)
        return self.accounts

    def deposit(self, amount):
        self.balance += amount
        return self.balance


ahmet = Customer(name="Ahmet", surname="soyad")

accounts = ahmet.open_account('3343535')

print(accounts)

print(ahmet.deposit(600))