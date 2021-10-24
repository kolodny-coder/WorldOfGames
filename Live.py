def welcome(name):
    print(f'Hello {name} and welcome to the  World of Games(WoG).\n'
          f'Here you can find many cool games to play.')


def load_game():
    while True:
        chosen_game = input('''Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to
        guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS ''')
        if chosen_game in ['1', '2', '3']:
            break
        print('please choose a number between 1 - 3')
        continue

    while True:
        level_of_difficulty = input('Please choose game difficulty from 1 to 5: ')
        if level_of_difficulty in ['1', '2', '3', '4', '5']:
            break
        print('please choose a number between 1 - 5')
        continue
    return int(chosen_game), int(level_of_difficulty)



