from pypal import Pypal


def bank():
    a = Pypal("Angela",  money=2000, withdraw_limit=1000)
    a.withdraw(1500)
    a.set_limit(1500)
    a_amount = a.get_amount()
    print(a_amount)
    a.withdraw(700)
    a.withdraw(3000)


if __name__ == "__main__":
    bank()