from User import User


class Admin(User):
    def __init__(self, name, email, address, account_type, password) -> None:
        super().__init__(name, email, address, account_type)
        self.__password = password

    def getPassword(self):
        return self.__password

    def auth(self, email: str, password: str) -> bool:
        if self.email == email and self.__password == password:
            return True
        else:
            return False
