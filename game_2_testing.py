# File game_2_testing.py: Game with starting 2 and the dimensions of
# the matrix which you can choose there.

from tictactoe import AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100

from numpy.core._multiarray_umath import ndarray


class Game2First:
    """
    The main game logic. With 2 playing first.
    """

    # The variables for accumulating points are instantiated.

    wins_2: int = 0
    wins_1: int = 0
    draws: int = 0

    choose_dimensions: int = int(input("Choose the dimensions of the matrix: > "))

    def play(self):
        """
        The matrix (the game's grid, a numpy.ndarray) is constructed by
        pseudorandomly choosing its dimensions (where dimension  ∈ <3, 100>, and
        both are equal) by the construct_matrix method. The horizontal dimension
        is accessed by accessing the 0-th numpy.ndarray's shape parameter and
        saved as the matrix_dimension variable. The number of accessible cells
        is calculated by multiplying the matrix_dimension by itself and saved as
        the variable matrix_dimension_quadrupled. The loop uses the counter
        variable to direct the activity of the gameplay to the relevant blocks of
        the game. The even counter values direct the activity towards typing in
        the new 2, while the uneven counter values - towards typing in the new 1.
        The values of the counter variable greater or equal than
        (matrix_dimension - 1) and smaller than matrix_dimension_quadrupled
        are directed towards the block with the checking of the game results.
        There, the numpy.ndarray is plugged into the methods:
        the vertical_and_horizontal_win method (the numpy.ndarray is checked for
        the possibility of the horizontal or vertical win), the
        diagonal_win method (the numpy.ndarray is checked for the possibility of
        the diagonal win) and the draw method (the numpy.ndarray is checked for
        the possibility of the draw). There, the game may resolve to 4 outcomes
        - 3 of them results in the printout of the game results and the
        termination of the game - depending on the counter values. If the counter
        values are uneven, then the player with 1 may win (when that's the case
        the phrase "1 wins! is printed and the game is terminated), or there may
        be a draw (then the "Draw." is printed and the game resolves). If the
        counter values are even then the player with 2 may win and there are 2
        possible scenarios of the game resolution - "2 wins!" is printed and the
        game terminates when the response from the either of the methods - the
        vertical_and_horizontal_win and the diagonal_win - is True and the
        "Draw" is printed if the response from the method draw is True.
        If the responses from the methods are False - the game in the cases of
        both blocks continues.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :return: None. Example: None.
        :rtype: None
        """
        tic_tac_toe: object = AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100(
            self.choose_dimensions)

        counter: int = 0

        matrix_dimension: int = \
            AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100.construct_matrix(
                tic_tac_toe).shape[0]

        matrix_dimension_quadrupled: int = matrix_dimension * matrix_dimension

        while counter < (matrix_dimension_quadrupled - 1):

            while counter < (matrix_dimension - 1):

                if counter % 2 == 1:

                    matrix_1: ndarray = \
                        AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100 \
                        .enter_the_coordinates_for_1_and_check_them(tic_tac_toe)

                    counter += 1

                elif counter % 2 == 0:

                    matrix_2: ndarray = \
                        AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100 \
                        .enter_the_coordinates_for_2_and_check_them(tic_tac_toe)

                    counter += 1

            while (matrix_dimension - 1) <= counter < matrix_dimension_quadrupled:

                if counter % 2 == 1:

                    matrix_1: ndarray = \
                        AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100 \
                        .enter_the_coordinates_for_1_and_check_them(tic_tac_toe)

                    response_1: bool = AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100 \
                        .vertical_and_horizontal_win(tic_tac_toe, matrix_1)

                    response_2: bool = \
                        AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100.diagonal_win(
                            tic_tac_toe, matrix_1)

                    response_3: bool = \
                        AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100.draw(
                            tic_tac_toe, matrix_1)

                    if response_1:

                        print("1 wins!")
                        print("Game over.")
                        self.wins_1 += 1
                        return

                    elif response_2:

                        print("1 wins!")
                        print("Game over.")
                        self.wins_1 += 1
                        return

                    elif response_3:

                        print("Draw.")
                        print("Game over.")
                        self.draws += 1
                        return

                    elif (not response_2) and (not response_1) and (not response_3):

                        pass

                    counter += 1

                elif counter % 2 == 0:

                    matrix_2: ndarray = \
                        AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100 \
                        .enter_the_coordinates_for_2_and_check_them(tic_tac_toe)

                    response_1: bool = AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100 \
                        .vertical_and_horizontal_win(tic_tac_toe, matrix_2)

                    response_2: bool = \
                        AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100.diagonal_win(
                            tic_tac_toe, matrix_2)

                    response_3: bool = \
                        AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100.draw(
                            tic_tac_toe, matrix_2)

                    if response_1:

                        print("2 wins!")
                        print("Game over.")
                        self.wins_2 += 1
                        return

                    elif response_2:

                        print("2 wins!")
                        print("Game over.")
                        self.wins_2 += 1
                        return

                    elif response_3:

                        print("Draw.")
                        print("Game over.")
                        self.draws += 1
                        return

                    elif (not response_2) and (not response_1) and (not response_3):

                        pass

                    counter += 1
