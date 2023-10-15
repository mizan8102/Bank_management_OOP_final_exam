from Admin import Admin
from Bank import Bank
from User import User


# user validation check
def isValidAccount(account_number: int, bank: Bank) -> bool:
    usr: User = [u for u in bank.accounts if u.account_number == account_number]
    if usr:
        print(f"Hi {usr[0].name} ! ")
        return True
    else:
        print(f"Your account number is wrong")
        return False


# main
if __name__ == "__main__":
    admin = Admin("Admin", "admin@gmail.com", "Dhaka", "current", "123456")
    bank = Bank()

    while True:
        print("Are you Admin or User?\n1.Admin\n2.User\n3.Exit")
        n: int = int(input("Choose a option: "))

        # admin panel
        if n == 1:
            email = input("Enter email:")
            password = input("Enter password: ")
            # auth check
            if admin.auth(email, password):
                print(
                    f"Login successfull \n--------------------- Welcome to Admin Panel-------------------------"
                )
                while True:
                    print(
                        "What do you want :\n1.Create account\n2.Delete account\n3.show All Users\n4.Check Total available balance\n5.Check the Total loan Amount\n6.Loan featur active/deactive\n7.Bank Draft Enable or Disable\n8.Log out "
                    )
                    try:
                        choice: int = int(input("choose your option: "))
                    except Exception as e:
                        print("\nChoose right option\n")

                    if choice == 1:
                        name: str = input("Enter name :")
                        email: str = input("Enter email:")
                        address: str = input("Enter address: ")
                        account_selection: int = int(
                            input("Account Type:\n1.Savings\n2.Curent\nSelect one:")
                        )
                        account_type: str = (
                            "Savings" if account_selection == 1 else "Current"
                        )

                        # user create

                        user = User(name, email, address, account_type)
                        bank.create_account(user)

                    # user delete
                    elif choice == 2:
                        del_acc_num: str = input("Enter deleted account number : ")
                        bank.delete_account(del_acc_num)
                    elif choice == 3:
                        # all usr show
                        bank.all_user()

                    # show available amount
                    elif choice == 4:
                        print(
                            f"Total Available Amount = {bank.availableAmountOfBank()} \n"
                        )
                    # show total loan amount
                    elif choice == 5:
                        print(f"Total Loan Amount = {bank.total_loan_amount()} \n")

                    # Loan Feature
                    elif choice == 6:
                        accNum: str = input(
                            "Enter account number for active or deactive loan feature:"
                        )
                        op: int = int(input("Enter option :\n1.Active\n2.De-active\n"))
                        status: bool = False if op == 1 else True
                        bank.loan_lock(accNum, status)

                    # bank Draft
                    elif choice == 7:
                        op: int = int(input("Enter option :\n1.Active\n2.De-active\n"))
                        status: bool = True if op == 1 else False
                        bank.setBankDraft(status)

                    elif choice == 8:
                        break

            else:
                print(
                    "----------------------------\nCredentials is not correct . Try again\n-----------------\n"
                )

        # user panel
        elif n == 2:
            accNum: str = input("Enter your account number:")
            # account validation check
            if isValidAccount(accNum, bank):
                print(
                    f"\n--------------------- Welcome to User Panel-------------------------"
                )
                while True:
                    print(
                        "What do you want :\n1.Check available balance\n2.Transaction History\n3.Take Loan \n4.Transfer Amount\n5.Deposit Amount\n6.Withdraw Amount\n7.Log out from user panel"
                    )
                    try:
                        choice: int = int(input("choose your option: "))
                    except Exception as e:
                        print("\nChoose right option\n")

                    if choice == 1:
                        bank.current_balance(accNum)
                    elif choice == 2:
                        bank.show_transaction_history(accNum)

                    elif choice == 3:
                        amt: int = int(input("Enter loan amount: "))
                        bank.getLoan(accNum, amt)

                    elif choice == 4:
                        trnsAcc: str = input("Enter transfer Account Number: ")
                        amt: int = int(input("Enter transfer amount: "))
                        bank.amount_transfer(accNum, trnsAcc, amt)

                    elif choice == 5:
                        amt: int = int(input("Enter Deposit amount: "))
                        bank.deposit_amount(accNum, amt)

                    elif choice == 6:
                        amt: int = int(input("Enter Withdraw amount: "))
                        bank.withdraw_amount(accNum, amt)

                    elif choice == 7:
                        break

        # Exit
        elif n == 3:
            break
