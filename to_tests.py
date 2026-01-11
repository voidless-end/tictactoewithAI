# File: to_tests.py: The file with the functions adapted fot the
# testing purposes.

import numpy as np
from random import randint
from typing import Tuple, List, Any, Dict
from numpy.core._multiarray_umath import ndarray


def check_if_coordinates_int(first_coordinate: int,
                             second_coordinate: int) -> bool:
    """
    Returns False if the first or the second coordinate is not an instance of
    an integer.
    Otherwise returns True.

    :param first_coordinate: The first coordinate of the pair.
    An integer ∈ <0, matrix.shape[0] - 1>. Example: 1.
    :type first_coordinate: int
    :param second_coordinate: The second coordinate of the pair.
    An integer ∈ <0, matrix.shape[0] - 1>. Example: 2.
    :type second_coordinate: int
    :returns: False if the first or the second coordinate is not an instance
     of an integer. Otherwise returns True. Example: False.
    :rtype: bool
    """

    if not isinstance(first_coordinate, int) or \
            not isinstance(second_coordinate, int):
        return False

    return True


def enter_the_coordinates(coordinates: str) -> Tuple[int, int]:
    """
    Prompts entering of the coordinates by the player in the form of the
    string of 2 integers separated by a single whitespace ("0 0").
    There, for the purpose of testing the coordinates are passed in the
    string form ("0 0") as the function's parameter. If the player will be
    unfortunate enough to spoil the coordinates at the beginning or/and at the
    end of the string with the accidental whitespaces and the other
    non-alphanumeric symbols an attempt will be made to unclutter the string.
    The string will be splitted into the list and the numerical identity of
    the i-th symbol of the list will be checked. Those positively tested will
    be returned as a tuple of 2 integers.

    :param coordinates: The coordinates in the form of 2 integers divided by a
    single whitespace ("0 0" form). Example: "1 1".
    :type coordinates: str
    :returns: A tuple of 2 integers processed from the raw string input.
    An integer in a pair may be ∈ <0, matrix.shape[0] - 1>.
    Example: (1, 1).
    :rtype: Tuple[int, int]
    """

    try:

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

        print("You had an IndexError. Try again.")

        coordinates = coordinates.strip()
        coordinates_list = coordinates.split(" ")

        new_coordinates_list = []

        for coordinate in coordinates_list:

            coordinate = coordinate.strip()

            if coordinate.isdigit():
                coordinate_int = int(coordinate)
                new_coordinates_list.append(coordinate_int)

        return new_coordinates_list[0], new_coordinates_list[1]


def construct_matrix(dimensions_of_matrix: int) -> ndarray:
    """
    The method asks the player for the dimensions of matrix (therefore the
    dimensions of the tic-tac-toe grid) in a form an integer number. There,
    for the purpose of testing the dimensions_of_matrix are passed in as
    the parameter. If the ValueError has taken place (the player hasn't typed
    in the integer with the base 10), the player is informed of the mistake and
    asked for the dimensions of the grid (matrix) again. The chosen dimensions
    are plugged into the display_coordinates method, where the list of the
    coordinates is constructed. Then, that list is plugged into the
    display_coordinates_matrix method, where it is converted into a view of
    the accessible coordinates in a form of the coordinates' matrix and
    printed at the beginning of the game. In the next step, an empty matrix in
    the form of numpy.ndarray of the chosen dimensions composed of zeros is
    created and plugged into the display_matrix method where it is converted
    and printed out in the neat format (without the numpy's brackets).
    The so-called matrix (the game's grid) numpy.ndarray is also
    constructed in a way which was borrowed from the method previously
    employed in the adding of the vertices to the adjacency matrix.
    That's a more complicated way of constructing an initial adjacency matrix
    composed of zeros than just creating the numpy.ndarray with the method
    numpy.zeros((dimensions_of_the_matrix, dimensions_of_the_matrix),
    dtype=int). For the dimension in the range ∈ <0, (dimensions_of_matrix - 1)>,
    if dimension == 0, the 2D numpy.ndarray array [[0]] is created, for the greater
    values of vertices the matrix numpy.ndarray is updated with the
    column of zeros and then with the row of zeros adjusted to the new length
    of the matrix. The matrix numpy.ndarray (or matrix, or the
    game's grid) composed of zeros is returned after the construction.

    :param dimensions_of_matrix: The one of the matrix's dimensions.
    Example: 4.
    :type dimensions_of_matrix: int
    :returns: A numpy ndarray - the initial matrix with the chosen dimensions
     passed in (the game's grid) composed of zeros.
     Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
    :rtype: numpy.ndarray
    """

    try:

        dimension: int

        for dimension in range(0, dimensions_of_matrix):

            if dimension == 0:

                matrix: ndarray = np.zeros((1,), dtype=int)

            else:

                add_row: ndarray = np.zeros((dimension + 1,), dtype=int)
                add_column: ndarray = np.zeros((dimension,), dtype=int)
                matrix = np.c_[matrix, add_column]
                matrix = np.r_[matrix, [add_row]]

        return matrix

    except ValueError:

        print("You had ValueError. Please enter the integer with the base 10.")

        for dimension in range(0, dimensions_of_matrix):

            if dimension == 0:

                matrix = np.zeros((1,), dtype=int)

            else:

                add_row = np.zeros((dimension + 1,), dtype=int)
                add_column = np.zeros((dimension,), dtype=int)
                matrix = np.c_[matrix, add_column]
                matrix = np.r_[matrix, [add_row]]

        return matrix


