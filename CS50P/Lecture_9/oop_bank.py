class Account():
    def __init__(self) -> None:
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, n:int) -> None:
        self._balance = n


    def deposit(self, n:int) -> None:
        self._balance += n

    def withdraw(self, n:int) -> None:
        self._balance -= n


def main():
    account = Account()
    print(f"Balance: {account.balance}")
    #account.balance = 1000
    account.deposit(100)
    account.withdraw(50)
    print(f"Balance: {account.balance}")



if __name__ == "__main__":
    main()
