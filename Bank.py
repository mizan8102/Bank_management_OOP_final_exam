from User import User


class Bank:
    bankDraft = False

    def __init__(self) -> None:
        self.transaction_history = []
        self.accounts = []

    # create account
    def create_account(self, user):
        self.accounts.append(self.user)

    # delete account
    def delete_account(self, account_number):
        usr = [u for u in self.accounts if u.account_number == account_number]
        self.accounts.remove(usr)

    # all user list
    def all_user(self):
        for index, usr in enumerate(self.accounts):
            print(
                f"{index}. Account number = {usr.account_number}, name = { usr.name}, and {type} balance = { usr.balance}"
            )

    # get available amount of Bank
    def availableAmountOfBank(self) -> int:
        total = 0
        for usr in self.accounts:
            total += usr.balance

        return total

    # total loan amount
    def total_loan_amount(self) -> int:
        total = 0
        for usr in self.accounts:
            total += usr.loanAmount

        return total

    # loan feature active and deactive
    def isActiveDeactiveLoan(self, account_number: int) -> None:
        usr: User = [u for u in self.accounts if u.account_number == account_number]
        usr.isLoanActive = not usr.isLoanActive

    # change loan lock
    def loan_lock(self, account_number: int) -> None:
        usr: User = [u for u in self.accounts if u.account_number == account_number]
        usr.loanLock = True

    # amount transfer
    def amount_transfer(
        self, my_account: str, transfer_account, transfer_amount: int
    ) -> None:
        usr: User = [u for u in self.accounts if u.account_number == my_account]
        trn_usr: User = [
            u for u in self.accounts if u.account_number == transfer_account
        ]
        if trn_usr:
            if usr.balance >= transfer_amount:
                trn_usr.balance += transfer_amount
                usr.balance -= transfer_amount

            else:
                print("Your have not enough amount to transfer")
        else:
            print("Account does not exist")

    # get current amount
    def current_balance(self, account_number: int) -> int:
        usr: User = [u for u in self.accounts if u.account_number == account_number]
        print(f"Current Balance = {usr.balance}")

    # trnsaction history
    def transaction_history(
        self, account_number: str, name: str, amount: int, type: str
    ) -> None:
        self.transaction_history.append(
            f"Account number = {account_number}, name = { name}, and {type} amount = { amount}"
        )

    # withdraw amount
    def withdraw_amount(self, account_number: str, amount: int) -> None:
        usr: User = [u for u in self.accounts if u.account_number == account_number]

        # bank draft check
        if self.bankDraft:
            print(f"the bank is bankrupt")
            return

        if amount > 0:
            if usr.balance < amount:
                print("Withdrawal amount exceeded")
            else:
                usr.balance -= amount
                print(f"Withdraw successfull. Account Number = { usr.account_number}")
                self.current_balance(account_number)
                # trasaction history
                self.transaction_history(account_number, usr.name, amount, "withdraw")

        else:
            print("amount must be greater than 0 ")

    # deposit amount
    def deposit_amount(self, account_number: int, amount: int) -> None:
        usr: User = [u for u in self.accounts if u.account_number == account_number]

        # bank draft check
        if self.bankDraft:
            print(f"the bank is bankrupt")
            return

        if amount > 0:
            usr.balance += amount
            print(f"Deposit successfull. Account Number = { usr.account_number}")
            print(f"your current balance = { usr.balance}")

            # trasaction history
            self.transaction_history(account_number, usr.name, amount, "Deposit")

    # get loan
    def getLoan(self, account_number: int, amount: int) -> None:
        usr: User = [u for u in self.accounts if u.account_number == account_number]
        if usr.loanCount < 2 and usr.loanLock:
            usr.balance += amount
            usr.loanAmount += amount
            usr.loanCount += 1
            print("Your Load is granted")
            self.current_balance(account_number)

            # trasaction history
            self.transaction_history(account_number, usr.name, amount, "Loan")
        else:
            print(f"Your loan is not granted.")