def check_if_coordinates_in_range(first_coordinate: int,
                                  second_coordinate: int,
                                  matrix: ndarray) -> bool:
    """
    Returns False if the first or the second coordinate
    ∉ <0, matrix.shape[0] - 1>.
    Otherwise returns True.

    :param first_coordinate: The first coordinate of the pair.
    An integer ∈ <0, matrix.shape[0] - 1>. Example: 2.
    :type first_coordinate: int
    :param second_coordinate: The second coordinate of the pair.
    An integer ∈ <0, matrix.shape[0] - 1>. Example: 3.
    :type second_coordinate: int
    :param matrix: The numpy.ndarray passed in to extract from it
     its dimensions. Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
    :type matrix: numpy.ndarray
    :returns: False if the first or the second coordinate
    ∉ <0, matrix.shape[0] - 1>. Otherwise returns True. Example:
    True.
    :rtype: bool
    """

    coordinates_range_list: List[int] = list(range(0, matrix.shape[0]))

    if first_coordinate not in coordinates_range_list \
            or second_coordinate not in coordinates_range_list:
        return False

    return True


def check_if_cell_occupied(
        first_coordinate: int,
        second_coordinate: int,
        matrix: ndarray) -> bool:
    """
    Returns False if the numpy.ndarray (matrix) under the
    (first_coordinate, second_coordinate) key is not empty (has other value
    than 0). Otherwise returns True.

    :param first_coordinate: The first coordinate of the pair
    (first part of the key). An integer
    ∈ <0, matrix.shape[0]-1>. Example: 3.
    :type first_coordinate: int
    :param second_coordinate: The second coordinate of the pair
    (second part of the key). An integer
    ∈ <0, matrix.shape[0]-1>. Example: 2.
    :type second_coordinate: int
    :param matrix: The numpy.ndarray passed in to check if the
    cell with the chosen coordinates passed in is empty (equals 0).
    Example: [[0, 0, 0], [2, 1, 0], [0, 0, 0]].
    :type matrix: numpy.ndarray
    :returns: False if numpy.ndarray value under the key (first_coordinate,
    second_coordinate) is not empty (is not a 0). Otherwise returns True.
    Example: False.
    :rtype: bool
    """

    try:

        if matrix[(first_coordinate, second_coordinate)] != 0:
            return False

        return True

    except IndexError:

        return False


