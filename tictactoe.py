# File: tictactoe.py: The non-classical 2-player console gameplay of
# the tic-tac-toe with the dimensions which you can choose. Play
# with 1 and 2. File contains the main game logic divided game logic and
# the derived subclasses for the customized, automatic gameplay.

import numpy as np
from typing import Tuple, List, Dict, Any
from random import randint

from numpy.core._multiarray_umath import ndarray


class AdjacencyMatrixTicTacToe:
    """
    The tic-tac-toe gameplay with the dimensions of the grid which you can
    choose. Play with 1 and 2. The class contains the main game logic divided
    into the methods. Inspired by the adjacency matrix creation.
    """

    edges: List[Tuple[int, int]]
    coordinates_matrix: Dict[Any, Any]
    matrix: ndarray

    def __init__(self) -> None:
        """
        Instantiates the self.matrix as an empty 2-dimensional
        numpy.ndarray. Instantiates the self.coordinates_matrix as an empty
        dictionary. Instantiates self.edges as an empty list.
        """

        self.matrix = np.array([])
        self.coordinates_matrix = dict()
        self.edges = []

    def construct_matrix(self) -> ndarray:
        """
        The method asks the player for the dimensions of the ndarray (therefore
        the dimensions of the tic-tac-toe grid) in a form an integer number.
        If the ValueError has taken place (the player hasn't typed in the integer
        with the base 10), the player is informed of the mistake and asked for
        the dimensions of the grid (matrix, numpy.ndarray) again. The
        chosen dimensions are plugged into the display_coordinates method, where
        the list of the coordinates is constructed. Then, that list
        is plugged into the display_coordinates_matrix method where it is
        converted into a view of the accessible coordinates in a form of the
        coordinates' matrix and printed at the beginning of the game. In the next
        step, an empty matrix in the form of numpy.ndarray of the chosen
        dimensions composed of zeros is created and plugged into the
        display_matrix method where it is converted and printed out in the neat
        format (without the numpy's brackets). The so-called matrix
        (the game's grid) is also constructed in a way which was borrowed from the
        method previously employed in the adding of the vertices to the adjacency
        matrix. That's a more complicated way of constructing an adjacency matrix
        composed of zeros than just creating the numpy.ndarray with the method
        numpy.zeros((dimensions_of_the_matrix, dimensions_of_the_matrix),
        dtype=int). For the dimension in range from 0 to the
        (dimensions_of_matrix - 1), if dimension == 0, the numpy.ndarray array [[0]]
        is created, for the greater values of dimensions the matrix is
        updated with the column of zeros and then with the new row of zeros adjusted
        to the new length of the matrix. The matrix (or matrix,
        or the game's grid) is returned after construction.

        :param self: An instance of the class.
        :type self: An instance of the class
        :returns: A numpy.ndarray with the chosen dimensions (the game's grid)
        composed of zeros. Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
        :rtype: numpy.ndarray
        """

        try:

            dimensions_of_matrix: int = int(input("Choose the dimensions of the matrix: "))

            self.display_coordinates_matrix(self.display_coordinates(dimensions_of_matrix))

            empty_matrix: ndarray = np.zeros((dimensions_of_matrix, dimensions_of_matrix),
                                             dtype=int)

            self.display_matrix(empty_matrix)

            dimension: int

            for dimension in range(0, dimensions_of_matrix):

                if dimension == 0:

                    self.matrix = np.zeros((1,), dtype=int)

                else:

                    add_row: ndarray = np.zeros((dimension + 1,), dtype=int)
                    add_column: ndarray = np.zeros((dimension,), dtype=int)
                    self.matrix = np.c_[self.matrix, add_column]
                    self.matrix = np.r_[self.matrix, [add_row]]

            return self.matrix

        except ValueError:

            print("You had ValueError. Enter the integer with the base 10.")

            dimensions_of_matrix = int(input("Choose the dimensions of the matrix: "))

            self.display_coordinates_matrix(self.display_coordinates(dimensions_of_matrix))

            empty_matrix = np.zeros((dimensions_of_matrix, dimensions_of_matrix),
                                    dtype=int)

            self.display_matrix(empty_matrix)

            for dimension in range(0, dimensions_of_matrix):

                if dimension == 0:

                    self.matrix = np.zeros((1,), dtype=int)

                else:

                    add_row = np.zeros((dimension + 1,), dtype=int)
                    add_column = np.zeros((dimension,), dtype=int)
                    self.matrix = np.c_[self.matrix, add_column]
                    self.matrix = np.r_[self.matrix, [add_row]]

            return self.matrix

    def construct_adjacency_matrix(self, number_of_vertices: int) -> ndarray:
        """
        The original method that allows for the construction of the adjacency
        matrix. Takes in the number of vertices from which the adjacency matrix
        is to be composed and returns the adjacency matrix composed of zeros
        with the number of vertices passed into the method (number_of_vertices).

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param number_of_vertices: The number of vertices. From that information
        the initial adjacency matrix (composed of zeros) will be created.
        Example: 3.
        :type number_of_vertices: int
        :returns: The initial adjacency matrix (composed of zeros) with the number
        of vertices passed into the method.
        Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
        :rtype: numpy.ndarray
        """
        vertex: int

        for vertex in range(0, number_of_vertices + 1):

            if vertex == 0:

                self.matrix = np.zeros((1,), dtype=int)

            else:

                add_row: ndarray = np.zeros((vertex + 1,), dtype=int)
                add_column: ndarray = np.zeros((vertex,), dtype=int)
                self.matrix = np.c_[self.matrix, add_column]
                self.matrix = np.r_[self.matrix, [add_row]]

        return self.matrix

    def diagonal_win(self, new_matrix_1: ndarray) -> bool:
        """
        Evaluates the passed-in numpy.ndarray (the matrix numpy.ndarray) for
        the possibility of the diagonal win. In the event of the diagonal win
        constitution of the passed-in numpy.ndarray - returns True. Otherwise
        - returns False.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param new_matrix_1: A numpy.ndarray passed in for the evaluation of the
        possibility of the diagonal win constitution.
        Example: [[2, 1, 0], [2, 0, 1], [0, 0, 1]].
        :type new_matrix_1: numpy.ndarray
        :returns: True, if the passed-in numpy.ndarray has the constitution of the
        diagonal win. Otherwise - returns False. Example: True.
        :rtype: bool
        """

        # The three empty lists are initialized every time the new numpy.ndarray
        # is passed in.

        diagonal_win_1_coordinates_list: List[Tuple[int, int]] = []
        diagonal_win_1_boolean_list: List[bool] = []
        diagonal_win_2_boolean_list: List[bool] = []

        # The horizontal dimension is extracted from the numpy.ndarray's shape
        # property.

        len_matrix: int = new_matrix_1.shape[0]

        # The diagonal_win_1_coordinates_list is populated with the constellation of
        # the coordinates which, when their values are equal to 1 or to 2 and
        # equal to one another in the diagonal axis, are the 1st diagonal winning
        # set of the coordinates out of 2 possible.

        i: int

        for i in range(0, len_matrix):

            j: int = len_matrix - i - 1
            diagonal_win_1_coordinates_list.append((i, j))

        # For the range of the diagonal coordinates, if the 2 consecutive
        # values from the 2 consecutive diagonal coordinates pairs in the
        # passed-in numpy.ndarray are equal and different from 0, the boolean
        # True is appended to the diagonal_win_1_boolean_list.
        # If the same consecutive diagonal coordinates' values with the
        # corresponding 2 consecutive diagonal coordinates pairs in the
        # numpy.ndarray are different from each other, the False is appended
        # to the diagonal_win_1_boolean_list list.

        win_coordinates: int

        for win_coordinates in range(len(diagonal_win_1_coordinates_list) - 1):

            if new_matrix_1[diagonal_win_1_coordinates_list[win_coordinates]] \
                    == new_matrix_1[diagonal_win_1_coordinates_list[win_coordinates + 1]] != 0:

                diagonal_win_1_boolean_list.append(True)

            elif new_matrix_1[diagonal_win_1_coordinates_list[win_coordinates]] \
                    != new_matrix_1[diagonal_win_1_coordinates_list[win_coordinates + 1]]:

                diagonal_win_1_boolean_list.append(False)

        # The second possible diagonal constitution of the consecutive coordinates
        # is easier to extract, so there's no prepopulated list with the
        # coordinates to check. The coordinates in this constitution have the
        # pattern (i, i), where i is an integer ∈ <0, (len_matrix - 1)>. When
        # the two consecutive values of the numpy.ndarray with the diagonal
        # coordinates (i, i) and (i + 1, i + 1) are equal and different from 0,
        # the boolean True is appended to the diagonal_win_2_boolean_list list.
        # If the same pair of values are different from each other, the boolean
        # False is appended to the diagonal_win_2_boolean_list list.

        for i in range(0, len_matrix - 1):

            if new_matrix_1[(i, i)] == new_matrix_1[(i + 1, i + 1)] != 0:

                diagonal_win_2_boolean_list.append(True)

            elif new_matrix_1[(i, i)] != new_matrix_1[(i + 1, i + 1)]:

                diagonal_win_2_boolean_list.append(False)

        # The truthy_list is instantiated as an empty list.

        truthy_list: List[bool] = []

        # If the diagonal_win_1_boolean_list list is not empty (therefore
        # it evaluates to boolean True), the aforementioned list
        # is checked if the boolean False is in it. If False is in
        # diagonal_win_1_boolean_list list, the boolean False is appended
        # to the truthy_list. If False is not in diagonal_win_1_boolean_list list,
        # the boolean True is appended to the truthy_list. If
        # diagonal_win_1_boolean_list list is empty (therefore it
        # evaluates to the boolean False), the boolean False is appended to the
        # the truthy_list. The same type of checking with is performed with
        # the diagonal_win_2_boolean_list list.

        if diagonal_win_1_boolean_list:

            if False in diagonal_win_1_boolean_list:
                truthy_list.append(False)

            if False not in diagonal_win_1_boolean_list:
                truthy_list.append(True)

        truthy_list.append(False)

        if diagonal_win_2_boolean_list:

            if False in diagonal_win_2_boolean_list:
                truthy_list.append(False)

            if False not in diagonal_win_2_boolean_list:
                truthy_list.append(True)

        truthy_list.append(False)

        # If True is in truthy_list the boolean True is returned.
        # if that's not the case - the boolean False is returned.

        return any(truthy_list)

    def vertical_and_horizontal_win(self, new_matrix_1: ndarray) -> bool:
        """
        Evaluates the passed-in numpy.ndarray (the matrix numpy.ndarray) for
        the possibility of the vertical or horizontal win constitution of the cells.
        In the event of the horizontal or vertical win constitution of the
        passed-in numpy.ndarray - the True is returned. Otherwise - the False is
        returned.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param new_matrix_1: The numpy.ndarray passed in for evaluation.
         Example: [[2, 1, 0], [0, 1, 2], [0, 1, 1]].
        :type new_matrix_1: numpy.ndarray.
        :returns: True if the horizontal or vertical "win constitution" is
         detected. Otherwise it returns False. Example: False.
        :rtype: bool
        """

        # The horizontal_boolean_dict and the vertical_boolean_dict are
        # initialized as the empty dictionaries.

        horizontal_boolean_dict: Dict[str, List[bool]] = dict()
        vertical_boolean_dict: Dict[str, List[bool]] = dict()

        # The horizontal dimension of the numpy.ndarray (the one of the
        # numpy.ndarray's equal dimensions) is extracted by accessing the 0th
        # item of the numpy.ndarray's shape property.

        len_matrix: int = self.matrix.shape[0]

        # For the range of numbers ∈ <0, (len_matrix - 1)> (the vertical or the
        # horizontal indices of the matrix or the game's grid), the
        # horizontal_boolean_dict is populated by the empty lists with the
        # keys of the pattern "horizontal_boolean_list_{j}", where {j} is the
        # grid's horizontal index. The vertical_boolean_dict is also populated by
        # the empty lists with the keys of the pattern
        # "vertical_boolean_list_{j}", where {j} is its vertical index, as the
        # both dimensions of the  numpy.ndarray's (matrix) are equal.

        j: int

        for j in range(0, len_matrix):

            horizontal_boolean_dict[f"horizontal_boolean_list_{j}"] = []
            vertical_boolean_dict[f"vertical_boolean_list_{j}"] = []

        # The index_list is instantiated as the list of integers,
        # where integer ∈ <0, len_matrix - 1>.

        index_list: List[int] = list(range(0, len_matrix))

        # For the each index in index_list the new loop is instantiated.
        # In that loop, the index is held constant up until the next range of
        # indices (i), where i ∈ <0, len_matrix - 1> , won't be checked for the
        # condition of equality of the consecutive numpy.ndarray values (and not
        # being 0 at the same time) under the keys of the consecutive coordinates
        # (index, i) and (index, i + 1) in the same row. If that condition is
        # fulfilled, the boolean True is appended to the list in the
        # horizontal_boolean_dict under the key of "horizontal_boolean_list_{index}"
        # where {index} is the horizontal index. If the values of the consecutive
        # horizontal cells are not equal, the boolean False is appended to that
        # list under the same key value of the horizontal_boolean_dict.

        # index there is the horizontal index of the numpy.ndarray.

        index: int

        for index in index_list:

            # i: the vertical index of the numpy.ndarray

            i: int

            for i in range(0, len_matrix - 1):

                if new_matrix_1[(index, i)] == new_matrix_1[(index, i + 1)] != 0 \
                        and ((new_matrix_1[(index, i)] == new_matrix_1[(index, i + 1)] == 1)
                             or (new_matrix_1[(index, i)] == new_matrix_1[(index, i + 1)] == 2)):

                    horizontal_boolean_dict[f"horizontal_boolean_list_{index}"].append(True)

                elif new_matrix_1[(index, i)] != new_matrix_1[(index, i + 1)]:

                    horizontal_boolean_dict[f"horizontal_boolean_list_{index}"].append(False)

        # For the each index in index_list the new loop is instantiated.
        # In that loop, the index is held constant until the next range of
        # indices (i), where i ∈ <0, len_matrix - 1>, won't be checked for the
        # condition of equality of the consecutive numpy.ndarray values
        # (and not being 0 at the same time) under the keys of the corresponding
        # consecutive coordinates: (i, index) and (i + 1, index) in the same
        # column. If that condition is fulfilled, the boolean True is appended to
        # the list in the vertical_boolean_dict under the key of
        # "vertical_boolean_list_{index}", where {index} is the vertical index
        # of the numpy.ndarray. If the values of the consecutive vertical cells
        # are not equal, the boolean False is appended to that list under the
        # same key value of the vertical_boolean_dict.

        # index here is the vertical index of the numpy.ndarray.

        for index in index_list:

            # i: here is the horizontal index.

            for i in range(0, len_matrix - 1):

                if new_matrix_1[(i, index)] == new_matrix_1[(i + 1, index)] != 0 \
                        and ((new_matrix_1[(i, index)] == new_matrix_1[(i + 1, index)] == 1)
                             or (new_matrix_1[(i, index)] == new_matrix_1[(i + 1, index)] == 2)):

                    vertical_boolean_dict[f"vertical_boolean_list_{index}"].append(True)

                elif new_matrix_1[(i, index)] != new_matrix_1[(i + 1, index)]:

                    vertical_boolean_dict[f"vertical_boolean_list_{index}"].append(False)

        # The win_vertically_boolean_list is instantiated as an empty list.

        win_vertically_boolean_list: List[bool] = []

        # For each index in the index_list, if the list under the key
        # "vertical_boolean_list_{index}" in the vertical_boolean_dict dictionary is
        # not empty (and therefore evaluates to True), if False is in the list,
        # the boolean False is appended to the win_vertically_boolean_list list.
        # If False is not in the aforementioned list, the boolean True is appended
        # to the win_vertically_boolean_list list. If the
        # vertical_boolean_dict[f"vertical_boolean_list_{index}"] list is empty
        # (or it evaluates to False), the boolean False is appended to
        # win_vertically_boolean_list list.

        for index in index_list:

            if vertical_boolean_dict[f"vertical_boolean_list_{index}"]:

                if False in vertical_boolean_dict[f"vertical_boolean_list_{index}"]:

                    win_vertically_boolean_list.append(False)

                elif False not in vertical_boolean_dict[f"vertical_boolean_list_{index}"]:

                    win_vertically_boolean_list.append(True)

            win_vertically_boolean_list.append(False)

        # The win_horizontally_boolean_list is instantiated as an empty list.

        win_horizontally_boolean_list: List[bool] = []

        # For each index in the index_list, if the list under the key
        # "horizontal_boolean_list_{index}" in the horizontal_boolean_dict dictionary
        # is not empty (and therefore evaluates to True), if False is in the list,
        # the boolean False is appended to win_horizontally_boolean_list list.
        # If False is not in the aforementioned list, the boolean True is appended
        # to the win_horizontally_boolean_list list. If the
        # horizontal_boolean_dict[f"horizontal_boolean_list_{index}"] list is empty
        # (or evaluates to False), the boolean False is appended to
        # the win_horizontally_boolean_list list.

        for index in index_list:

            if horizontal_boolean_dict[f"horizontal_boolean_list_{index}"]:

                if False in horizontal_boolean_dict[f"horizontal_boolean_list_{index}"]:

                    win_horizontally_boolean_list.append(False)

                elif False not in horizontal_boolean_dict[f"horizontal_boolean_list_{index}"]:

                    win_horizontally_boolean_list.append(True)

            win_horizontally_boolean_list.append(False)

        # The truthy_list is instantiated as an empty list.

        truthy_list: List[bool] = []

        # If True is in win_horizontally_boolean_list list or True is in the
        # win_vertically_boolean_list list, the boolean True is appended to the
        # truthy_list. If True is not in the win_horizontally_boolean_list list or
        # True is not in the win_vertically_boolean_list list, the boolean False
        # is appended to the truthy_list.

        if True in win_horizontally_boolean_list:
            truthy_list.append(True)

        if True in win_vertically_boolean_list:
            truthy_list.append(True)

        if True not in win_horizontally_boolean_list:
            truthy_list.append(False)

        if True not in win_vertically_boolean_list:
            truthy_list.append(False)

        # If True is in truthy_list, the boolean True is returned.
        # Otherwise - the boolean False is returned.

        return any(truthy_list)

    def draw(self, new_matrix_1: ndarray) -> bool:
        """
        Evaluates the passed-in numpy.ndarray (the matrix numpy.ndarray) for
        the possibility of the draw. In the event of the constitution of cells
        of the passed-in matrix suggesting a draw - the method
        returns the boolean True. Otherwise - it returns the boolean False.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param new_matrix_1: A numpy.ndarray passed in for the evaluation.
        Example: [[0, 1, 2, 0], [1, 0, 2, 1], [0, 2, 0, 1], [2, 0, 0, 0]].
        :type new_matrix_1: numpy.ndarray
        :return: True if there is a draw, False otherwise. Example: True.
        :rtype: bool
        """

        # The horizontal dimension (the one of the numpy.ndarray's equal
        # dimensions is extracted from the numpy.ndarray's shape property
        # (the matrix numpy.ndarray).

        len_matrix: int = new_matrix_1.shape[0]

        # The index_list instantiated as the list of integers,
        # where integer ∈ <0, len_matrix - 1>.

        index_list: List[int] = list(range(0, len_matrix))

        # The truthy_list is instantiated as an empty list.

        truthy_list: List[bool] = []

        # All the matrix numpy.ndarray's cells are checked for their value.
        # If the value of the cell is different from 0, the boolean True is
        # appended to the truthy_list list. If the value of the cell equals 0,
        # the boolean False is appended to the truthy_list list.

        index: int

        for index in index_list:

            i: int

            for i in range(0, len_matrix):

                if new_matrix_1[(index, i)] != 0:

                    truthy_list.append(True)

                elif new_matrix_1[(index, i)] == 0:

                    truthy_list.append(False)

        # If False is in the truthy_list list, the method returns boolean
        # False. If False is not in the truthy_list list and calling in the
        # methods diagonal_win and the vertical_and_horizontal_win with the
        # numpy.ndarray (matrix) passed in returns False in both cases,
        # the method returns the boolean True.

        if False in truthy_list:

            return False

        elif False not in truthy_list and (not self.diagonal_win(new_matrix_1)
                                           and (not self.vertical_and_horizontal_win(new_matrix_1))):

            return True

    def add_vertex(self, vertex_no: int) -> ndarray:
        """
        The method adds a consecutive, new vertex to the adjacency matrix.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param vertex_no: An integer passed in being the consecutive number of
        the next vertex to add to the adjacency matrix. Example: 3.
        :type vertex_no: int
        :returns: An adjacency matrix with the new added vertex enumerated as the
        vertex_no, which is the number passed in the method.
        Example: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        :rtype: numpy.ndarray
        """

        if vertex_no == 0:

            self.matrix = np.zeros((1,), dtype=int)

            return self.matrix

        else:

            add_row: ndarray = np.zeros((vertex_no + 1,), dtype=int)
            add_column: ndarray = np.zeros((vertex_no,), dtype=int)
            self.matrix = np.c_[self.matrix, add_column]
            self.matrix = np.r_[self.matrix, [add_row]]

            return self.matrix

    def enter_the_coordinates_for_1_and_check_them(self) -> ndarray:
        """
        The player is prompted to enter the coordinates in the form of the 2
        integers divided by a single whitespace ("0 0" form). The coordinates are
        preprocessed into a tuple of 2 integers (all is done by the method
        enter_the_coordinates) and delegated to their own variables
        (first_coordinate, second_coordinate). The integer identity of the both
        variables is checked by the method check_if_coordinates_int. If the one or
        the both of them are not integers, the player is informed of it and
        prompted to enter the coordinates again. Then, the both coordinates are
        checked if they are in the bounds of the ranges of the coordinates set by
        the shape of the matrix (or the matrix or the game's grid). If
        one or both of the coordinates are out of the bounds, then the player is
        informed of it (altogether with displaying the correct range), and
        prompted for entering the coordinates again. If the cell is already
        occupied, the player is informed of it and prompted to enter the
        coordinates once again. Finally, if the cell is empty (or it equals to 0),
        the new 1 is positioned in the numpy.ndarray according to the coordinates
        passed into the method add_1. The new matrix (numpy.ndarray) is
        displayed by the method display_matrix and returned. In the further
        iterations of the class, the method doesn't ask the player for the
        coordinates, but draws the coordinates pseudorandomly from the
        prepopulated list.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :returns: The matrix (numpy.ndarray) with the newly positioned 1 according
         to the coordinates passed in by the player.
         Example: [[0, 1, 0], [0, 2, 0], [0, 0, 0]].
        :rtype: numpy.ndarray
        """

        coordinates: Tuple[int, int] = self.enter_the_coordinates()

        first_coordinate: int = coordinates[0]
        second_coordinate: int = coordinates[1]

        while not self.check_if_coordinates_int(first_coordinate, second_coordinate):

            print("The coordinates must be integer numbers!!")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        while not self.check_if_coordinates_in_range(
                first_coordinate, second_coordinate):

            print(f"The coordinates must be in range <0,"
                  f" {self.matrix.shape[0] - 1}>.")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        while not self.check_if_cell_occupied(first_coordinate, second_coordinate):

            print("This cell is occupied. Choose another one!")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        if self.check_if_cell_occupied(first_coordinate, second_coordinate):

            matrix_with_new_1: ndarray = \
                self.add_1((first_coordinate, second_coordinate))

            self.display_matrix(matrix_with_new_1)

            return matrix_with_new_1

    def enter_the_coordinates_for_2_and_check_them(self) -> ndarray:
        """
        The player is prompted to enter the coordinates in the form of the 2
        integers divided by a single whitespace ("0 0" form). The coordinates are
        preprocessed into a tuple of 2 integers (all is done by the method
        enter_the_coordinates) and delegated to their own variables
        (first_coordinate, second_coordinate). The integer identity of the both
        variables is checked by the method check_if_coordinates_int. If the one or
        two of them are not integers, the player is informed of it and prompted to
        enter the coordinates again. Then, the both coordinates are checked if
        they are in the bounds of the ranges of the coordinates set by the shape
        of the matrix (or the matrix or the game's grid). If one or both
        of the coordinates are out of the bounds, then the player is informed of it
        (altogether with displaying the correct range), and prompted to enter
        the coordinates again. If the cell is already occupied, the player is
        informed of it and prompted to enter the coordinates once again. Finally,
        if the cell is empty (or it equals to 0), the new 2 is positioned in the
        matrix according to the coordinates passed into the method add_2.
        The new matrix (numpy.ndarray) is displayed by the method display_matrix
        and returned. In the further iterations of the class, the method doesn't
        ask the player for the coordinates, but draws the coordinates
        pseudorandomly from the prepopulated list.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :returns: The matrix (numpy.ndarray) with the newly positioned 2 according
        to the coordinates passed in by the player.
        Example: [[0, 0, 2], [0, 0, 0], [0, 0, 0]].
        :rtype: numpy.ndarray
        """

        coordinates: Tuple[int, int] = self.enter_the_coordinates()

        first_coordinate: int = coordinates[0]
        second_coordinate: int = coordinates[1]

        while not self.check_if_coordinates_int(first_coordinate, second_coordinate):

            print("The coordinates must be integer numbers!!")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        while not self.check_if_coordinates_in_range(
                first_coordinate, second_coordinate):

            print(f"The coordinates must be in range <0,"
                  f" {self.matrix.shape[0] - 1}>.")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        while not self.check_if_cell_occupied(first_coordinate, second_coordinate):

            print("This cell is occupied. Choose another one!")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        if self.check_if_cell_occupied(first_coordinate, second_coordinate):

            matrix_with_new_2: ndarray = \
                self.add_2((first_coordinate, second_coordinate))

            self.display_matrix(matrix_with_new_2)

            return matrix_with_new_2

    def display_coordinates(self, new_matrix_len: int) -> List[str]:
        """
        Having passed in the one of the dimensions of the np.ndarray
        (new_matrix_len), it returns the list of the coordinates available in the
        matrix for their further display by the method
        display_coordinates_matrix.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param new_matrix_len: The horizontal dimension of the matrix. Example: 3.
        :type new_matrix_len: int
        :returns: The list of the coordinates available in the matrix.
        Example: ['(0,0)(0,1)(0,2)', '(1,0)(1,1)(1,2)', '(2,0)(2,1),(2,2)'].
        :rtype: List[str]
        """

        len_matrix: int = new_matrix_len

        index_list: List[int] = list(range(0, len_matrix))

        bigger_list: List[str] = []

        index: int

        for index in index_list:

            new_list: List[Dict[Tuple[int, int], str]] = []

            i: int

            for i in range(0, len_matrix):
                self.coordinates_matrix[(index, i)] = f"({index},{i})"
                new_list.append(self.coordinates_matrix[(index, i)])
                new: str = ''.join(new_list)

            bigger_list.append(new)

        return bigger_list

    def enter_the_coordinates(self) -> Tuple[int, int]:
        """
        Prompts entering of the coordinates by the player in the form of the
        string of the 2 integers separated by a single whitespace ("0 0"). If the
        player will be unfortunate enough to spoil the coordinates at the
        beginning or/and at the end of the string with the accidental whitespaces
        and other non-alphanumeric symbols an attempt will be made to unclutter
        the string. The string will be splitted into the list and the numerical
        identity of the i-th item of the list will be checked. Those positively
        tested will be returned as a tuple of 2 integers.

        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        returns: A tuple of 2 integers processed from the string user input.
        An integer ∈ <0, self.matrix.shape[0] - 1>.
        Example: (1, 1).
        rtype: Tuple[int, int]
        """

        try:

            coordinates: str = input("Enter the coordinates: '0 0' > ")

            coordinates: str = coordinates.strip()
            coordinates_list: List[str] = coordinates.split(" ")
            new_coordinates_list: List[int] = []

            coordinate: str

            for coordinate in coordinates_list:
                coordinate: str = coordinate.strip()
                if coordinate.isdigit():
                    coordinate_int: int = int(coordinate)
                    new_coordinates_list.append(coordinate_int)
            return new_coordinates_list[0], new_coordinates_list[1]

        except IndexError:

            print("You had IndexError. Try again.")

            coordinates = input("Enter the coordinates: '0 0' > ")
            coordinates = coordinates.strip()
            coordinates_list = coordinates.split(" ")
            new_coordinates_list = []
            for coordinate in coordinates_list:
                coordinate = coordinate.strip()
                if coordinate.isdigit():
                    coordinate_int = int(coordinate)
                    new_coordinates_list.append(coordinate_int)
            return new_coordinates_list[0], new_coordinates_list[1]

    def check_if_coordinates_int(self, first_coordinate: int,
                                 second_coordinate: int) -> bool:
        """
        Returns False if the first or the second coordinate is not an instance of
        an integer.
        Otherwise returns True.

        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        :param first_coordinate: The first coordinate of the pair.
        An integer ∈ <0, self.matrix.shape[0] - 1>. Example: 1.
        :type first_coordinate: int
        :param second_coordinate: The second coordinate of the pair.
        An integer ∈ <0, self.matrix.shape[0] - 1>. Example: 2.
        :type second_coordinate: int
        :returns: False if the first or the second coordinate is not an instance
         of an integer. Otherwise returns True. Example: False.
        :rtype: bool
        """

        if not isinstance(first_coordinate, int) or \
                not isinstance(second_coordinate, int):
            return False

        return True

    def check_if_coordinates_in_range(self, first_coordinate: int,
                                      second_coordinate: int) -> bool:
        """
        Returns False if the first or the second coordinate
        ∉ <0, self.matrix.shape[0] - 1>.
        Otherwise returns True.

        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        :param first_coordinate: The first coordinate of the pair.
        An integer ∈ <0, self.matrix.shape[0] - 1>. Example: 2.
        :type first_coordinate: int
        :param second_coordinate: The second coordinate of the pair.
        An integer ∈ <0, self.matrix.shape[0] - 1>. Example: 3.
        :type second_coordinate: int
        :returns: False if the first or the second coordinate
        ∉ <0, self.matrix.shape[0] - 1>. Otherwise returns True.
         Example: True.
        :rtype: bool
        """

        coordinates_range_list: List[int] = list(
            range(0, self.matrix.shape[0]))

        if first_coordinate not in coordinates_range_list \
                or second_coordinate not in coordinates_range_list:

            return False

        return True

    def check_if_cell_occupied(
            self, first_coordinate: int,
            second_coordinate: int) -> bool:
        """
        Returns False if the numpy.ndarray under the (first_coordinate,
        second_coordinate) key is not empty (has other value than 0).
        Otherwise returns True.


        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        :param first_coordinate: The first coordinate of the pair
        (first part of the key).
        An integer ∈ <0, self.matrix.shape[0] - 1>. Example: 3.
        :type first_coordinate: int
        :param second_coordinate: The second coordinate of the pair
        (second part of the key).
         An integer ∈ <0, self.matrix.shape[0] - 1>. Example: 2.
        :type second_coordinate: int
        :returns: False if the numpy.ndarray value under the key
        (first_coordinate, second_coordinate) is not empty (is not a 0).
        Otherwise returns True. Example: False.
        :rtype: bool
        """

        try:

            if self.matrix[(first_coordinate, second_coordinate)] != 0:

                return False

            return True

        except IndexError:

            return False

    def add_1(self, pair: Tuple[int, int]) -> ndarray:
        """
        Method for adding the "edges", that is, method for entering
        1 (replacement for "X" or "O") under the key of passed-in 2-integer
        tuple in the matrix numpy.ndarray (the game's grid).
        Indexes from 0. The pair is appended to the edges list.

        :param pair: The tuple of 2 integers.
        An integer ∈ <0, self.matrix.shape[0] - 1>.
        Example: (1, 0).
        :type pair: Tuple[int, int]
        :returns: A numpy.ndarray with the newly positioned 1
        under a key of the passed-in 2-integer tuple.
        Example: [[1, 0, 0], [0, 0, 0], [0, 2, 0]].
        :rtype: numpy.ndarray
        """

        self.matrix[pair] = 1
        self.edges.append(pair)

        return self.matrix

    def add_2(self, pair: Tuple[int, int]) -> ndarray:
        """
        Method for adding the "edges", that is, method for entering
        2 (replacement for "X" or "O") under the key of the passed-in
        2-integer tuple in the matrix np.ndarray (the game's grid).
        Indexes from 0. The pair is appended to the edges list.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param pair: The tuple of 2 integers.
        An integer ∈ <0, self.matrix.shape[0] - 1>.
        Example: (0, 0).
        :type pair: Tuple[int, int]
        :returns: A numpy.ndarray with the newly positioned 2
        under the key of the passed-in 2-integer tuple.
        Example: [[1, 0, 0], [0, 0, 0], [0, 2, 0]].
        :rtype: numpy.ndarray

        """
        self.matrix[pair] = 2
        self.edges.append(pair)

        return self.matrix

    def find_connected_vertices(self, vertex_no: int) -> List[Tuple[int, int]]:
        """
        The method for finding the connected vertices
        in the adjacency matrix.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param vertex_no: The vertex for searching its connected vertices.
        An integer ∈ <0, self.matrix.shape[0] - 1>. Example: 2.
        :type vertex_no: int
        :return: A list of connected vertices (their coordinates).
        Example: [(3, 2), (2, 3)].
        :rtype: List[Tuple[int, int]]
        """

        connected_vertices: List[Tuple[int, int]] = []

        edge: Tuple[int, int]

        for edge in self.edges:

            if vertex_no in edge:

                connected_vertices.append(edge)

        return connected_vertices

    def display_adjacency_matrix(self) -> None:
        """
        The method for displaying an adjacency matrix without the
        square brackets.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :returns: Prints the matrix, returns None. Example: None.
        :rtype: None
        """

        s: str = str(self.construct_matrix)
        s = s.replace('[', '')
        s = s.replace(']', '')
        s = ' ' + s
        print(s)

    def display_matrix(self, adjacency_matrix: ndarray) -> None:
        """
        The method for displaying a matrix without the square brackets.
        Add a horizontal dividing line between the matrices during the
        game.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param adjacency_matrix: The passed-in numpy.ndarray.
        Example: [[1, 0, 0], [0, 0, 0], [0, 2, 0]].
        :return: It prints the numpy.ndarray without the square brackets.
        Returns None. Example: None.
        :rtype: None
        """

        line: str = "-" * 2 * adjacency_matrix.shape[0]
        line: str = line + "-"
        print(line)

        s: str = str(adjacency_matrix)
        s = s.replace('[', '')
        s = s.replace(']', '')
        s = ' ' + s
        print(s)

    def display_coordinates_matrix(self, adjacency_matrix: List[str]) -> None:
        """
        The method for displaying the coordinates matrix without the
        square brackets.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param adjacency_matrix: The list of strings with the
         coordinates of the matrix (numpy.ndarray).
         Example: ['(0,0)(0,1)(0,2)', '(1,0)(1,1)(1,2)', '(2,0)(2,1),(2,2)'].
        :type adjacency_matrix: List[str]
        :return: It prints the matrix without the square brackets. Returns None.
        Example: None.
        :rtype: None
        """

        print("The coordinates of the cells: ")

        coordinates_row: str

        for coordinates_row in adjacency_matrix:
            s: str = str(coordinates_row)
            s = s.replace('[', '')
            s = s.replace(']', '')
            print(f"{s}")


