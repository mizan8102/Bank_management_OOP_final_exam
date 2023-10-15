from Admin import Admin
from Bank import Bank
from User import User

if __name__ == "__main__":
    admin = Admin("mizan", "mizan@gmail.com", "charijania", "current", "123456")

    while True:
        print(
            f"-------------------- Welcome To Bank Management System --------------------"
        )

        print("Are you Admin or User?\n1.Admin\n2.User")
        n: int = int(input("Choose a option: "))

        if n == 1:
            email = input("Enter email:")
            password = input("Enter password: ")
            if admin.auth(email, password):
                print(f"Login successfull . Welcome to Admin Panel")
                while True:
                    print(
                        "What do you want :\n1.Create account\n2.Delete account\n3.show All Users\n4.Check Total available balance\n5.Check the Total loan Amount\n6.Loan featur active/deactive "
                    )
                    choice: int = input(int("choose your option: "))
                    if choice == 1:
                        print("created Successfull")

            else:
                print("Credentials is not correct . Try again")

    # bank = Bank(admin)
    # bank.deposit_amount(9000)
    # bank.withdraw_amount(1000)

    # while True:
    #     n = int(input("Choice a option : "))
    #     if n == 1:
    #         amount = int(input("Enter amount : "))
    #         bank.getLoan(amount)

    # print("--------------------- history ---------------------")
    # for i in bank.transaction_history:
    #     print(i)
