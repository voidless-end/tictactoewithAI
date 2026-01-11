# File choice_2_choices_automatic_build.py: The automatic gameplay to
# simulate the choice between 1 and 2 and to simulate the choice between
# playing first or the second for the automatic building and testing
# purposes.

from random import randint

from tictactoe import Check


class TheGame:
    """
    The game logic of choice between starting with 1 or starting with 2
    and being the first or the second player (playing with the computer).
    There the choice is simulated.
    """

    # Let's instantiate a Check class.

    check: Check = Check()

    # The player is prompted to choose with which symbol they want to play.
    # Choose 1 to play with 1 first, choose 2 to play with 2 first.
    # There, this behaviour is simulated by the pseudorandom drawing of 1 or
    # 2.

    choice_1: int = randint(1, 2)

    # The player is required to choose an integer. Otherwise the player is
    # informed that they hadn't chosen an instance of an integer and they are
    # prompted to choose once again.

    while not Check.check_if_choice_int(check, choice_1):
        print("Choose an integer !!!")
        choice_1 = randint(1, 2)

    # If the player didn't choose an integer which is 1 or 2 they are informed
    # of it and prompted to choose once again.

    while not Check.check_if_choice_in_range(check, choice_1):
        print("Choose 1 or 2 !!! ")
        choice_1 = randint(1, 2)

    # The player is prompted to choose if they want to play first or the
    # second against the computer. There, this behaviour is simulated by the
    # pseudorandom drawing of 1 or 2.

    choice_2: int = randint(1, 2)

    # The player is required to choose an integer. Otherwise the player is
    # informed that they hadn't chosen an instance of an integer and they are
    # prompted to choose once again.

    while not Check.check_if_choice_int(check, choice_2):
        print("Choose an integer !!!")
        choice_2 = randint(1, 2)

    # If the player didn't choose an integer which is 1 or 2 they are informed
    # of it and prompted to choose once again.

    while not Check.check_if_choice_in_range(check, choice_2):
        print("Choose 1 or 2 !!! ")
        choice_2 = randint(1, 2)

    # If 1 is chosen the game with the logic with starting 1 is imported,
    # instantiated and played. There this behaviour is simulated.

    if choice_1 == 1:

        # If 1 is chosen the game with the logic with the human playing first is
        # imported, instantiated and played. There this behaviour is simulated.

        # with playing 1 and first

        if choice_2 == 1:

            print(f"Choice 1: {choice_1}")
            print(f"Choice 2: {choice_2}")

            from game_1_automatic import Game1First
            game = Game1First()
            game.play()

        # If 2 is chosen the game with the logic with the human playing as the
        # second player is imported, instantiated and played. There this
        # behaviour is simulated.

        # with 2 playing first

        elif choice_2 == 2:

            print(f"Choice 1: {choice_1}")
            print(f"Choice 2: {choice_2}")

            from game_2_automatic import Game2First
            game = Game2First()
            game.play()

    # If 2 is chosen the game with the logic with starting 2 is imported,
    # instantiated and played. There this behaviour is simulated.

    elif choice_1 == 2:

        # If 1 is chosen the game with the logic with the human playing first is
        # imported, instantiated, and played. There this behaviour is simulated.

        # with 1 playing first

        if choice_2 == 1:

            print(f"Choice 1: {choice_1}")
            print(f"Choice 2: {choice_2}")

            from game_1_automatic import Game1First
            game = Game1First()
            game.play()

        # If 2 is chosen the game with the logic with the human playing as the
        # second player is imported, instantiated and played. There, this
        # behaviour is simulated.

        # with 2 playing first

        elif choice_2 == 2:

            print(f"Choice 1: {choice_1}")
            print(f"Choice 2: {choice_2}")

            from game_2_automatic import Game2First
            game = Game2First()
            game.play()