class AdjacencyMatrixTicTacToeAutomaticBuild(AdjacencyMatrixTicTacToe):
    """
    The tic-tac-toe gameplay with customised dimensions which are
    pseudorandomly chosen from the range if integers, where
    integer ∈ <3, 101>, for the automatic building and testing purposes.
    """

    # The coordinates_already_drawn is instantiated as an empty list.
    # It accumulates the coordinates the coordinates that had been
    # already drawn in the pseudorandom manner or typed in, where applicable.

    coordinates_already_drawn: List[str] = []

    def construct_matrix(self) -> ndarray:
        """
        The method overrides the construct_matrix method in the superclass.
        The method draws the dimensions of matrix (therefore the
        dimensions of the tic-tac-toe grid) pseudorandomly from the range of
        integer numbers ∈ <3, 101>. The chosen dimensions of the matrix are
        then printed. The chosen dimensions are plugged into the
        display_coordinates method, where the list of the coordinates is
        constructed. Then, that list is plugged into the
        display_coordinates_matrix method where it is converted into a view of
        the accessible coordinates in a form of the coordinates' matrix and
        printed at the beginning of the game. In the next step, an "empty matrix"
        in the form of numpy.ndarray of the chosen dimensions composed of zeros is
        created and plugged into the display_matrix method where it is converted
        to the string and printed out in the neat format (without the numpy's
        brackets). The so-called matrix numpy.ndarray (the game's grid)
        is also constructed in a way which was borrowed from the method previously
        employed in the adding of the vertices to the adjacency matrix. That's a
        more complicated way of constructing an initial adjacency matrix composed
        of zeros than just creating the numpy.ndarray with the method
        numpy.zeros((dimensions_of_the_matrix, dimensions_of_the_matrix),
        dtype=int). For the dimension in the range from 0 to the
        (dimensions_of_matrix - 1), if dimension == 0, the 2D numpy.ndarray array
        [[0]] is created, for the greater values of vertices the matrix
        is updated with the column of zeros and then with the row of zeros
        adjusted to the new length of the matrix.
        The matrix numpy.ndarray (or matrix, or the game's grid) is
        returned after construction.

        :param self: An instance of the class.
        :type self: An instance of the class
        :returns: A numpy.ndarray with the chosen dimensions (the game's grid)
        composed of zeros. Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
        :rtype: numpy.ndarray
        """

        random_matrix_dimension: int = randint(3, 101)

        print(f"Dimensions of the matrix:"
              f" {random_matrix_dimension} x {random_matrix_dimension} ")

        self.display_coordinates_matrix(
            self.display_coordinates(random_matrix_dimension))

        empty_matrix: ndarray = \
            np.zeros((random_matrix_dimension, random_matrix_dimension), dtype=int)

        self.display_matrix(empty_matrix)

        dimension: int

        for dimension in range(0, random_matrix_dimension):

            if dimension == 0:

                self.matrix = np.zeros((1,), dtype=int)

            else:

                add_row: ndarray = np.zeros((dimension + 1,), dtype=int)
                add_column: ndarray = np.zeros((dimension,), dtype=int)
                self.matrix = np.c_[self.matrix, add_column]
                self.matrix = np.r_[self.matrix, [add_row]]

        return self.matrix

    def enter_the_coordinates_for_1_and_check_them(self) -> ndarray:
        """
        The two coordinates in the form of the string divided by a single
        whitespace ("0 0" form) are drawn pseudorandomly from the list.
        The coordinates are preprocessed into a tuple of 2 integers (all is
        done by the enter_the_coordinates method) and delegated to their own
        variables (first_coordinate, second_coordinate). The integer identity of
        the both variables is checked by the check_if_coordinates_int method.
        Then, the both coordinates are checked if they are in the bounds of
        the ranges of the coordinates set by the shape of the matrix
        numpy.ndarray (or the matrix or the game's grid).  The coordinates
        are checked if they haven't been drawn from the list previously.
        If that was the case, the new ones are drawn. Finally, if the cell is
        empty (or equals to 0), the new 1 is positioned in the numpy.ndarray
        according to the coordinates passed into the method add_1. The new
        matrix (numpy.ndarray) is displayed by the method display_matrix and
        returned.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :returns: The matrix (numpy.ndarray) with the newly positioned 1 according
        to the coordinates drawn pseudorandomly from the list.
        Example: [[0, 1, 0], [0, 0, 1], [2, 0, 0]].
        :rtype: numpy.ndarray
        """

        coordinates: Tuple[int, int] = self.enter_the_coordinates()

        first_coordinate: int = coordinates[0]
        second_coordinate: int = coordinates[1]

        while not self.check_if_coordinates_int(first_coordinate, second_coordinate):

            print("The coordinates must be integer numbers!!")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        while not self.check_if_coordinates_in_range(
                first_coordinate, second_coordinate):

            print(f"The coordinates must be in range <0,"
                  f" {self.matrix.shape[0] - 1}>.")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        while not self.check_if_cell_occupied(first_coordinate, second_coordinate):

            print("This cell is occupied. Choose another one!")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        if self.check_if_cell_occupied(first_coordinate, second_coordinate):

            matrix_with_new_1: ndarray = \
                self.add_1((first_coordinate, second_coordinate))

            self.display_matrix(matrix_with_new_1)

            return matrix_with_new_1

    def enter_the_coordinates_for_2_and_check_them(self) -> ndarray:
        """
        The two coordinates in the form of the string divided by a single
        whitespace ("0 0" form) are drawn pseudorandomly from the list.
        The coordinates are preprocessed into a tuple of 2 integers (all is
        done by the enter_the_coordinates method) and delegated to their own
        variables (first_coordinate, second_coordinate). The coordinates
        are checked, if they haven't been drawn from the list previously.
        If that was the case, the new ones are drawn. Finally, if the cell is
        empty (or equals to 0), the new 2 is positioned in the numpy.ndarray
        according to the coordinates passed into the add_2 method. The new
        matrix (numpy.ndarray) is displayed by the method display_matrix and
        returned.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :returns: The matrix (numpy.ndarray) with the newly positioned 2 according
        to the coordinates drawn pseudorandomly from the list.
        Example: [[2, 0, 1], [0, 0, 0], [0, 0, 0]].
        :rtype: numpy.ndarray
        """

        coordinates: Tuple[int, int] = self.enter_the_coordinates()

        first_coordinate: int = coordinates[0]
        second_coordinate: int = coordinates[1]

        while not self.check_if_coordinates_int(first_coordinate, second_coordinate):

            print("The coordinates must be integer numbers!!")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        while not self.check_if_coordinates_in_range(
                first_coordinate, second_coordinate):

            print(f"The coordinates must be in range <0, "
                  f"{self.matrix.shape[0] - 1}>")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        while not self.check_if_cell_occupied(first_coordinate, second_coordinate):
            print("This cell is occupied. Choose another one!")

            first_coordinate, second_coordinate = self.enter_the_coordinates()

        if self.check_if_cell_occupied(first_coordinate, second_coordinate):

            matrix_with_new_2: ndarray = \
                self.add_2((first_coordinate, second_coordinate))

            self.display_matrix(matrix_with_new_2)

            return matrix_with_new_2

    def matrix_len(self) -> int:
        """
        Returns the horizontal dimension of the matrix.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :return: The horizontal dimension of the matrix. Example: 6.
        :rtype: int
        """
        len_matrix: int = self.matrix.shape[0]
        return len_matrix

    def enter_the_coordinates(self) -> Tuple[int, int]:
        """
        The method overrides the enter_the_coordinates method in the superclass.
        The coordinates are drawn pseudorandomly from the list in the form
        of the the string of the 2 integers separated by a single
        whitespace ("0 0"). If the coordinates are spoiled at the beginning
        or/and at the end of the string with the accidental whitespaces and
        symbols an attempt will be made to unclutter the string. The string will
        be splitted into the list and the numerical identity of the symbol will be
        checked. Those positively tested will be returned as a tuple of 2 integers.

        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        :returns: A tuple of 2 integers processed from the pseudorandomly drawn
        raw string of the coordinates (("0 0") form). Example: "1 3".
        An integer ∈ <0, self.matrix.shape[0] - 1>.
        Example: (1, 1).
        rtype: Tuple[int, int]

        """

        coordinates: str = self.choose_the_random_coordinates()

        coordinates: str = coordinates.strip()
        coordinates_list: List[str] = coordinates.split(" ")

        new_coordinates_list: List[int] = []

        coordinate: str

        for coordinate in coordinates_list:

            coordinate: str = coordinate.strip()

            if coordinate.isdigit():
                coordinate_int: int = int(coordinate)
                new_coordinates_list.append(coordinate_int)

        return new_coordinates_list[0], new_coordinates_list[1]

    def choose_the_random_coordinates(self) -> str:
        """
        Chooses pseudorandomly a pair of the coordinates from the list.
        A pair of the coordinates can be chosen only once from the list,
        as the chosen coordinates are appended to the all-class
        coordinates-already-drawn list and then checked if they
        accidentally hadn't been drawn before - if that was the case the
        coordinates are drawn till the unique pair (that is, those coordinates
        that hadn't been drawn before) will be chosen. The list of the available
        coordinates is prepopulated using the horizontal dimension of the
        matrix extracted by the method matrix_len.

        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        :returns: A string of the coordinates in the format "0 0".
        Example: "2 3".
        :rtype: str
        """

        coordinates_list: List[str] = []

        matrix_len: int = self.matrix_len()

        i: int

        for i in range(0, matrix_len):

            j: int

            for j in range(0, matrix_len):

                coordinates_list.append(f"{i} {j}")

        random_coordinate: str = \
            coordinates_list[randint(0, len(coordinates_list) - 1)]

        while random_coordinate in self.coordinates_already_drawn:

            random_coordinate = coordinates_list[randint(0, len(coordinates_list) - 1)]

        if random_coordinate not in self.coordinates_already_drawn:

            self.coordinates_already_drawn.append(random_coordinate)

        return random_coordinate


