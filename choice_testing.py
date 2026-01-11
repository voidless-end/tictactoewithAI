# File choice_testing.py: The choice logic of the game, where the player
# can choose how many games they want to play and a starting symbol.
# The summary of the results is written to a text file and is printed
# at the end of the game.

import time
from typing import List, Any, Union, TextIO

from tictactoe import Check


class TheGame:
    """
    The game logic of choice between starting with "X" or starting with "O".
    """

    # Let's instantiate a Check class.

    check: Check = Check()

    try:

        # The player is asked for the number of games they want to
        # play.

        number_of_the_games: int = int(input("How many games do you want to play? > "))

    except ValueError:

        # If the player had a ValueError during typing of the number of
        # games they want to play, they are informed of it and asked for
        # the number of games once again.

        print("You a had ValueError. Try again.")
        number_of_the_games = int(input("How many games do you want to play? > "))

    # The player is required to choose an integer. Otherwise the player is
    # informed that they hadn't chosen an instance of an integer and they are
    # prompted to choose once again.

    while not Check.check_if_choice_int(check, number_of_the_games):
        print("Choose an integer !!!")
        number_of_the_games = int(input("How many games do you want to play? > "))

    # The player is prompted to choose with which symbol they want to play.
    # Choose 1 to play with 1 first, choose 2 to play with 2 first.

    try:

        choice: int = int(input("Do you want to play first with 1 (choose 1) or "
                                "with 2 (choose 2)? "))

    except ValueError:

        # If the player had a ValueError during choosing of
        # the symbol they want to play, they are informed of
        # it and asked for the number of games once again.

        print("You had a ValueError. Try again.")
        choice = int(input("Do you want to play first with 1 (choose 1) or "
                           "with 2 (choose 2)? "))

    # The player is required to choose an integer. Otherwise the player is
    # informed that they hadn't chosen an instance of an integer and they are
    # prompted to choose once again.

    while not Check.check_if_choice_int(check, choice):
        print("Choose an integer !!!")
        choice = int(input("Do you want to play first with 1 (choose 1) or "
                           "with 2 (choose 2)? "))

    # If the player didn't chose an integer which is 1 or 2 they are informed
    # of it and prompted to choose once again.

    while not Check.check_if_choice_in_range(check, choice):
        print("Choose 1 or 2 !!! ")
        choice = int(input("Do you want to play first with 1 (choose 1) or "
                           "with 2 (choose 2)? "))

    # If 1 is chosen the game with the logic with starting 1 is imported,
    # instantiated, and played the preselected number of times. The outcomes
    # of playing the number of games the player had chosen are summarized at
    # the end and written to a file.

    if choice == 1:

        from game_1_testing import Game1First
        game = Game1First()

        i: int

        for i in range(0, number_of_the_games):
            game.play()

        print("---------------------------------------")
        dimensions_of_the_matrix_string: str = f"Dimensions of the matrix:" \
                                               f" {game.choose_dimensions} x {game.choose_dimensions}."
        print(dimensions_of_the_matrix_string)
        symbol_first_string: str = "You have played with 1 first."
        print(symbol_first_string)
        number_of_games_played: int = game.wins_1 + game.wins_2 + game.draws
        percent_of_1_won: float = (game.wins_1 / number_of_games_played) * 100
        percent_of_2_won: float = (game.wins_2 / number_of_games_played) * 100
        percent_of_draws: float = (game.draws / number_of_games_played) * 100
        won_1_string: str = f"1 won {game.wins_1} times. " \
                            f"That is {round(percent_of_1_won, 3)} % of the time."
        print(won_1_string)
        won_2_string: str = f"2 won {game.wins_2} times. " \
                            f"That is {round(percent_of_2_won, 3)} % of the time."
        print(won_2_string)
        draws_string: str = f"There were {game.draws} draws. " \
                            f"That is {round(percent_of_draws, 3)} % of the time."
        print(draws_string)
        number_of_games_played_string: str = f"You have played " \
                                             f"{number_of_games_played} games."
        print(number_of_games_played_string)
        current_time: int = int(time.time())
        file_name: str = f"testing_1_game_{game.choose_dimensions}D_" \
                         f"{number_of_games_played}_{current_time}.txt"

        string_list: List[Union[str, Any]] = [dimensions_of_the_matrix_string, "\n",
                                              symbol_first_string, "\n",
                                              won_1_string, "\n",
                                              won_2_string, "\n",
                                              draws_string, "\n",
                                              number_of_games_played_string, "\n"]

        f: TextIO

        with open(file_name, "a+") as f:
            f.writelines(string_list)

    # If 1 is chosen the game with the logic with starting "O" is imported,
    # instantiated, and played the preselected number of times. The outcomes
    # of playing the number of games the player had chosen are summarized at
    # the end.

    elif choice == 2:

        from game_2_testing import Game2First
        game = Game2First()
        for i in range(number_of_the_games):
            game.play()

        print("-------------------------------------------")
        dimensions_of_the_matrix_string = f"Dimensions of the matrix:" \
                                          f" {game.choose_dimensions} x {game.choose_dimensions}."
        print(dimensions_of_the_matrix_string)
        symbol_first_string = "You have played with 2 first."
        print(symbol_first_string)

        number_of_games_played: int = game.wins_1 + game.wins_2 + game.draws
        percent_of_1_won: float = (game.wins_1 / number_of_games_played) * 100
        percent_of_2_won: float = (game.wins_2 / number_of_games_played) * 100
        percent_of_draws: float = (game.draws / number_of_games_played) * 100

        won_1_string = f"1 won {game.wins_1} times. " \
                       f"That is {round(percent_of_1_won, 3)} % of the time."
        print(won_1_string)
        won_2_string = f"2 won {game.wins_2} times. " \
                       f"That is {round(percent_of_2_won, 3)} % of the time."
        print(won_2_string)
        draws_string = f"There were {game.draws} draws. " \
                       f"That is {round(percent_of_draws, 3)} % of the time."
        print(draws_string)
        number_of_games_played_string = f"You have played " \
                                        f"{number_of_games_played} games."
        print(number_of_games_played_string)
        current_time = int(time.time())
        file_name = f"testing_2_game_{game.choose_dimensions}D_" \
                    f"{number_of_games_played}_{current_time}.txt"
        string_list = [dimensions_of_the_matrix_string, "\n",
                       symbol_first_string, "\n",
                       won_1_string, "\n",
                       won_2_string, "\n",
                       draws_string, "\n",
                       number_of_games_played_string, "\n"]

        with open(file_name, "a+") as f:
            f.writelines(string_list)
