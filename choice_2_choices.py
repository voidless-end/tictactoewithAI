# File choice_2_choices.py: The game logic of choice between starting with
# 1 or starting with 2 and being the first or the second player (playing
# with the computer).

from tictactoe import Check


class TheGame:
    """
    The game logic of choice between starting with 1 or starting with 2
    and being the first or the second player (playing with the computer).
    """

    # Let's instantiate a Check class.

    check: Check = Check()

    # The player is prompted to choose with which symbol they want to play.
    # Choose 1 to play with 1 first, choose 2 to play with 2 first.

    try:

        choice_1: int = int(input("Do you want to play with 1 (choose 1) or with "
                                  "2 (choose 2)? "))

    except ValueError:

        print("You had a ValueError. Try again.")
        choice_1 = int(input("Do you want to play with 1 (choose 0) or with "
                             "2 (choose 2)? "))

    # The player is required to choose an integer. Otherwise the player is
    # informed that they hadn't chosen an instance of an integer and they are
    # prompted to choose once again.

    while not Check.check_if_choice_int(check, choice_1):
        print("Choose an integer !!!")
        choice_1 = int(input("Do you want to play with 1 (choose 1) or with "
                             "2 (choose 2)? "))

    # If the player didn't chose an integer which is 1 or 2, they are informed
    # of it and prompted to choose once again.

    while not Check.check_if_choice_in_range(check, choice_1):
        print("Choose 1 or 2 !!!")
        choice_1 = int(input("Do you want to play with 1 (choose 1) or with "
                             "2 (choose 1)? "))

    # The player is prompted to choose if they want to play first or the
    # second against the computer.

    try:

        choice_2: int = int(input("Do you want to play first (choose 1) or "
                                  "the second (choose 2)? "))

    except ValueError:

        print("You had a ValueError. Try again.")
        choice_2 = int(input("Do you want to play first (choose 1) or "
                             "the second (choose 2)? "))

    # Player is required to choose an integer. Otherwise player is
    # informed that they hadn't chosen an instance of an integer and they are
    # prompted to choose once again.

    while not Check.check_if_choice_int(check, choice_2):
        print("Choose an integer !!!")
        choice_2 = int(input("Do you want to play first (choose 1) or "
                             " second (choose 2)? "))

    # If the player didn't chose an integer which is 1 or 2 they are informed
    # of it and prompted to choose once again.

    while not Check.check_if_choice_in_range(check, choice_2):
        print("Choose 1 or 2 !!! ")
        choice_2 = int(input("Do you want to play first (choose 1) or "
                             " second (choose 2)? "))

    # If 1 is chosen the game with the logic with starting 1 is imported,
    # instantiated, and played.

    if choice_1 == 1:

        # If 1 is chosen the game with the logic with the human playing first is
        # imported, instantiated, and played.

        # playing 1 and playing first

        if choice_2 == 1:

            from game_1_1_human_2_computer import Game1First
            game = Game1First()
            game.play()

        # If 2 is chosen the game with the logic with the human playing as the
        # second player is imported, instantiated, and played.

        # with 1 and playing second

        elif choice_2 == 2:

            from game_2_1_human_2_computer import Game2First
            game = Game2First()
            game.play()

    # If 2 is chosen the game with the logic with starting 2 is imported,
    # instantiated, and played.

    elif choice_1 == 2:

        # If 1 is chosen the game with the logic with the human playing first is
        # imported, instantiated, and played.

        # with 2 and first

        if choice_2 == 1:

            from game_2_2_human_1_computer import Game2First
            game = Game2First()
            game.play()

        # If 2 is chosen the game with the logic with the human playing as the
        # second player is imported, instantiated, and played.

        # with 2 and playing as the second player

        elif choice_2 == 2:

            from game_1_2_human_1_computer import Game1First
            game = Game1First()
            game.play()