class AdjacencyMatrixTicTacToeAutomaticBuildSmaller(
      AdjacencyMatrixTicTacToeAutomaticBuild):
    """
    The tic-tac-toe gameplay with the customised dimensions. Chosen
    pseudorandomly from the range ∈ <3, 6>. That version of the game was
    written for the automatic building and testing purposes.
    """

    # The coordinates_already_drawn is instantiated as an empty list.

    coordinates_already_drawn: List[str] = []

    def construct_matrix(self) -> ndarray:
        """
        The method construct_matrix overrides the method in the parent class.
        The method draws the dimensions of the matrix (therefore the
        dimensions of the tic-tac-toe grid) pseudorandomly from the range of
        integer numbers, where integer ∈ <3, 6> The chosen dimensions of the
        matrix are then printed. The chosen dimensions are plugged into the
        display_coordinates method, where the list of the coordinates is
        constructed. That list is then plugged into the
        display_coordinates_matrix method where it is converted into a view
        of the accessible coordinates in a form of the coordinates' matrix and
        printed at the beginning of the game. In the next step, an "empty matrix"
        in the form of the numpy.ndarray of the drawn dimensions composed of zeros
        is created and plugged into the display_matrix method where it is
        converted to the string and printed out in the neat format (without the
        numpy's brackets). The so-called matrix numpy.ndarray (the
        game's grid) is also constructed in a way which was borrowed from the
        method previously employed in adding of the vertices to the adjacency
        matrix. That's a more complicated way of constructing an initial adjacency
        matrix composed of zeros than just creating the numpy.ndarray with the
        method numpy.zeros((dimensions_of_the_matrix, dimensions_of_the_matrix),
        dtype = int). For the dimension values in the range of
        ∈ <0, (dimensions_of_matrix - 1)>, if the dimension == 0, the 2D
        numpy.ndarray array [[0]] is created, for the greater values of vertices
        the matrix is updated with the column of zeros and then with the
        row of zeros adjusted to the new length of the matrix. The
        matrix numpy.ndarray (or matrix, or the game's grid) is returned
        after construction.

        :param self: An instance of the class.
        :type self: An instance of the class
        :returns: A numpy.ndarray with the pseudorandomly drawn dimensions from
        the range ∈ <3, 6> (the game's grid) composed of zeros.
         Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
        :rtype: numpy.ndarray
        """

        random_matrix_dimension: int = randint(3, 6)

        print(f"Dimensions of the matrix:"
              f" {random_matrix_dimension} x {random_matrix_dimension} ")

        self.display_coordinates_matrix(
            self.display_coordinates(random_matrix_dimension))

        empty_matrix: ndarray =\
            np.zeros((random_matrix_dimension, random_matrix_dimension), dtype=int)

        self.display_matrix(empty_matrix)

        dimension: int

        for dimension in range(0, random_matrix_dimension):

            if dimension == 0:

                self.matrix = np.zeros((1,), dtype=int)

            else:

                add_row: ndarray = np.zeros((dimension + 1,), dtype=int)
                add_column: ndarray = np.zeros((dimension,), dtype=int)
                self.matrix = np.c_[self.matrix, add_column]
                self.matrix = np.r_[self.matrix, [add_row]]

        return self.matrix


class AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice(
      AdjacencyMatrixTicTacToeAutomaticBuild):
    """
    The tic-tac-toe game with customised dimensions which you can choose
    and the automatic gameplay.
    """

    # The coordinates_already_drawn is instantiated as an empty list.

    coordinates_already_drawn: List[str] = []

    def construct_matrix(self) -> ndarray:
        """
        The method construct_matrix overrides the method in the parent class.
        This method asks the player for the dimensions of the ndarray (therefore
        the dimensions of the tic-tac-toe grid) in a form an integer number.
        If the ValueError has taken place (the player hasn't typed in the integer
        with the base 10), the player is informed of the mistake and asked for
        the dimensions of the grid (matrix, numpy.ndarray) again. The
        chosen dimensions are plugged into the display_coordinates method, where
        the list of the coordinates is constructed. Then, that list
        is plugged into the display_coordinates_matrix method where it is
        converted into a view of the accessible coordinates in a form of the
        coordinates' matrix and printed at the beginning of the game. In the next
        step, an empty matrix in the form of numpy.ndarray of the chosen
        dimensions composed of zeros is created and plugged into the
        display_matrix method where it is converted and printed out in the neat
        format (without the numpy's brackets). The so-called matrix
        (the game's grid) is also constructed in a way which was borrowed from the
        method previously employed in the adding of the vertices to the adjacency
        matrix. That's a more complicated way of constructing an adjacency matrix
        composed of zeros than just creating the numpy.ndarray with the method
        numpy.zeros((dimensions_of_the_matrix, dimensions_of_the_matrix),
        dtype=int). For the dimension in range from 0 to the
        (dimensions_of_matrix - 1), if dimension == 0, the numpy.ndarray array [[0]]
        is created, for the greater values of vertices the matrix is
        updated with the column of zeros and the with the new row of zeros adjusted
        to the new length of the matrix. The matrix (or matrix,
        or the game's grid) is returned after construction.

        :param self: An instance of the class.
        :type self: An instance of the class
        :returns: A numpy.ndarray with the chosen dimensions (the game's grid)
        composed of zeros. Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
        :rtype: numpy.ndarray
        """

        try:

            dimension_of_matrix: int = int(input("Choose the dimensions of the matrix: "))

            print(f"Dimensions of the matrix: "
                  f"{dimension_of_matrix} x {dimension_of_matrix} ")

            self.display_coordinates_matrix(self.display_coordinates(dimension_of_matrix))

            empty_matrix: ndarray = \
                np.zeros((dimension_of_matrix, dimension_of_matrix), dtype=int)
            self.display_matrix(empty_matrix)

            dimension: int

            for dimension in range(0, dimension_of_matrix):

                if dimension == 0:

                    self.matrix = np.zeros((1,), dtype=int)

                else:

                    add_row: ndarray = np.zeros((dimension + 1,), dtype=int)
                    add_column: ndarray = np.zeros((dimension,), dtype=int)
                    self.matrix = np.c_[self.matrix, add_column]
                    self.matrix = np.r_[self.matrix, [add_row]]

            return self.matrix

        except ValueError:

            print("You had ValueError. Please enter the integer with the base 10.")

            dimension_of_matrix: int = int(input("Choose the dimensions of the matrix: "))

            print(f"Dimensions of the matrix: "
                  f"{dimension_of_matrix} x {dimension_of_matrix} ")

            self.display_coordinates_matrix(self.display_coordinates(dimension_of_matrix))

            empty_matrix = np.zeros((dimension_of_matrix, dimension_of_matrix), dtype=int)

            self.display_matrix(empty_matrix)

            for dimension in range(0, dimension_of_matrix):

                if dimension == 0:

                    self.matrix = np.zeros((1,), dtype=int)

                else:

                    add_row = np.zeros((dimension + 1,), dtype=int)
                    add_column = np.zeros((dimension,), dtype=int)
                    self.matrix = np.c_[self.matrix, add_column]
                    self.matrix = np.r_[self.matrix, [add_row]]

            return self.matrix


