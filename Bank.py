from User import User


class Bank:
    bankDraft = False

    def __init__(self) -> None:
        self.accounts = []

    # set bank draft
    def setBankDraft(self, opt: bool) -> None:
        self.bankDraft = opt

    # create account
    def create_account(self, user):
        self.accounts.append(user)
        print("Account created successful")

    # delete account
    def delete_account(self, account_number):
        usr: User = [u for u in self.accounts if u.account_number == account_number]
        if usr:
            self.accounts.remove(usr[0])
            print("User deleted successful\n")
        else:
            print("cann't delete . try again\n")

    # all user list
    def all_user(self):
        if len(self.accounts):
            for index, usr in enumerate(self.accounts):
                print(
                    f"{index+1}. Account number = {usr.account_number}, name = { usr.name}, and email = {usr.email}, balance = { usr.balance}"
                )
        else:
            print("There have no users")

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

    # change loan lock
    def loan_lock(self, account_number: int, loanLock: bool) -> None:
        usr: User = [u for u in self.accounts if u.account_number == account_number]
        usr[0].loanLock = loanLock

    # amount transfer
    def amount_transfer(
        self, my_account: str, transfer_account, transfer_amount: int
    ) -> None:
        usr: User = [u for u in self.accounts if u.account_number == my_account]
        trn_usr: User = [
            u for u in self.accounts if u.account_number == transfer_account
        ]
        if trn_usr:
            if usr[0].balance >= transfer_amount:
                trn_usr[0].balance += transfer_amount
                usr[0].balance -= transfer_amount

                ttf = f"received from acc no ={my_account}"
                gttf = f"transfer to acc no ={transfer_account}"

                # received history
                self.addTransaction_history(
                    transfer_account, trn_usr[0].name, transfer_amount, ttf, trn_usr[0]
                )

                # transfer history
                self.addTransaction_history(
                    my_account, usr[0].name, transfer_amount, gttf, usr[0]
                )

            else:
                print("Your have not enough amount to transfer")
        else:
            print("Account does not exist")

    # get current amount
    def current_balance(self, account_number: int) -> int:
        usr: User = [u for u in self.accounts if u.account_number == account_number]
        print(f"Current Balance = {usr[0].balance}")

    # add trnsaction history
    def addTransaction_history(
        self, account_number: str, name: str, amount: int, type: str, usrr: User
    ) -> None:
        usrr.transaction_history.append(
            f"Account number = {account_number}, name = { name}, and {type} amount = { amount}"
        )

    # show transaction history
    def show_transaction_history(self, account_number: str) -> None:
        usr: User = [u for u in self.accounts if u.account_number == account_number]
        print("\n--------------------- history ---------------------")
        if len(usr[0].transaction_history) > 0:
            for i in usr[0].transaction_history:
                print(i)
        else:
            print("There have no transaction history ---\n")

    # withdraw amount
    def withdraw_amount(self, account_number: str, amount: int) -> None:
        usr: User = [u for u in self.accounts if u.account_number == account_number]

        # bank draft check
        if self.bankDraft:
            print(f"the bank is bankrupt")
            return

        if amount > 0:
            if usr[0].balance < amount:
                print("Withdrawal amount exceeded")
            else:
                usr[0].balance -= amount
                print(
                    f"Withdraw successfull. Account Number = { usr[0].account_number}"
                )
                self.current_balance(account_number)
                # trasaction history
                self.addTransaction_history(
                    account_number, usr[0].name, amount, "withdraw", usr[0]
                )

        else:
            print("\namount must be greater than 0 \n")

    # deposit amount
    def deposit_amount(self, account_number: int, amount: int) -> None:
        usr: User = [u for u in self.accounts if u.account_number == account_number]

        # bank draft check
        if self.bankDraft:
            print(f"\nthe bank is bankrupt\n")
            return

        if amount > 0:
            usr[0].balance += amount
            print(f"\nDeposit successfull. Account Number = { usr[0].account_number}")
            print(f"your current balance = { usr[0].balance}\n")

            # trasaction history
            self.addTransaction_history(
                account_number, usr[0].name, amount, "Deposit", usr[0]
            )

    # get loan
    def getLoan(self, account_number: int, amount: int) -> None:
        usr: User = [u for u in self.accounts if u.account_number == account_number]
        if usr[0].loanCount < 2 and not usr[0].loanLock:
            usr[0].balance += amount
            usr[0].loanAmount += amount
            usr[0].loanCount += 1
            print("Your Load is granted")
            self.current_balance(account_number)

            # trasaction history
            self.addTransaction_history(
                account_number, usr[0].name, amount, "Loan", usr[0]
            )
        else:
            print(
                f"\n---------------------\nYour loan is not granted.\n------------------------------\n"
            )
