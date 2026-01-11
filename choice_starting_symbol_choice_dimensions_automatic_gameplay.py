# File choice_starting_symbol_choice_dimensions_automatic_gameplay.py: The
# choice logic of the gameplay with the choice of the starting
# symbol by the player and the choice of dimensions (also by the player).
# Run the game in: ... file.

from tictactoe import Check


class TheGame:
    """
    The game logic of the choice between starting with 1 or starting with 2.
    The player has a choice with which symbol to start with. The player has
    also the choice of the dimensions of the game's grid.
    """

    # Let's instantiate a Check class.

    check: Check = Check()

    # The player chooses with which symbol to play.

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

    # If the player hadn't chosen an integer which is 1 or 2, they are
    # informed of it and prompted to choose once again.

    while not Check.check_if_choice_in_range(check, choice):
        print("Choose 1 or 2 !!! ")
        choice: int = int(input("Do you want to play first with 1 (choose 1) or"
                                " with 2 (choose 2)? "))

    # If 1 is drawn the automatic gameplay with the logic with starting 1 is
    # imported, instantiated and played.

    if choice == 1:

        from game_1_automatic_choice_of_dimensions import Game1First
        game = Game1First()
        game.play()

    # If 2 is drawn the automatic gameplay with the logic with starting 2 is
    # imported, instantiated, and played.

    elif choice == 2:

        from game_2_automatic_choice_of_dimensions import Game2First
        game = Game2First()
        game.play()