class AdjacencyMatrixTicTacToeAutomaticBuild1Human2Computer(
      AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice):
    """
    The tic-tac-toe gameplay with customised dimensions which are
    pseudorandomly chosen from the range if integers, where
    integer ∈ <3, 101>, for the automatic building and testing purposes.
    """

    # The coordinates_already_drawn is instantiated as an empty list.

    coordinates_already_drawn: List[str] = []

    def enter_the_coordinates_for_1_and_check_them(self) -> ndarray:
        """
        This method overrides the method in the parent class.
        The two coordinates separated by a single space are typed in by the
        player. The coordinates are preprocessed into a tuple of 2 integers
        (all is done by the enter_the_coordinates_1 method) and delegated to
        their own variables (first_coordinate, second_coordinate).
        The integer identity of the both variables is checked by the
        check_if_coordinates_int method. Then, the both coordinates are
        checked if they are in the bounds of the ranges of the coordinates
        set by the shape of the matrix numpy.ndarray (or the matrix
        or the game's grid).  The coordinates are checked if they haven't been
        drawn from the list previously. If that was the case, the new ones are
        drawn. Finally, if the cell is empty (or equals to 0), the new 1 is
        positioned in the numpy.ndarray according to the coordinates passed
        into the method add_1. The new matrix (numpy.ndarray) is displayed
        by the method display_matrix and returned.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :returns: The matrix (numpy.ndarray) with the newly positioned 1 according
        to the coordinates drawn pseudorandomly from the list.
        Example: [[0, 1, 0], [0, 0, 1], [2, 0, 0]].
        :rtype: numpy.ndarray
        """

        coordinates: Tuple[int, int] = self.enter_the_coordinates_1()

        first_coordinate: int = coordinates[0]
        second_coordinate: int = coordinates[1]

        while not self.check_if_coordinates_int(first_coordinate, second_coordinate):

            print("The coordinates must be integer numbers!!")

            first_coordinate, second_coordinate = self.enter_the_coordinates_1()

        while not self.check_if_coordinates_in_range(
                first_coordinate, second_coordinate):

            print(f"The coordinates must be in range <0,"
                  f" {self.matrix.shape[0] - 1}>.")

            first_coordinate, second_coordinate = self.enter_the_coordinates_1()

        while not self.check_if_cell_occupied(first_coordinate, second_coordinate):

            print("This cell is occupied. Choose another one!")

            first_coordinate, second_coordinate = self.enter_the_coordinates_1()

        if self.check_if_cell_occupied(first_coordinate, second_coordinate):

            matrix_with_new_1: ndarray = \
                self.add_1((first_coordinate, second_coordinate))

            self.display_matrix(matrix_with_new_1)

            return matrix_with_new_1

    def enter_the_coordinates_for_2_and_check_them(self) -> ndarray:
        """
        This method overrides the method in the parent class.
        The two coordinates in the form of the string divided by a single
        whitespace ("0 0" form) are drawn pseudorandomly from the list.
        The coordinates are preprocessed into a tuple of 2 integers (all is
        done by the enter_the_coordinates_2 method) and delegated to their own
        variables (first_coordinate, second_coordinate). The coordinates
        are checked, if they haven't been drawn from the list previously.
        If that was the case, the new ones are drawn. Finally, if the cell is
        empty (or equals to 0), the new 2 is positioned in the numpy.ndarray
        according to the coordinates passed into the add_2 method. The new
        matrix (numpy.ndarray) is displayed by the method display_matrix and
        returned.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :returns: The matrix (numpy.ndarray) with the newly positioned 2 according
        to the coordinates drawn pseudorandomly from the list.
        Example: [[2, 0, 1], [0, 0, 0], [0, 0, 0]].
        :rtype: numpy.ndarray
        """

        coordinates: Tuple[int, int] = self.enter_the_coordinates_2()

        first_coordinate: int = coordinates[0]
        second_coordinate: int = coordinates[1]

        while not self.check_if_coordinates_int(first_coordinate, second_coordinate):

            print("The coordinates must be integer numbers!!")

            first_coordinate, second_coordinate = self.enter_the_coordinates_2()

        while not self.check_if_coordinates_in_range(
                first_coordinate, second_coordinate):

            print(f"The coordinates must be in range <0, "
                  f"{self.matrix.shape[0] - 1}>")

            first_coordinate, second_coordinate = self.enter_the_coordinates_2()

        while not self.check_if_cell_occupied(first_coordinate, second_coordinate):

            print("This cell is occupied. Choose another one!")

            first_coordinate, second_coordinate = self.enter_the_coordinates_2()

        if self.check_if_cell_occupied(first_coordinate, second_coordinate):

            matrix_with_new_2: ndarray = \
                self.add_2((first_coordinate, second_coordinate))

            self.display_matrix(matrix_with_new_2)

            return matrix_with_new_2

    def enter_the_coordinates_1(self) -> Tuple[int, int]:
        """
        The coordinates are typed in by the player to position the new 1 in the
        grid. If the coordinates are spoiled at the beginning or/and at the end
        of the string with the accidental whitespaces and symbols an attempt will
        be made to unclutter the string. The string will be splitted into the list
        and the numerical identity of the symbol will be checked. Those positively
        tested will be returned as a tuple of 2 integers.

        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        :returns: A tuple of 2 integers processed from the pseudorandomly drawn
        raw string of the coordinates (("0 0") form). Example: "1 3".
        An integer ∈ <0, self.matrix.shape[0] - 1>.
        Example: (1, 1).
        rtype: Tuple[int, int]

        """

        try:

            coordinates: str = input("Enter the coordinates: '0 0' > ")
            coordinates: str = coordinates.strip()
            self.coordinates_already_drawn.append(coordinates)
            coordinates_list: List[str] = coordinates.split(" ")
            new_coordinates_list: List[int] = []

            coordinate: str

            for coordinate in coordinates_list:
                coordinate: str = coordinate.strip()
                if coordinate.isdigit():
                    coordinate_int: int = int(coordinate)
                    new_coordinates_list.append(coordinate_int)
            return new_coordinates_list[0], new_coordinates_list[1]

        except IndexError:

            print("You had IndexError. Try again.")
            coordinates = input("Enter the coordinates: '0 0' > ")
            coordinates = coordinates.strip()
            self.coordinates_already_drawn.append(coordinates)
            coordinates_list = coordinates.split(" ")
            new_coordinates_list = []
            for coordinate in coordinates_list:
                coordinate: str = coordinate.strip()
                if coordinate.isdigit():
                    coordinate_int = int(coordinate)
                    new_coordinates_list.append(coordinate_int)
            return new_coordinates_list[0], new_coordinates_list[1]

    def enter_the_coordinates_2(self) -> Tuple[int, int]:
        """
        The coordinates are drawn pseudorandomly from the list in the form
        of the the string of the 2 integers separated by a single
        whitespace ("0 0") to position the new 2 in the grid. If the coordinates
        are spoiled at the beginning or/and at the end of the string with the
        accidental whitespaces and symbols an attempt will be made to unclutter
        the string. The string will be splitted into the list and the numerical
        identity of the symbol will be checked. Those positively tested will
        be returned as a tuple of 2 integers.

        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        :returns: A tuple of 2 integers processed from the pseudorandomly drawn
        raw string of the coordinates (("0 0") form). Example: "1 3".
        An integer ∈ <0, self.matrix.shape[0] - 1>.
        Example: (1, 1).
        rtype: Tuple[int, int]

        """

        coordinates: str = self.choose_the_random_coordinates()

        coordinates: str = coordinates.strip()
        coordinates_list: List[str] = coordinates.split(" ")

        new_coordinates_list: List[int] = []

        coordinate: str

        for coordinate in coordinates_list:

            coordinate: str = coordinate.strip()

            if coordinate.isdigit():
                coordinate_int: int = int(coordinate)
                new_coordinates_list.append(coordinate_int)

        return new_coordinates_list[0], new_coordinates_list[1]


