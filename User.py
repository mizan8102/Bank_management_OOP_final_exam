import random


class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = name[:2] + str(random.randint(1, 100)) + email[:3]
        self.loanCount = 0
        self.loanAmount = 0
        self.loanLock = False