def add_1(
        pair: Tuple[int, int],
        matrix: ndarray) -> ndarray:
    """
    The method for adding the "edges", that is, the method for entering
    1 (replacement for "X" or "O") under the key of passed-in 2-integer tuple
    in the matrix (the game's grid).
    Indexes from 0.

    :param pair: A tuple of 2 integers.
    An integer ∈ <0, matrix.shape[0] - 1>. Example: (0, 2).
    :type pair: Tuple[int, int]
    :param matrix: The numpy.ndarray (the game's grid) passed in
    to enter in it a new 1.
    Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
    :type matrix: numpy.ndarray
    :returns: A numpy.ndarray with the newly positioned 1
    under a key of the passed-in 2-integer tuple.
    Example: [[0, 0, 0], [0, 0, 0], [0, 1, 0]].
    :rtype: numpy.ndarray
    """

    matrix[pair] = 1

    return matrix


def add_2(
        pair: Tuple[int, int],
        matrix: ndarray) -> ndarray:
    """
    The method for adding the "edges", that is, the method for entering
    2 (replacement for "X" or "O") under the key of passed-in pair
    in the matrix (the game's grid).
    Indexes from 0.

    :param pair: The tuple of 2 integers.
    An integer ∈ <0, matrix.shape[0] - 1>. ExampleL (3, 4).
    :type pair: Tuple[int, int]
    :param matrix: The numpy.ndarray (the game's grid) passed in
    to enter in it a new 2. Example: [[0, 0, 0], [0, 0, 0], [0, 1, 0]].
    :type matrix: numpy.ndarray
    :returns: A numpy.ndarray with a newly positioned 2
    under a key of the passed-in pair 2-integer tuple.
    Example: [[0, 2, 0], [0, 0, 0], [0, 1, 0]].
    :rtype: numpy.ndarray
    """
    matrix[pair] = 2

    return matrix


def display_adjacency_matrix() -> None:
    """
    The method for displaying an adjacency matrix without the square brackets.

    :returns: Prints the matrix, returns None. Example: None.
    :rtype: None
    """

    s: str = str(construct_matrix(randint(3, 100)))
    s: str = s.replace('[', '')
    s: str = s.replace(']', '')
    s: str = ' ' + s

    print(s)


def display_matrix(matrix: ndarray) -> None:
    """
    The method for displaying a matrix without the square brackets.

    :param matrix: The passed-in numpy.ndarray.
    Example: [[0, 0, 0], [0, 0, 0], [0, 1, 0]].
    :type matrix: numpy.ndarray
    :return: It prints the matrix without the square brackets.
    Returns None. Example: None.
    :rtype: None
    """
    line: str = "-" * 2 * matrix.shape[0]
    line: str = line + "-"
    print(line)

    s: str = str(matrix)
    s: str = s.replace('[', '')
    s: str = s.replace(']', '')
    s: str = ' ' + s

    print(s)


def display_coordinates_matrix(matrix: List[str]) -> None:
    """
    The method for displaying the coordinates' matrix without the
    square brackets.

    :param matrix: The list of the coordinates of the matrix.
    Example: ['(0,0)(0,1)(0,2),(0,3)','(1,1)(1,1)(1,2),(1,3)',
               '(2,0)(2,1)(2,2),(2,3)','(3,0)(3,1)(3,2),(3,3)'].
    :type matrix: List[str]
    :return: It prints the matrix without the square brackets. Returns None.
    Example: None.
    :rtype: None
    """

    print("The coordinates of the cells: ")

    cooordinates_row: str

    for cooordinates_row in matrix:
        s: str = str(cooordinates_row)
        s: str = s.replace('[', '')
        s: str = s.replace(']', '')

        print(f"{s}")


def display_coordinates(new_matrix_len: int) -> List[str]:
    """
    Having passed in the one of the dimensions of the matrix (new_matrix_len),
    it returns the list of the coordinates available in the matrix
    (numpy.ndarray).

    :param new_matrix_len: The horizontal dimension of the matrix.
    Example: 3.
    :type new_matrix_len: int
    :returns: The list of the coordinates available in the matrix
    (numpy.ndarray). Example: ['(0,0)(0,1)(0,2),(0,3)','(1,1)(1,1)(1,2),(1,3)',
                               '(2,0)(2,1)(2,2),(2,3)','(3,0)(3,1)(3,2),(3,3)'].
    :rtype: List[str]
    """

    len_matrix: int = new_matrix_len

    index_list: List[int] = list(range(0, len_matrix))

    coordinates_matrix: Dict[Tuple[int, int], str] = dict()

    bigger_list: List[str] = []

    index: int

    for index in index_list:

        new_list: List[str] = []

        i: int

        for i in range(0, len_matrix):
            coordinates_matrix[(index, i)] = f"({index},{i})"
            new_list.append(coordinates_matrix[(index, i)])
            new: str = ''.join(new_list)

        bigger_list.append(new)

    return bigger_list


