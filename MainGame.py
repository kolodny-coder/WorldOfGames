from Live import load_game, welcome
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from WordOfGames.CurrencyRouletteGame import CurrencyRouletteGame
from WordOfGames.scores import add_score


def start_playing():
    print(welcome("Guy"))
    return load_game()


def run_memory_game():
    player1 = MemoryGame(level_of_difficulty)
    rv = player1.play_memory_game()
    print(rv)
    if rv == 'You Won !!!':
      add_score(level_of_difficulty)




def run_guess_game():
    player1 = GuessGame(level_of_difficulty)
    rv = player1.play()
    print(rv)
    if rv == 'You Won !!!':
        add_score(level_of_difficulty)



def run_currency_roulette_game():
    player1 = CurrencyRouletteGame(level_of_difficulty)
    print(player1.play_currency_roulette_game())


if __name__ == '__main__':
    chosen_game, level_of_difficulty = start_playing()
    dispatch = {
        1: run_memory_game,
        2: run_guess_game,
        3: run_currency_roulette_game,
    }
    dispatch[chosen_game]()
