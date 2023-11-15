WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    def __init__(self, name, money=MONEY, withdraw_limit=WITHDRAW_LIMIT):
        self.__n = name
        self.__m = money
        self.__w = withdraw_limit

    def withdraw(self, amount):
        if amount > self.__w:
            print("Exceeds limit.")
        elif amount < self.__m:
            print("Error")
        else:
            self.__m -= amount
            print(f"{self.__n} remains {self.__m}")

    def set_limit(self, new_limit):
        self.__w = new_limit

    def get_amount(self):
        return self.__m

    def __str__(self):
        return f"name: {self.__n} / money: {self.__m} / limit: {self.__w}"

def main():
    angelala = Pypal("Angela", 100, 700)
    print(angelala)

if __name__ == "__main__":
    main()

if __name__ == "pypal":
    print("This pypal class simulates an online bank account.")