def enter_the_coordinates_for_1_and_check_them(
        coordinates: str,
        matrix: ndarray) -> ndarray:
    """
    The player is prompted to enter the coordinates in the form of 2 integers
    divided by a single whitespace ("0 0" form). There, for the testing
    purposes, the coordinates are passed into the function as the parameter in
    the same raw string form. The coordinates are preprocessed into a tuple of
    2 integers (all done by the method enter_the_coordinates) and delegated
    to their own variables (first_coordinate, second_coordinate). The integer
    identity of the both variables is checked by the method
    check_if_coordinates_int. Finally, if the cell is empty
    (or equals to 0), the new 1 is positioned in the matrix according to the
    coordinates passed into the method add_1. The new matrix (numpy.ndarray)
    is displayed by the method display_matrix and returned.

    :param coordinates: The raw string of the coordinates passed in (the "0 0"
    form). Example: "3 2".
    :type coordinates: str
    :param matrix: The numpy.ndarray passed in for entering 1 in it.
    Example: [[0, 2, 0], [0, 0, 0], [0, 1, 0]].
    :type matrix: numpy.ndarray
    :returns: The matrix (numpy.ndarray) with the newly positioned 1 according
     to the coordinates passed in to the function.
     Example: [[0, 2, 0], [0, 1, 0], [0, 1, 0]].
    :rtype: numpy.ndarray
    """
    coordinates_tuple: Tuple[int, int] = enter_the_coordinates(coordinates)

    first_coordinate: int = coordinates_tuple[0]
    second_coordinate: int = coordinates_tuple[1]

    while not check_if_coordinates_int(first_coordinate, second_coordinate):
        print("The coordinates must be integer numbers!!")

        first_coordinate, second_coordinate = enter_the_coordinates(coordinates)

    while not check_if_coordinates_in_range(
            first_coordinate, second_coordinate, matrix):
        print(f"The coordinates must be in range <0, "
              f"{matrix.shape[0] - 1}>")

        first_coordinate, second_coordinate = enter_the_coordinates(coordinates)

    while not check_if_cell_occupied(
            first_coordinate, second_coordinate, matrix):
        print("This cell is occupied. Choose another one!")

        first_coordinate, second_coordinate = enter_the_coordinates(coordinates)

    if check_if_cell_occupied(first_coordinate, second_coordinate, matrix):
        matrix_with_new_1: ndarray = add_1(
            (first_coordinate, second_coordinate), matrix)

        return matrix_with_new_1


