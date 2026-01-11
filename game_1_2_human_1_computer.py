# File game_1_2_human_1_computer.py. : The game logic with starting
# 1 and the choice of dimensions, human plays with 2 against the
# computer - pseudorandomly.

from numpy.core._multiarray_umath import ndarray

from tictactoe import AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer


class Game1First:
    """
    The main game logic. With 1 playing first and human player playing with 2.
    """

    # Let's make available what was made beforehand and
    # instantiate an instance of the
    # AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer class.

    tic_tac_toe: object = AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer()

    # The counter variable set to 0.

    counter: int = 0

    def play(self):
        """
        The player chooses the numpy.ndarray's dimensions, and from that data
        the numpy.ndarray is constructed. The horizontal dimension is accessed
        by accessing the 0-th numpy.ndarray's shape parameter and saved as the
        matrix_dimension variable. The number of accessible cells is calculated
        by multiplying the matrix_dimension by itself and saved as the variable
        matrix_dimension_quadrupled. The loop uses the counter variable to direct
        the activity of the gameplay to the relevant blocks of the game.
        The even counter values direct the activity towards drawing in
        the coordinates for a new 1 - pseudorandomly - from the prepopulated list,
        while the uneven counter values - towards typing in the coordinates
        for a new 2. The values of the counter variable greater or equal than
        (matrix_dimension - 1) and smaller than matrix_dimension_quadrupled are
        directed towards the block with the checking of the game results.
        There, the numpy.ndarray is plugged into the methods: the
        vertical_and_horizontal_win method (the numpy.ndarray
        is checked for the possibility of the horizontal or vertical win),
        the diagonal_win method (the numpy.ndarray is checked for the
        possibility of the diagonal win) and the draw method (the
        numpy.ndarray is checked for the possibility of the draw). There, the
        game may resolve to 4 outcomes - 3 of them results in the printout of
        the game results and the termination of the game - depending on the
        counter values. If the counter values are uneven, then the player
        with 2 may win (when that's the case the phrase "2 wins! is printed and
        the game is terminated) or there may be a draw (then the "Draw." is
        printed and the game resolves). If the counter values are even then
        the player with 1 may win and there are 2 possible scenarios of the
        game resolution - "1 wins!" is printed and the game terminates when the
        response from the either of the methods - the vertical_and_horizontal_win
        and the diagonal_win - is True and the "Draw" is printed if the response
        from the method draw is True. If the responses from the methods are False
        - the game in the cases of both blocks continues.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :return: None. Example: None.
        :rtype: None
        """

        matrix_dimension: int = \
            AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer.construct_matrix(
                self.tic_tac_toe).shape[0]

        matrix_dimension_quadrupled: int = matrix_dimension * matrix_dimension

        while self.counter < (matrix_dimension_quadrupled - 1):

            while self.counter < (matrix_dimension - 1):

                if self.counter % 2 == 1:

                    matrix_2: ndarray = \
                        AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer. \
                        enter_the_coordinates_for_2_and_check_them(self.tic_tac_toe)

                    self.counter += 1

                elif self.counter % 2 == 0:

                    matrix_1: ndarray = \
                        AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer. \
                        enter_the_coordinates_for_1_and_check_them(self.tic_tac_toe)

                    self.counter += 1

            while (matrix_dimension - 1) <= self.counter < matrix_dimension_quadrupled:

                if self.counter % 2 == 1:

                    matrix_1: ndarray = \
                        AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer. \
                        enter_the_coordinates_for_2_and_check_them(self.tic_tac_toe)

                    response_1: bool = \
                        AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer. \
                        vertical_and_horizontal_win(self.tic_tac_toe, matrix_1)

                    response_2: bool = \
                        AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer.diagonal_win(
                            self.tic_tac_toe, matrix_1)

                    response_3: bool = \
                        AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer.draw(
                            self.tic_tac_toe, matrix_1)

                    if response_1:

                        print("2 wins!")
                        print("Game over.")
                        return

                    elif response_2:

                        print("2 wins!")
                        print("Game over.")
                        return

                    elif response_3:

                        print("Draw.")
                        print("Game over.")
                        return

                    elif (not response_2) and (not response_1) and (not response_3):

                        pass

                    self.counter += 1

                elif self.counter % 2 == 0:

                    matrix_2 = \
                        AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer. \
                        enter_the_coordinates_for_1_and_check_them(self.tic_tac_toe)

                    response_1 = \
                        AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer. \
                        vertical_and_horizontal_win(self.tic_tac_toe, matrix_2)

                    response_2 = \
                        AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer.diagonal_win(
                            self.tic_tac_toe, matrix_2)

                    response_3 = \
                        AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer.draw(
                            self.tic_tac_toe, matrix_2)

                    if response_1:

                        print("1 wins!")
                        print("Game over.")
                        return

                    elif response_2:

                        print("1 wins!")
                        print("Game over.")
                        return

                    elif response_3:

                        print("Draw.")
                        print("Game over.")
                        return

                    elif (not response_2) and (not response_1) and (not response_3):

                        pass

                    self.counter += 1
