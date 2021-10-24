import random
import collections
import subprocess
from time import sleep
import sys


class MemoryGame:
    def __init__(self, level_of_difficulty):
        self.level_of_difficulty = level_of_difficulty

    def generate_sequence(self, length_of_sequence) -> list:
        generated_list = []
        for _ in range(length_of_sequence):
            num = random.randint(1, 101)
            generated_list.append(num)
        return generated_list

    def get_list_from_user(self, user_sequence) -> list:
        print('Please type the numbers you recall from previous display')
        user_list_of_numbers = []
        for _ in range(user_sequence):
            user_input = int(input('add a number and press ENTER '))
            user_list_of_numbers.append(user_input)
        return user_list_of_numbers

    def is_list_equal(self, list1, list2):
        if collections.Counter(list1) == collections.Counter(list2):
            return 'You Won !!!'
        else:
            return 'You didn\'t recall all the numbers correctly'

    def play_memory_game(self):
        random_generated_list = self.generate_sequence(self.level_of_difficulty)
        print(random_generated_list)
        sleep(0.7)
        if 'win' in sys.platform:
            subprocess.run('cls', shell=True)
        else:
            subprocess.run('clear', shell=True)

        user_remembered_numbers = self.get_list_from_user(self.level_of_difficulty)
        return self.is_list_equal(random_generated_list, user_remembered_numbers)