def enter_the_coordinates_for_2_and_check_them(
        coordinates: str,
        matrix: ndarray) -> ndarray:
    """
    The player is prompted to enter the coordinates in the form of 2 integers
    divided by a single whitespace ("0 0" form). There, for the testing
    purposes, the coordinates are passed into the function as the parameter in
    the same raw string form. The coordinates are preprocessed into a tuple of
    2 integers (all done by the enter_the_coordinates method) and delegated to
    their own variables (first_coordinate, second_coordinate). The integer
    identity of the both variables is checked by the method
    check_if_coordinates_int. If the one or two of them are not integers, the
    player is informed of it and prompted to enter the coordinates again.
    Then, the both coordinates are checked if they are in the bounds of the
    ranges of the coordinates set by the shape of the matrix (or the
    matrix or the game's grid). If one or both of the coordinates are out of
    the bounds, then the player is informed of it (altogether with displaying
    the correct range), and prompted for entering  the coordinates again. If
    the cell is already occupied, the player is informed of it and prompted
    to enter the coordinates once again. Finally, if the cell is empty (or
    equals to 0), the new 2 is positioned in the matrix according to the
    coordinates passed into the method add_2. The new matrix
    (numpy.ndarray) is displayed by the method display_matrix and returned.

    :param coordinates: The raw string of the coordinates passed in (the "0 0"
    form). Example: "4 4".
    :type coordinates: str
    :param matrix: The numpy.ndarray passed in for entering 1 in it.
    Example: [[0, 2, 0], [0, 0, 0], [0, 1, 0]].
    :type matrix: numpy.ndarray
    :returns: The matrix (numpy.ndarray) with the newly positioned 2 according
    to the coordinates passed in by the player.
    Example: [[0, 2, 0], [0, 0, 2], [0, 1, 0]].
    :rtype: numpy.ndarray
    """

    coordinates_tuple: Tuple[int, int] = enter_the_coordinates(coordinates)

    first_coordinate: int = coordinates_tuple[0]
    second_coordinate: int = coordinates_tuple[1]

    while not check_if_coordinates_int(first_coordinate, second_coordinate):
        print("The coordinates must be integer numbers!!")
        first_coordinate, second_coordinate = enter_the_coordinates(coordinates)

    while not check_if_coordinates_in_range(
            first_coordinate, second_coordinate, matrix):
        print(f"The coordinates must be in range <0,"
              f" {matrix.shape[0] - 1}>.")

        first_coordinate, second_coordinate = enter_the_coordinates(coordinates)

    while not check_if_cell_occupied(
            first_coordinate, second_coordinate, matrix):
        print("This cell is occupied. Choose another one!")

        first_coordinate, second_coordinate = enter_the_coordinates(coordinates)

    if check_if_cell_occupied(first_coordinate, second_coordinate, matrix):
        matrix_with_new_2: ndarray = add_2(
            (first_coordinate, second_coordinate), matrix)

        return matrix_with_new_2


def diagonal_win(matrix: ndarray) -> bool:
    """
    Evaluates the passed-in numpy.ndarray (the matrix matrix) for the
    possibility of the diagonal win. In the event of the diagonal
    win constitution of the passed-in matrix - returns True. Otherwise
    - returns False.

    :param matrix: A numpy.ndarray passed in for the evaluation of the
    possibility of the diagonal win constitution, a numpy.ndarray.
    Example: [[0, 2, 2], [0, 0, 2], [0, 1, 1]].
    :type matrix: numpy.ndarray
    :returns: True, if the passed-in numpy.ndarray has the constitution of the
    diagonal win. Otherwise - returns False. Example: True.
    :rtype: bool
    """

    # The three empty lists are initialized every time the new matrix
    # is passed in.

    diagonal_win_1_coordinates_list: List[Tuple[int, int]] = []
    diagonal_win_1_boolean_list: List[bool] = []
    diagonal_win_2_boolean_list: List[bool] = []

    # The horizontal dimension is extracted from the numpy.ndarray passed in
    # by accessing it's shape property.

    len_matrix: int = matrix.shape[0]

    # The diagonal_win_1_list is populated with the constellation of
    # the coordinates which, when their values are equal to 1 or to 2 and
    # equal to one another in the diagonal axis, are the 1st diagonal winning
    # set of the coordinates out of 2 possible.

    i: int

    for i in range(0, len_matrix):
        j: int = len_matrix - i - 1
        diagonal_win_1_coordinates_list.append((i, j))

    # For the range of the diagonal coordinates, if the 2 consecutive
    # values from the 2 consecutive diagonal coordinates in the
    # passed-in numpy.ndarray are equal and different from 0, to the
    # diagonal_win_1_boolean_list the boolean True value is appended.
    # If the same consecutive diagonal coordinates' values in the
    # numpy.ndarray are different from each other, the False is appended
    # to the diagonal_win_1_boolean_list list.

    win_coordinates: int

    for win_coordinates in range(len(diagonal_win_1_coordinates_list) - 1):

        if matrix[diagonal_win_1_coordinates_list[win_coordinates]] \
                == matrix[diagonal_win_1_coordinates_list[win_coordinates + 1]] != 0:

            diagonal_win_1_boolean_list.append(True)

        elif matrix[diagonal_win_1_coordinates_list[win_coordinates]] \
                != matrix[diagonal_win_1_coordinates_list[win_coordinates + 1]]:

            diagonal_win_1_boolean_list.append(False)

    # The second diagonal constitution of the consecutive coordinates
    # is easier to extract, so there's no prepopulated list with the
    # coordinates to check. The coordinates in this constitution have the
    # pattern (i, i), where i is an integer ∈ <0, len_matrix-1>. When
    # the two consecutive values of numpy.ndarray of the diagonal coordinates
    # (i, i) and (i + 1, i + 1) are equal and different from 0, the boolean
    # True is appended to the diagonal_win_2_boolean_list list. If the same
    # pair of values are different from each other, the boolean False is
    # appended to the diagonal_win_2_boolean_list list.

    for i in range(0, len_matrix - 1):

        if matrix[(i, i)] == matrix[(i + 1, i + 1)] != 0:

            diagonal_win_2_boolean_list.append(True)

        elif matrix[(i, i)] != matrix[(i + 1, i + 1)]:

            diagonal_win_2_boolean_list.append(False)

    # The truthy_list is instantiated as an empty list.

    truthy_list: List[bool] = []

    # If the diagonal_win_1_boolean_list list is not empty (therefore
    # it evaluates to the boolean True), the aforementioned list
    # is checked if the boolean False is in it. If False is in
    # diagonal_win_1_boolean_list list, the boolean False is appended
    # to the truthy_list. If False is not in diagonal_win_1_boolean_list list,
    # the boolean True is appended to the truthy_list. If
    # diagonal_win_1_boolean_list list is empty (therefore it
    # evaluates to False), the boolean False is appended to the
    # the truthy_list. The same type of checking is performed with
    # the diagonal_win_2_boolean_list.

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


