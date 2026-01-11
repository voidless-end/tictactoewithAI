# File choice.py: The game logic of the choice between playing first with
# 1 or with 2.

from tictactoe import Check


class TheGame:
    """
    The game logic of the choice between starting with 1 or starting with 2.
    When the choice is made the customized game is imported.
    """

    # Let's instantiate a Check class.

    check: Check = Check()

    # The player is prompted to choose with which symbol they want to play.
    # Choose 1 to play with 1 first, choose 2 to play with 2 first.

    try:

        choice: int = int(input("Do you want to play first with 1 (choose 1) or"
                                " with 2 (choose 2)? "))

    except ValueError:

        print("You had a ValueError. Try again.")
        choice: int = int(input("Do you want to play first with 1 (choose 1) or"
                                " with 2 (choose 2)? "))

    # The player is required to choose an integer. Otherwise the player is
    # informed that they hadn't chosen an instance of an integer and they are
    # prompted to choose once again.

    while not Check.check_if_choice_int(check, choice):
        print("Choose an integer !!!")
        choice: int = int(input("Do you want to play first with 1 (choose 1) or"
                                " with 2 (choose 2)? "))

    # If the player didn't chose an integer that is 1 or 2 they are informed
    # of it and prompted to choose once again.

    while not Check.check_if_choice_in_range(check, choice):
        print("Choose 1 or 2 !!! ")
        choice: int = int(input("Do you want to play first with 1 (choose 1) or"
                                " with 2 (choose 2)? "))

    # If 1 is chosen the game with the logic with starting 1 is imported,
    # instantiated and played.

    if choice == 1:

        from game_1_first import Game1First
        game = Game1First()
        game.play()

    # If 2 is chosen the game with the logic with starting 2 is imported,
    # instantiated, and played.

    elif choice == 2:

        from game_2_first import Game2First
        game = Game2First()
        game.play()
