from random import sample


class BankingSystem:
    def __init__(self):
        self.cards: dict = dict()

    def menu(self) -> None:
        while True:
            print("1. Create an account\n2. Log into account\n0. Exit")
            choice: str = input()
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.login()
            elif choice == '0':
                print('Bye!')
                exit()
            else:
                print('Unknown option.')

    def account(self, card: str) -> None:
        while True:
            print('1. Balance\n2. Log out\n0. Exit')
            choice = input()
            if choice == '1':
                print(f"\nBalance: {self.cards[card]['Balance']}\n")
            elif choice == '2':
                print('You have successfully logged out!\n')
                return
            elif choice == '0':
                print('Bye!')
                exit()
            else:
                print('Unknown option.\n')

    def login(self) -> None:
        card: str = input('Enter your card number:\n')
        PIN: str = input('Enter your PIN:\n')
        try:
            if self.cards[card]['PIN'] == PIN:
                print('You have successfully logged in!\n')
                self.account(card)
            else:
                print('Wrong card number or PIN\n')
        except KeyError:
            print('Wrong card number or PIN\n')

    @staticmethod
    def generate_numbers() -> tuple:
        while True:
            random_card = '400000' + ''.join([str(n) for n in sample(range(9), 9)]) + '7'
            random_PIN = ''.join([str(n) for n in sample(range(9), 4)])
            yield random_card, random_PIN

    def create_account(self) -> None:
        card, PIN = next(self.generate_numbers())
        self.cards[card] = {'PIN': PIN, 'Balance': 0}
        print('\nYour card has been created')
        print(f'Your card number:\n{card}')
        print(f'Your card PIN:\n{PIN}\n')


BankingSystem().menu()