def vertical_and_horizontal_win(matrix: ndarray) -> bool:
    """
    Evaluates the passed-in numpy.ndarray (the matrix matrix) for the
    the possibility of the vertical or horizontal win. In the
    event of the horizontal or vertical win constitution of the passed-in
    matrix - the True is returned. Otherwise - it returns False.

    :param matrix: A numpy.ndarray passed in for evaluation.
    Example: [[0, 2, 2], [0, 0, 2], [0, 1, 1]].
    :type matrix: numpy.ndarray
    :returns: True if the horizontal or vertical "win" constitution is
    detected. Otherwise it returns False. Example: True.
    :rtype: bool
    """

    # The horizontal_boolean_dict and the vertical_boolean_dict are
    # initialized as the empty dictionaries.

    horizontal_boolean_dict: Dict[str, List[bool]] = dict()
    vertical_boolean_dict: Dict[str, List[bool]] = dict()

    # The horizontal dimension (the one of the numpy.ndarray's equal
    # dimensions) is extracted by accessing the 0th item of the tuple
    # returned as the shape of the matrix.

    len_matrix: int = matrix.shape[0]

    # For the range of numbers from 0 to (len_matrix-1) (the vertical or the
    # horizontal indices of the matrix numpy.ndarray or the game's
    # grid), the horizontal_boolean_dict is populated by the empty lists with the
    # keys of the pattern "horizontal_boolean_list_{j}", where {j} is the
    # grid's horizontal index. The vertical_boolean_dict is also populated by the
    # empty lists with the keys of the pattern "vertical_boolean_list_{j}",
    # where {j} is the index (vertical).

    j: int

    for j in range(0, len_matrix):
        horizontal_boolean_dict[f"horizontal_boolean_list_{j}"] = []
        vertical_boolean_dict[f"vertical_boolean_list_{j}"] = []

    # The index_list is instantiated as the list of integers,
    # where integer ∈ <0, len_matrix-1>.

    index_list: List[int] = list(range(0, len_matrix))

    # For the each index in index_list the new loop is instantiated.
    # In that loop, the index is held constant up until the next range of
    # indices (i) , where i ∈ <0, len_matrix-1>, won't be checked for the
    # condition of equality of the consecutive numpy.ndarray values (and not
    # being 0 at the same time) under the keys of the consecutive coordinates
    # (index, i) and (index, i + 1) in the same row. If that condition is
    # fulfilled, the boolean True is appended to the list in the
    # horizontal_boolean_dict under the key of "horizontal_boolean_list_{index}"
    # where {index} is the horizontal index. If the values of the consecutive
    # horizontal cells are not equal, the boolean False is appended to that
    # list under the same key value of the horizontal_boolean_dict.

    # Here index is the horizontal index.

    index: int

    for index in index_list:

        # i: the vertical index.

        i: int

        for i in range(0, len_matrix - 1):

            if matrix[(index, i)] == matrix[(index, i + 1)] != 0 \
                    and ((matrix[(index, i)] == matrix[(index, i + 1)] == 1)
                         or (matrix[(index, i)] == matrix[(index, i + 1)] == 2)):

                horizontal_boolean_dict[f"horizontal_boolean_list_{index}"].append(True)

            elif matrix[(index, i)] != matrix[(index, i + 1)]:

                horizontal_boolean_dict[f"horizontal_boolean_list_{index}"].append(False)

    # For the each index in index_list the new loop is instantiated.
    # In that loop, the index is held constant up until the next range of
    # indices (i), where i ∈ <0, len_matrix-1>, won't be checked for the
    # condition of equality of the consecutive numpy.ndarray values (and
    # not being 0 at the same time) under the keys of the corresponding
    # consecutive coordinates: (i, index) and (i + 1, index) in the same
    # column. If that condition is fulfilled, the boolean True is appended
    # to the list in the vertical_boolean_dict under the key of
    # "vertical_boolean_list_{index}" where {index} is the vertical index.
    # If the values of the consecutive vertical cells are not equal,
    # the boolean False is appended to that list under the same key value
    # of the vertical_boolean_dict.

    # Here index is the vertical index.

    for index in index_list:

        # i: the horizontal index

        for i in range(0, len_matrix - 1):

            if matrix[(i, index)] == matrix[(i + 1, index)] != 0 \
                    and ((matrix[(i, index)] == matrix[(i + 1, index)] == 1)
                         or (matrix[(i, index)] == matrix[(i + 1, index)] == 2)):

                vertical_boolean_dict[f"vertical_boolean_list_{index}"].append(True)

            elif matrix[(i, index)] != matrix[(i + 1, index)]:

                vertical_boolean_dict[f"vertical_boolean_list_{index}"].append(False)

    # The win_vertically_boolean_list is instantiated as an empty list.

    win_vertically_boolean_list: List[bool] = []

    # For each index in the index_list, if the list under the key
    # "vertical_boolean_list_{index}" in the vertical_boolean_dict dictionary is
    # not empty (and therefore evaluates to True), if False is in the list,
    # the boolean False is appended to the win_vertically_boolean_list list.
    # If False is not in the aforementioned list, the boolean True is appended
    # to the win_vertically_boolean_list list. If the
    # vertical_boolean_dict[f"vertical_boolean_list_{index}"] list is empty (or
    # evaluates to False), False is appended to win_vertically_boolean_list
    # list.

    for index in index_list:

        if vertical_boolean_dict[f"vertical_boolean_list_{index}"]:

            if False in vertical_boolean_dict[f"vertical_boolean_list_{index}"]:

                win_vertically_boolean_list.append(False)

            elif False not in vertical_boolean_dict[f"vertical_boolean_list_{index}"]:

                win_vertically_boolean_list.append(True)

        win_vertically_boolean_list.append(False)

    # The win_horizontally_list is instantiated as an empty list.

    win_horizontally_boolean_list: List[bool] = []

    # For each index in the index_list, if the list under the key
    # "horizontal_boolean_list_{index}" in the horizontal_boolean_dict dictionary
    # is not empty (and therefore evaluates to True), if False is in the list,
    # the boolean False is appended to win_horizontally_boolean_list list. If
    # False is not in the aforementioned list, the boolean True is appended to
    # the win_horizontally_boolean_list list. If the
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

    # The truthy list is instantiated as an empty list.

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


