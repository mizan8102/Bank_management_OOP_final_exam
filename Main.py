from Bank import Bank
from User import User

if __name__ == "__main__":
    admin = User("mizan", "mizan@gmail.com", "charijania", "admin")

    bank = Bank(admin)
    bank.deposit_amount(9000)
    bank.withdraw_amount(1000)

    while True:
        n = int(input("Choice a option : "))
        if n == 1:
            amount = int(input("Enter amount : "))
            bank.getLoan(amount)

    print("--------------------- history ---------------------")
    for i in bank.transaction_history:
        print(i)
