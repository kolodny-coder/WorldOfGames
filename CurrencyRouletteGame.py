import requests

from random import randint


class CurrencyRouletteGame:
    def __init__(self, level_of_difficulty):
        self.level_of_difficulty = level_of_difficulty

    def get_usd_ils_excahnge_rate(self):
        url = 'https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=04c733dc779b8b934b60'
        response = requests.get(url)
        return response.json()['USD_ILS']

    def get_money_interval(self, amt_dollar):
        difficulty = self.level_of_difficulty
        total_amount = amt_dollar * self.get_usd_ils_excahnge_rate()
        min_interval = total_amount - (5 - difficulty)
        max_interval = total_amount + (5 - difficulty)
        return min_interval, max_interval

    def generate_amount_of_dollars(self):
        return randint(1, 100)

    def get_guess_from_user(self, amt_dollar):
        return int(
            input(
                f'please Estimate what is the'
                f' value of {amt_dollar}$'
                f' in Shekels '
            )
        )

    def check_user_guess(self ,amt_dollar):
        user_input = self.get_guess_from_user(amt_dollar)
        min_value, max_value = self.get_money_interval(amt_dollar)
        if min_value <= user_input <= max_value :
            return 'You Won !!!'
        else:
            return 'Your estimation is out of scope'

    def play_currency_roulette_game(self):
        amt_dollar = self.generate_amount_of_dollars()
        return self.check_user_guess(amt_dollar)
