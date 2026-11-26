class BankAccount:
    def __init__(self, holderName, accountNum, balance):
        self.customer = holderName
        self.num = accountNum
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        try:
            value = float(value)

            if value >= 0:
                self.__balance = value
            else:
                print("Saldo ei voi olla negatiivinen!")

        except ValueError:
            print("Syötä vain numeroita!")
    def __eq__(self, other):
        return self.__balance > other.__balance


def main():
    accounts = [        
        BankAccount(
            "Petteri",
            "FI92 8987 9847 9873 90",
            500
        ),
        BankAccount(
            "Saima",
            "FI03 4495 0483 2938 80",
            10520
        ),
        BankAccount(
            "Mira",
            "FI60 4938 2940 5968 45",
            1264
        ),
        BankAccount(
            "Matti",
            "FI90 3456 1245 8295 45",
            67
        ),
        BankAccount(
            "Marjatta",
            "FI34 9384 2748 9824 56",
            0
        )]

    while True:
        print()
        print(f"{accounts[0].customer}")
        print(f"Tili: {accounts[0].num}")
        print(f"Saldo: {accounts[0].balance:.2f} €")

        command = int(input(
            "\n1. Nosta rahaa"
            "\n2. Talleta rahaa"
            "\n3. Poistu"
            "\n4. Vertaile GDPR:n vastaisesti"
            "\nValinta: "
        ))

        match command:
            case 1:
                amount = float(input("Nostettava summa: "))

                if amount <= accounts[0].balance:
                    accounts[0].balance -= amount
                else:
                    print("Tilillä ei ole tarpeeksi rahaa.")

            case 2:
                amount = float(input("Talletettava summa: "))

                if amount > 0:
                    accounts[0].balance += amount
                else:
                    print("Virheellinen summa.")

            case 3:
                break

            case 4:
                s1 = accounts[0].balance
                s2 = accounts[1].balance
                print(s1>s2)
                sorted_accounts = sorted(accounts, key=lambda s: s.balance)
                for account in sorted_accounts:
                    print(account.customer)

            case _:
                print("Virheellinen valinta.")


if __name__ == "__main__":
    main()