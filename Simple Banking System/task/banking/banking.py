# Write your code here
import random


class Card:
    pin: str
    card_nm: str
    all_cards = []

    def __init__(self):
        self.acc_nm = str(random.randint(0, 999_999_999)).zfill(9)
        self.checksum = 0
        self.card_nm = f"400000{self.acc_nm}{self.checksum}"
        self.pin = str(random.randint(0, 9999)).zfill(4)
        self.balance = 0
        Card.all_cards.append(self)
        print("Your card has been created")
        print("Your card number:")
        print("{}".format(self.card_nm))
        print("Your card PIN:")
        print(self.pin)

    def print_ballance(self):
        print(f"Balance: {self.balance}")

    def check_credentials(self, entered_card_nm, enterd_pin):
        """
        :param entered_card_nm: введенный номер карты при входе в систему
        :param enterd_pin: введенный пин кодек
        :return: возвращает тру фолс на наличе параметров
        """
        if entered_card_nm == self.card_nm and enterd_pin == self.pin:
            print("You have successfully logged in!")
            return True
        else:
            print("Wrong card number or PIN!")
            return False


running: bool = True

while running:
    cursor = int(input("""
        1. Create an account
        2. Log into account
        0. Exit
    """))
    if cursor == 0:
        running = False

    elif cursor == 1:
        my_card = Card()
        continue

    elif cursor == 2:
        entered_card_nm = input("Enter your card number:")
        enterd_pin = input("Enter your PIN:")
        if my_card.check_credentials(entered_card_nm, enterd_pin):
            while True:
                coursor2 = int(input("""
                    1. Balance
                    2. Log out
                    0. Exit
                """))
                if coursor2 == 0:
                    running = False
                    break
                elif coursor2 == 1:
                    print(f"Balance: {my_card.balance}")
                elif coursor2 == 2:
                    print("You have successfully logged out!")
                    break
        else:
            print("Wrong card number or PIN!")
print("Bye!")
