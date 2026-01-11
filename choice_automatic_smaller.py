# File choice_automatic_smaller.py: The simulation of the player's choice
# between playing first with 1 or 2. For the automatic building and
# testing purposes - the grid dimensions are also drawn pseudorandomly
# from the range of integers, where integer ∈ <3, 6>.

from random import randint

from tictactoe import Check


class TheGame:
    """
    The game logic of the choice between starting with 1 or starting with 2.
    """

    # Let's instantiate a Check class.

    check: Check = Check()

    # The player behavior of the choice between 1 or 2 is simulated by the
    # pseudorandom drawing of 1 or 2.

    try:

        choice: int = randint(1, 2)
        print(f"Choice: {choice}")

    except ValueError:

        print("You had a ValueError. Try again.")
        choice = randint(1, 2)

    # The player is required to choose an integer. Otherwise the player is
    # informed that they hadn't chosen an instance of an integer and they are
    # prompted to choose another time.

    while not Check.check_if_choice_int(check, choice):
        print("Choose an integer !!!")
        choice = randint(1, 2)

    # If the player didn't chose an integer which is 0 or 1 they are informed
    # of it and prompted to choose once again.

    while not Check.check_if_choice_in_range(check, choice):
        print("Choose 1 or 2 !!! ")
        choice = randint(1, 2)

    # If 1 is drawn the game with the logic with starting 1 is imported,
    # instantiated and played.

    if choice == 1:

        from game_1_automatic_smaller import Game1First
        game = Game1First()
        game.play()

    # If 2 is drawn the game with the logic with starting 2 is imported,
    # instantiated and played.

    elif choice == 2:

        from game_2_automatic_smaller import Game2First
        game = Game2First()
        game.play()