def draw(matrix: ndarray) -> bool:
    """
    Evaluates the passed-in numpy.ndarray (the matrix) for
    the possibility of the draw. In the event of the constitution of cells
    of the passed-in matrix suggesting a draw - the method
    return the boolean True. Otherwise - it returns the boolean False.

    :param matrix: A numpy.ndarray passed in for the evaluation.
    Example: [[0, 2, 2], [0, 0, 2], [0, 1, 1]].
    :type matrix: numpy.ndarray
    :return: True if there is a draw, False otherwise. Example: False.
    :rtype: bool
    """

    # The horizontal dimension is extracted from the numpy.ndarray's
    # (matrix) shape property.

    len_matrix: int = matrix.shape[0]

    # The index_list is instantiated as the list of
    # integers, where integer ∈ <0, len_matrix-1>.

    index_list: List[int] = list(range(0, len_matrix))

    # The truthy_list is instantiated as an empty list.

    truthy_list: List[bool] = []

    # All the matrix cells are checked for its value. If the value of
    # the cell is different from 0, the boolean True is appended to the
    # truthy_list list. If the value of the cell equals 0, the boolean
    # False is appended to the truthy_list list.

    index: int

    for index in index_list:

        i: int

        for i in range(0, len_matrix):

            if matrix[(index, i)] != 0:

                truthy_list.append(True)

            elif matrix[(index, i)] == 0:

                truthy_list.append(False)

    # If False is in the truthy_list list, the method returns boolean
    # False. If False is not in the truthy_list list and calling in the
    # methods diagonal_win and vertical_and_horizontal_win with the
    # numpy.ndarray (matrix) passed in returns False in both cases,
    # the method returns boolean True.

    if False in truthy_list:

        return False

    elif False not in truthy_list and ((not diagonal_win(matrix))
                                       and (not vertical_and_horizontal_win(matrix))):

        return True


