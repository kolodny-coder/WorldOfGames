import random


class GuessGame():
    def __init__(self, level_of_difficulty):
        self.level_of_difficulty = level_of_difficulty

    def generate_number(self):
        return random.randint(1, self.level_of_difficulty)

    def get_guess_from_user(self):
        while True:
            user_number = int(input(
                f'\n\nWelcome to The Guess Guess Game\nPlease choose a number between 1 to {self.level_of_difficulty} '))
            if 1 <= user_number <= self.level_of_difficulty:
                return user_number
            print('you choose a number out of scope Please Try again')
            continue

    def compare_results(self):
        if self.generate_number() == self.get_guess_from_user():
            return 'You Won !!!'
        else:
            return 'You didn\'t guess correctly better luck next time'

    def play(self):
        return self.compare_results()