class AdjacencyMatrixTicTacToeAutomaticBuild2Human1Computer(
      AdjacencyMatrixTicTacToeAutomaticBuild1Human2Computer):
    """
    The 1-player tic-tac-toe gameplay with the dimensions you can choose,
    and with the human player playing with 2.
    """

    # The coordinates_already_drawn is instantiated as an empty list.

    coordinates_already_drawn: List[str] = []

    def enter_the_coordinates_2(self) -> Tuple[int, int]:
        """
        The method overrides the enter_the_coordinates_2 method in the parent
        class and therefore changes the described behaviour of the connected
        method enter_the_coordinates_for_2_and_check_them in the parent class.
        The coordinates are typed in by the player to type in the new
        2 into the grid. If the coordinates are spoiled at the beginning
        or/and at the end of the string with the accidental whitespaces and
        symbols an attempt will be made to unclutter the string. The string will
        be splitted into the list and the numerical identity of the symbol will be
        checked. Those positively tested will be returned as a tuple of 2
        integers.

        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        :returns: A tuple of 2 integers processed from the pseudorandomly drawn
        raw string of the coordinates (("0 0") form). Example: "1 3".
        An integer ∈ <0, self.matrix.shape[0] - 1>.
        Example: (1, 1).
        rtype: Tuple[int, int]

        """

        try:

            coordinates: str = input("Enter the coordinates: '0 0' > ")
            coordinates: str = coordinates.strip()
            self.coordinates_already_drawn.append(coordinates)
            coordinates_list: List[str] = coordinates.split(" ")
            new_coordinates_list: List[int] = []

            coordinate: str

            for coordinate in coordinates_list:
                coordinate: str = coordinate.strip()
                if coordinate.isdigit():
                    coordinate_int: int = int(coordinate)
                    new_coordinates_list.append(coordinate_int)
            return new_coordinates_list[0], new_coordinates_list[1]

        except IndexError:

            print("You had IndexError. Try again.")
            coordinates = input("Enter the coordinates: '0 0' > ")
            coordinates = coordinates.strip()
            self.coordinates_already_drawn.append(coordinates)
            coordinates_list = coordinates.split(" ")
            new_coordinates_list = []
            for coordinate in coordinates_list:
                coordinate = coordinate.strip()
                if coordinate.isdigit():
                    coordinate_int = int(coordinate)
                    new_coordinates_list.append(coordinate_int)
            return new_coordinates_list[0], new_coordinates_list[1]

    def enter_the_coordinates_1(self) -> Tuple[int, int]:
        """
        The method overrides the enter_the_coordinates_1 method, which
        changes the behaviour of the connected method
        enter_the_coordinates_for_1_and_check_them in the parent class.
        The coordinates are drawn pseudorandomly from the list in the form
        of the the string of the 2 integers separated by a single
        whitespace ("0 0") to position the new 1. If the coordinates are
        spoiled at the beginning or/and at the end of the string with the
        accidental whitespaces and symbols an attempt will be made to unclutter
        the string. The string will be splitted into the list and the numerical
        identity of the symbol will be checked. Those positively tested will be
        returned as a tuple of 2 integers.

        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        :returns: A tuple of 2 integers processed from the pseudorandomly drawn
        raw string of the coordinates (("0 0") form). Example: "1 3".
        An integer ∈ <0, self.matrix.shape[0] - 1>.
        Example: (1, 1).
        rtype: Tuple[int, int]

        """

        coordinates: str = self.choose_the_random_coordinates()

        coordinates: str = coordinates.strip()
        coordinates_list: List[str] = coordinates.split(" ")

        new_coordinates_list: List[int] = []

        coordinate: str

        for coordinate in coordinates_list:

            coordinate: str = coordinate.strip()

            if coordinate.isdigit():
                coordinate_int: int = int(coordinate)
                new_coordinates_list.append(coordinate_int)

        return new_coordinates_list[0], new_coordinates_list[1]


class AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice100(
      AdjacencyMatrixTicTacToeAutomaticBuildDimensionChoice):
    """
    The tic-tac-toe game with customised dimensions which you can choose
    and the automatic gameplay.
    """

    # The coordinates_already_drawn is instantiated as an empty list.

    # coordinates_already_drawn: List[str] = []

    def __init__(self, dimensions_of_the_matrix):

        self.dimensions_of_the_matrix = dimensions_of_the_matrix
        self.matrix = np.array([])
        self.coordinates_matrix = dict()
        self.edges = []
        self.coordinates_already_drawn: List[str] = []

    def construct_matrix(self) -> ndarray:
        """
        The method construct_matrix overrides the method in the parent class.
        This method asks the player for the dimensions of the ndarray (therefore
        the dimensions of the tic-tac-toe grid) in a form an integer number.
        If the ValueError has taken place (the player hasn't typed in the integer
        with the base 10), the player is informed of the mistake and asked for
        the dimensions of the grid (matrix, numpy.ndarray) again. The
        chosen dimensions are plugged into the display_coordinates method, where
        the list of the coordinates is constructed. Then, that list
        is plugged into the display_coordinates_matrix method where it is
        converted into a view of the accessible coordinates in a form of the
        coordinates' matrix and printed at the beginning of the game. In the next
        step, an empty matrix in the form of numpy.ndarray of the chosen
        dimensions composed of zeros is created and plugged into the
        display_matrix method where it is converted and printed out in the neat
        format (without the numpy's brackets). The so-called matrix
        (the game's grid) is also constructed in a way which was borrowed from the
        method previously employed in the adding of the vertices to the adjacency
        matrix. That's a more complicated way of constructing an adjacency matrix
        composed of zeros than just creating the numpy.ndarray with the method
        numpy.zeros((dimensions_of_the_matrix, dimensions_of_the_matrix),
        dtype=int). For the dimension in range from 0 to the
        (dimensions_of_matrix - 1), if dimension == 0, the numpy.ndarray array [[0]]
        is created, for the greater values of vertices the matrix is
        updated with the column of zeros and the with the new row of zeros adjusted
        to the new length of the matrix. The matrix (or matrix,
        or the game's grid) is returned after construction.

        :param self: An instance of the class.
        :type self: An instance of the class
        :returns: A numpy.ndarray with the chosen dimensions (the game's grid)
        composed of zeros. Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
        :rtype: numpy.ndarray
        """

        try:

            dimension_of_matrix: int = int(self.dimensions_of_the_matrix)

            print(f"Dimensions of the matrix: "
                  f"{dimension_of_matrix} x {dimension_of_matrix} ")

            self.display_coordinates_matrix(self.display_coordinates(dimension_of_matrix))

            empty_matrix: ndarray = \
                np.zeros((dimension_of_matrix, dimension_of_matrix), dtype=int)

            self.display_matrix(empty_matrix)

            dimension: int

            for dimension in range(0, dimension_of_matrix):

                if dimension == 0:

                    self.matrix = np.zeros((1,), dtype=int)

                else:

                    add_row: ndarray = np.zeros((dimension + 1,), dtype=int)
                    add_column: ndarray = np.zeros((dimension,), dtype=int)
                    self.matrix = np.c_[self.matrix, add_column]
                    self.matrix = np.r_[self.matrix, [add_row]]

            return self.matrix

        except ValueError:

            print("You had ValueError. Please enter the integer with the base 10.")

            dimension_of_matrix: int = int(self.dimensions_of_the_matrix)

            print(f"Dimensions of the matrix:"
                  f" {dimension_of_matrix} x {dimension_of_matrix} ")

            self.display_coordinates_matrix(self.display_coordinates(dimension_of_matrix))

            empty_matrix = np.zeros((dimension_of_matrix, dimension_of_matrix), dtype=int)

            self.display_matrix(empty_matrix)

            for dimension in range(0, dimension_of_matrix):

                if dimension == 0:

                    self.matrix = np.zeros((1,), dtype=int)

                else:

                    add_row = np.zeros((dimension + 1,), dtype=int)
                    add_column = np.zeros((dimension,), dtype=int)
                    self.matrix = np.c_[self.matrix, add_column]
                    self.matrix = np.r_[self.matrix, [add_row]]

            return self.matrix

    def choose_the_random_coordinates(self) -> str:
        """
        Chooses pseudorandomly a pair of the coordinates from the list.
        Overrides the method in the parent class.
        :param self: An instance of the class.
        :type self: An instance of the class, an object.
        :returns: A string of the coordinates in the format "0 0".
        Example: "2 3".
        :rtype: str
        """

        coordinates_list: List[str] = []

        matrix_len: int = self.matrix_len()

        i: int

        for i in range(0, matrix_len):

            j: int

            for j in range(0, matrix_len):

                coordinates_list.append(f"{i} {j}")

        random_coordinate: str = \
            coordinates_list[randint(0, len(coordinates_list) - 1)]

        while random_coordinate in self.coordinates_already_drawn:
           random_coordinate = coordinates_list[randint(0, len(coordinates_list) - 1)]

        if random_coordinate not in self.coordinates_already_drawn:
            self.coordinates_already_drawn.append(random_coordinate)

        return random_coordinate


class Check:
    """
    Class for checking, if the data entered during choosing of the
    starting symbol and starting player are at least to some degree correct.
    """

    def check_if_choice_int(self, choice: [int, Any]) -> bool:
        """
        Checks if the choice is an instance of an integer.

        :param self: An instance of the class.
        :type self: An instance of the class.
        :param choice: An integer - 1 or 2. Example: 1.
        :type choice: int
        :returns: False if the choice is not an instance of an integer.
        Otherwise returns True. Example: True.
        :rtype: bool
        """

        if not isinstance(choice, int):

            return False

        return True

    def check_if_choice_in_range(self, choice: int) -> bool:
        """
        Checks if the choice is 1 or 2.
        Otherwise returns False.

        :param self: An instance of the class. An object.
        :type self: An instance of the class. An object.
        :param choice: An integer - 1 or 2. Example: 2.
        :type choice: int
        :returns: False if the choice is not 1 or 2.
        Otherwise returns True. Example: False.
        :rtype: bool
        """

        if choice not in [1, 2]:

            return False

        return True
