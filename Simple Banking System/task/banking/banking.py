import random


class Accounting:

    def __init__(self):
        self.cards: dict = dict()

    def log_in_menu(self) -> None:
        while True:
            print("1. Create an account\n2. Log into account\n0. Exit")
            cursor: str = input()
            if cursor == '1':
                self.create_account()
            elif cursor == '2':
                entered_card: str = input('Enter your card number:\n')
                entered_pin: str = input('Enter your PIN:\n')
                if self.cards[entered_card]['PIN'] == entered_pin:
                    print("You have successfully logged in!")
                    self.account(entered_card)
                else:
                    print("Wrong card number or PIN!")
            elif cursor == '0':
                print('Bye!')
                exit()
            else:
                print('Unknown option.')

    def account(self, card: str) -> None:
        while True:
            print("1. Balance\n2. Log out\n0. Exit")
            cursor = input()
            if cursor == '1':
                self.print_balance(card)
            elif cursor == '2':
                print("You have successfully logged out!")
                return
            elif cursor == '0':
                print('Bye!')
                exit()
            else:
                print('Unknown option.\n')

    def print_balance(self, card) -> None:
        print(f"Balance: {self.cards[card]['Balance']}")

    @staticmethod
    def generate_numbers():
        checksum: str = '0'
        card, pin = ('400000' + str(random.randint(0, 999_999_999)).zfill(9) + checksum,
                     str(random.randint(0, 9999)).zfill(4))
        return card, pin

    def create_account(self) -> None:
        card, pin = self.generate_numbers()
        self.cards[card] = {'PIN': pin, 'Balance': 0}
        print("Your card has been created")
        print("Your card number:")
        print(f"{card}")
        print("Your card PIN:")
        print(f"{pin}")


Accounting().log_in_menu()