def check_if_choice_int(choice: [int, Any]) -> bool:
    """
    Checks if the choice is an instance of an integer.

    :param choice: An integer - 1 or 2. Example: 1.
    :type choice: int
    :returns: False if the choice is not an instance of an integer.
    Otherwise returns True. Example: True.
    :rtype: bool
    """

    if not isinstance(choice, int):
        return False

    return True


def check_if_choice_in_range(choice: int) -> bool:
    """
    Checks if the choice is 1 or 2.
    Otherwise returns False.

    :param choice: An integer - 1 or 2. Example: 2.
    :type choice: int
    :returns: False if the choice is not 1 or 2.
    Otherwise returns True. Example: False.
    :rtype: bool
    """

    if choice not in [1, 2]:
        return False

    return True


def matrix_len(matrix: ndarray) -> int:
    """
    Extracts the horizontal dimension from the passed-in numpy.ndarray.

    :param matrix: The passed-in numpy.ndarray from which the
    horizontal dimension will be extracted.
    Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0]].
    :type matrix: numpy.ndarray
    :returns: The horizontal dimension of the passed-in numpy.ndarray.
    :rtype: int
    """

    len_matrix: int = matrix.shape[0]

    return len_matrix


def construct_adjacency_matrix(number_of_vertices: int) -> ndarray:
    """
    The original function allowing for the construction the adjacency matrix.
    Takes in the number of vertices from which the adjacency matrix is
    composed and returns the adjacency matrix composed of zeros with the
    number of vertices passed in the function (number_of_vertices).

    :param number_of_vertices: The number of vertices. From that information
    the initial adjacency matrix (composed of zeros) will be created.
    Example: 4.
    :type number_of_vertices: int
    :returns: The initial adjacency matrix (composed of zeros) with the number
    of vertices passed in the method.
    Example: [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0], [[0, 0, 0, 0, 0]].
    :rtype: numpy.ndarray
    """

    vertex: int

    for vertex in range(0, number_of_vertices + 1):

        if vertex == 0:

            adjacency_matrix: ndarray = np.zeros((1,), dtype=int)

        else:

            add_row: ndarray = np.zeros((vertex + 1,), dtype=int)
            add_column: ndarray = np.zeros((vertex,), dtype=int)
            adjacency_matrix = np.c_[adjacency_matrix, add_column]
            adjacency_matrix = np.r_[adjacency_matrix, [add_row]]

    return adjacency_matrix
