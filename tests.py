# File tests.py


import unittest
from random import randint
from typing import List, Tuple, Any, Union

import numpy as np
from numpy.core._multiarray_umath import ndarray

from to_tests import (check_if_coordinates_int,
                      enter_the_coordinates,
                      construct_matrix,
                      check_if_coordinates_in_range,
                      check_if_cell_occupied,
                      add_1,
                      add_2,
                      display_coordinates,
                      enter_the_coordinates_for_1_and_check_them,
                      enter_the_coordinates_for_2_and_check_them,
                      diagonal_win,
                      vertical_and_horizontal_win,
                      draw,
                      check_if_choice_int,
                      check_if_choice_in_range,
                      matrix_len,
                      construct_adjacency_matrix)


class MyTest(unittest.TestCase):

    def test_enter_the_coordinates(self):
        """
        Tests if the given i-th string combination of digits ∈ <1, 3>
        separated by a whitespace in the list give the corresponding i-th tuple of
        2 integers in the second list after being subjected to the action of the
        tested function (enter_the_coordinates). It also checks if the function
        strips the strings from the whitespaces correctly.
        """

        coordinates_string_test: List[str] = [
            '1 1', '2 2',
            ' 2 3', '3 3',
            '2 3', ' 2 1 '
        ]

        coordinates_return: List[Tuple[int, int]] = [
            (1, 1), (2, 2),
            (2, 3), (3, 3),
            (2, 3), (2, 1)
        ]

        i: int

        for i in range(len(coordinates_string_test)):
            self.assertEqual(enter_the_coordinates(coordinates_string_test[i]),
                             coordinates_return[i])

    def test_check_if_coordinates_int_assert_true(self):
        """
        Asserts that the function (check_if_coordinates_int) -
        checking if the symbol passed in is an instance of an integer
        - returns True on receiving pairs of digits in the strings.
        """

        coordinates: List[str] = [
            "2 3",
            "3 3",
            "3 3",
            "1 1",
            "1 1",
            "2 1",
            "2 2",
            "2 1",
            "3 1",
            "3 1",
            "1 2"
        ]

        coordinate: str

        for coordinate in coordinates:
            self.assertTrue(
                check_if_coordinates_int(
                    *enter_the_coordinates(coordinate)))

    def test_check_if_coordinates_int_assert_false(self):
        """
        Asserts that's the function (check_if_coordinates_int)
        - checking if the symbol passed in is an instance of an integer
        - returns False on receiving an instance of the non-integer or the
        non-digit in a pair.

        :returns: None
        :rtype: None
        """

        coordinates: List[Union[Tuple[float, int], Tuple[str, str], Tuple[int, float],
                                Tuple[float, float]]] = [
            (2.0, 3),
            ("two", "3"),
            ('3', "two"),
            ('three', 'three'),
            (1, 1.0),
            (2.3, 1.0),
            ("half", "big")
        ]

        coordinate: Union[Tuple[float, int], Tuple[str, str], Tuple[int, float],
                          Tuple[float, float]]

        for coordinate in coordinates:
            self.assertFalse(check_if_coordinates_int(*coordinate))

    def test_construct_matrix(self):
        """
        Asserts that the numpy.ndarray constructed by the function
        construct_matrix having passed in the pseudorandomly drawn integer
        (from 1 to 100) is equal to the numpy.ndarray constructed by the method
        numpy.zeros, where the same pseudorandomly drawn integer is passed in as
        the numpy.ndarray dimensions. The numbers are drawn 10 times.

        :return: None
        :rtype: None
        """

        i: int

        for i in range(10):
            random_dimensions: int = randint(1, 100)

            empty_matrix: ndarray = np.zeros((random_dimensions, random_dimensions),
                                             dtype=int)

            self.assertEqual(construct_matrix(random_dimensions).all(), empty_matrix.all())

    def test_check_if_coordinates_in_range_assert_true(self):
        """
        It chooses the dimensions of the numpy.ndarray pseudorandomly (from
        the integers ∈ <1, 100>, the random_dimension variable). It constructs the
        matrix (numpy.ndarray) by passing in the chosen dimensions to the method
        numpy.zeros. It chooses pseudorandomly 2 coordinates (in the range of
        ∈ <0, random_dimensions - 1>) and checks if those coordinates are in range
        of the coordinates of the previously constructed numpy.ndarray by passing
        them into the function check_if_coordinates_in_range altogether with the
        previously constructed numpy.ndarray.
        """

        i: int

        for i in range(1, randint(2, 100)):
            random_dimensions: int = randint(1, 100)

            empty_matrix: ndarray = np.zeros((random_dimensions, random_dimensions),
                                             dtype=int)

            first_coordinate: int = randint(0, random_dimensions - 1)
            second_coordinate: int = randint(0, random_dimensions - 1)

            self.assertTrue(check_if_coordinates_in_range(first_coordinate,
                                                          second_coordinate,
                                                          empty_matrix))

    def test_check_if_coordinates_in_range_assert_false_both(self):
        """
        It chooses the dimensions of the numpy.ndarray pseudorandomly (from
        the integers ∈ <1, 100>, the random_dimension variable). It constructs the
        matrix (numpy.ndarray) by passing in the chosen dimensions to the method
        numpy.zeros. It chooses pseudorandomly 2 coordinates (in the range of
        ∈ <random_dimensions, 101>) and asserts the the function tested
        (check_if_coordinates_in_range) returns False on receiving those
        coordinates (that are certainly not in the range of the coordinates of
        the previously constructed numpy.ndarray) altogether with the constructed
        numpy.ndarray. The (pseudo)random number of tests is conducted - from 2 to
        99.
        """

        i: int

        for i in range(1, randint(2, 100)):
            random_dimensions: int = randint(1, 100)

            empty_matrix: ndarray = np.zeros((random_dimensions, random_dimensions),
                                             dtype=int)

            first_coordinate: int = randint(random_dimensions, 101)
            second_coordinate: int = randint(random_dimensions, 101)

            self.assertFalse(check_if_coordinates_in_range(first_coordinate,
                                                           second_coordinate,
                                                           empty_matrix))

    def test_check_if_coordinates_in_range_assert_false_first(self):
        """
        It chooses the dimensions of the numpy.ndarray pseudorandomly (from
        the integers ∈ <1, 100>, the random_dimension variable). It constructs the
        matrix (numpy.ndarray) by passing in the chosen dimensions to the method
        numpy.zeros. It chooses pseudorandomly 2 coordinates (first
        ∈ <0, random_dimensions - 1> and the second ∈ <random_dimensions, 101>)
        and asserts the the function tested (check_if_coordinates_in_range)
        returns False on receiving those coordinates (one of them is certainly not
        in the range of the coordinates of the previously constructed
        numpy.ndarray) altogether with the constructed numpy.ndarray.
        The (pseudo)random number of tests is conducted - from 2 to 99.
        """

        i: int

        for i in range(1, randint(2, 100)):
            random_dimensions: int = randint(1, 100)

            empty_matrix: ndarray = np.zeros((random_dimensions, random_dimensions),
                                             dtype=int)

            first_coordinate: int = randint(0, random_dimensions - 1)
            second_coordinate: int = randint(random_dimensions, 101)

            self.assertFalse(check_if_coordinates_in_range(first_coordinate,
                                                           second_coordinate,
                                                           empty_matrix))

    def test_check_if_coordinates_in_range_assert_false_second(self):
        """
        It chooses the dimensions of the numpy.ndarray pseudorandomly (from
        the integers ∈ <1, 100>, the random_dimension variable). It constructs the
        matrix (numpy.ndarray) by passing in the chosen dimensions to the method
        numpy.zeros. It chooses pseudorandomly 2 coordinates (first
        ∈ <random_dimensions, 101> and the second ∈ <0, random_dimensions - 1>)
        and asserts the the function tested (check_if_coordinates_in_range)
        returns False on receiving those coordinates (one of them is certainly not
        in the range of the coordinates of the previously constructed
        numpy.ndarray) altogether with the constructed numpy.ndarray. The
        (pseudo)random number of tests is conducted - from 2 to 99.
        """

        i: int

        for i in range(1, randint(2, 100)):
            random_dimensions: int = randint(1, 100)

            empty_matrix: ndarray = np.zeros((random_dimensions, random_dimensions),
                                             dtype=int)

            first_coordinate: int = randint(random_dimensions, 101)
            second_coordinate: int = randint(0, random_dimensions - 1)

            self.assertFalse(check_if_coordinates_in_range(first_coordinate,
                                                           second_coordinate,
                                                           empty_matrix))

    def test_check_if_cell_occupied_assert_false(self):
        """
        For the range of the coordinates in the i-th list, and for the i-th
        numpy.ndarray it checks if all the cells described by the coordinates
        are occupied.
        """

        coordinates_list: List[List[Tuple[int, int]]] = [
            [(1, 1)],
            [(0, 0), (1, 1)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 0), (1, 1), (2, 2), (0, 1)],
            [(0, 0), (1, 1), (2, 2), (0, 1), (1, 0)],
            [(0, 0), (1, 1), (2, 2), (0, 1), (1, 0), (2, 0)],
            [(0, 0), (1, 1), (2, 2), (0, 1), (1, 0), (2, 0), (1, 2)],
            [(2, 1)],
            [(2, 1), (2, 2)],
            [(2, 1), (2, 2), (0, 1)],
            [(2, 1), (2, 2), (0, 1), (0, 0)],
            [(2, 1), (2, 2), (0, 1), (0, 0), (3, 2)],
            [(2, 1), (2, 2), (0, 1), (0, 0), (3, 2), (3, 3)],
            [(2, 1), (2, 2), (0, 1), (0, 0), (3, 2), (3, 3), (2, 3)],
            [(2, 1), (2, 2), (0, 1), (0, 0), (3, 2), (3, 3), (2, 3), (0, 2)],
            [(2, 1), (2, 2), (0, 1), (0, 0), (3, 2), (3, 3), (2, 3), (0, 2), (0, 3),
             (1, 0)],
            [(2, 1), (2, 2), (0, 1), (0, 0), (3, 2), (3, 3), (2, 3), (0, 2), (0, 3),
             (1, 0), (2, 0)],
            [(2, 1), (2, 2), (0, 1), (0, 0), (3, 2), (3, 3), (2, 3), (0, 2), (0, 3),
             (1, 0), (2, 0), (1, 1)]
        ]

        list_of_arrays: List[ndarray] = [
            np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
            np.array([[2, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
            np.array([[2, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=int),
            np.array([[2, 2, 0], [0, 1, 0], [0, 0, 1]], dtype=int),
            np.array([[2, 2, 0], [1, 1, 0], [0, 0, 1]], dtype=int),
            np.array([[2, 2, 0], [1, 1, 0], [2, 0, 1]], dtype=int),
            np.array([[2, 2, 0], [1, 1, 1], [2, 0, 1]], dtype=int),
            np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]], dtype=int),
            np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 1, 0], [0, 0, 0, 0]], dtype=int),
            np.array([[0, 2, 0, 0], [0, 0, 0, 0], [0, 2, 1, 0], [0, 0, 0, 0]], dtype=int),
            np.array([[1, 2, 0, 0], [0, 0, 0, 0], [0, 2, 1, 0], [0, 0, 0, 0]], dtype=int),
            np.array([[1, 2, 0, 0], [0, 0, 0, 0], [0, 2, 1, 0], [0, 0, 2, 0]], dtype=int),
            np.array([[1, 2, 0, 0], [0, 0, 0, 0], [0, 2, 1, 0], [0, 0, 2, 1]], dtype=int),
            np.array([[1, 2, 0, 0], [0, 0, 0, 0], [0, 2, 1, 2], [0, 0, 2, 1]], dtype=int),
            np.array([[1, 2, 1, 0], [0, 0, 0, 0], [0, 2, 1, 2], [0, 0, 2, 1]], dtype=int),
            np.array([[1, 2, 1, 2], [1, 0, 0, 0], [0, 2, 1, 2], [0, 0, 2, 1]], dtype=int),
            np.array([[1, 2, 1, 2], [1, 0, 0, 0], [2, 2, 1, 2], [0, 0, 2, 1]], dtype=int),
            np.array([[1, 2, 1, 2], [1, 1, 0, 0], [2, 2, 1, 2], [0, 0, 2, 1]], dtype=int),
        ]

        i: int

        for i in range(0, len(coordinates_list)):

            coordinates: Tuple[int, int]

            for coordinates in coordinates_list[i]:
                self.assertFalse(check_if_cell_occupied(coordinates[0], coordinates[1],
                                                        list_of_arrays[i]))

    def test_check_if_cell_occupied_assert_true(self):
        """
        For the range of the coordinates in the i-th list_of_coordinates list, and
        for the i-th numpy.ndarray in the list_of_arrays list, it checks if all
        the cells described by the coordinates are not occupied.
        """

        list_of_arrays: List[ndarray] = [
            np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
            np.array([[2, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
            np.array([[2, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=int),
            np.array([[2, 2, 0], [0, 1, 0], [0, 0, 1]], dtype=int),
            np.array([[2, 2, 0], [1, 1, 0], [0, 0, 1]], dtype=int),
            np.array([[2, 2, 0], [1, 1, 0], [2, 0, 1]], dtype=int),
            np.array([[2, 2, 0], [1, 1, 1], [2, 0, 1]], dtype=int),
            np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]], dtype=int),
            np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 1, 0], [0, 0, 0, 0]], dtype=int),
            np.array([[0, 2, 0, 0], [0, 0, 0, 0], [0, 2, 1, 0], [0, 0, 0, 0]], dtype=int),
            np.array([[1, 2, 0, 0], [0, 0, 0, 0], [0, 2, 1, 0], [0, 0, 0, 0]], dtype=int),
            np.array([[1, 2, 0, 0], [0, 0, 0, 0], [0, 2, 1, 0], [0, 0, 2, 0]], dtype=int),
            np.array([[1, 2, 0, 0], [0, 0, 0, 0], [0, 2, 1, 0], [0, 0, 2, 1]], dtype=int),
            np.array([[1, 2, 0, 0], [0, 0, 0, 0], [0, 2, 1, 2], [0, 0, 2, 1]], dtype=int),
            np.array([[1, 2, 1, 0], [0, 0, 0, 0], [0, 2, 1, 2], [0, 0, 2, 1]], dtype=int),
            np.array([[1, 2, 1, 2], [1, 0, 0, 0], [0, 2, 1, 2], [0, 0, 2, 1]], dtype=int),
            np.array([[1, 2, 1, 2], [1, 0, 0, 0], [2, 2, 1, 2], [0, 0, 2, 1]], dtype=int),
            np.array([[1, 2, 1, 2], [1, 1, 0, 0], [2, 2, 1, 2], [0, 0, 2, 1]], dtype=int),
        ]

        list_of_coordinates: List[List[Tuple[int, int]]] = [
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
            [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
            [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)],
            [(0, 2), (1, 0), (1, 2), (2, 0), (2, 1)],
            [(0, 2), (1, 2), (2, 0), (2, 1)],
            [(0, 2), (1, 2), (2, 1)],
            [(0, 2), (2, 1)],
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0),
             (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)],
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0),
             (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)],
            [(0, 0), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0),
             (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)],
            [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0),
             (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)],
            [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0),
             (2, 3), (3, 0), (3, 1), (3, 3)],
            [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0),
             (2, 3), (3, 0), (3, 1)],
            [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0),
             (3, 0), (3, 1)],
            [(0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0),
             (3, 0), (3, 1)],
            [(1, 1), (1, 2), (1, 3), (2, 0),
             (3, 0), (3, 1)],
            [(1, 1), (1, 2), (1, 3),
             (3, 0), (3, 1)],
            [(1, 2), (1, 3), (3, 0),
             (3, 1)]]

        i: int

        for i in range(0, len(list_of_coordinates)):

            coordinates: Tuple[int, int]

            for coordinates in list_of_coordinates[i]:
                self.assertTrue(check_if_cell_occupied(coordinates[0], coordinates[1],
                                                       list_of_arrays[i]))

    def test_add_edge_1(self):
        """
        It asserts that 1 added to the numpy.ndarray by the add_1
        function is added correctly.
        """

        one_list_before: List[ndarray] = [np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=int),
                                          np.array([[2, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
                                          np.array([[2, 2, 0], [0, 1, 1], [0, 0, 0]], dtype=int),
                                          np.array([[2, 2, 0], [0, 1, 1], [0, 2, 1]], dtype=int),
                                          np.array([[2, 2, 0], [2, 1, 1], [1, 2, 1]], dtype=int),
                                          np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], dtype=int),
                                          np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
                                          np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
                                          np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 2, 1]], dtype=int),
                                          np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 2, 2, 1]], dtype=int),
                                          np.array([[2, 0, 2, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                          np.array([[2, 0, 2, 2], [0, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                          np.array([[2, 0, 2, 2], [1, 1, 0, 2], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int)]

        coordinates_list: List[Tuple[int, int]] = [(1, 1),
                                                   (1, 2), (2, 2), (2, 0), (0, 2), (2, 1), (2, 0), (3, 3), (2, 2),
                                                   (3, 0),
                                                   (1, 1), (1, 0), (1, 2)]

        one_list_after: List[ndarray] = [np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
                                         np.array([[2, 0, 0], [0, 1, 1], [0, 0, 0]], dtype=int),
                                         np.array([[2, 2, 0], [0, 1, 1], [0, 0, 1]], dtype=int),
                                         np.array([[2, 2, 0], [0, 1, 1], [1, 2, 1]], dtype=int),
                                         np.array([[2, 2, 1], [2, 1, 1], [1, 2, 1]], dtype=int),
                                         np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]], dtype=int),
                                         np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
                                         np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 1]], dtype=int),
                                         np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 2, 2, 1]], dtype=int),
                                         np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                         np.array([[2, 0, 2, 0], [0, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                         np.array([[2, 0, 2, 2], [1, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                         np.array([[2, 0, 2, 2], [1, 1, 1, 2], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int)
                                         ]

        i: int

        for i in range(0, len(one_list_before)):
            self.assertEqual(add_1(coordinates_list[i],
                                   one_list_before[i]).all(),
                             one_list_after[i].all())

    def test_add_edge_2(self):
        """
        It asserts that 2 added to the numpy.ndarray by the add_2
        function is added correctly.
        """

        two_list_before: List[ndarray] = [np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
                                          np.array([[2, 0, 0], [0, 1, 1], [0, 0, 0]], dtype=int),
                                          np.array([[2, 2, 0], [0, 1, 1], [0, 0, 1]], dtype=int),
                                          np.array([[2, 2, 0], [0, 1, 1], [1, 2, 1]], dtype=int),
                                          np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]], dtype=int),
                                          np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
                                          np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 1]], dtype=int),
                                          np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 2, 2, 1]], dtype=int),
                                          np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                          np.array([[2, 0, 2, 0], [0, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                          np.array([[2, 0, 2, 2], [1, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                          np.array([[2, 0, 2, 2], [1, 1, 1, 2], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int)]

        two_coordinates_list: List[Tuple[int, int]] = [(0, 0), (0, 1), (2, 1), (1, 0), (3, 1), (0, 0), (3, 2),
                                                       (2, 3), (0, 2), (0, 3), (1, 3), (0, 1)]

        two_list_after: List[ndarray] = [np.array([[2, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
                                         np.array([[2, 2, 0], [0, 1, 1], [0, 0, 0]], dtype=int),
                                         np.array([[2, 2, 0], [0, 1, 1], [0, 2, 1]], dtype=int),
                                         np.array([[2, 2, 0], [2, 1, 1], [1, 2, 1]], dtype=int),
                                         np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
                                         np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
                                         np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 2, 1]], dtype=int),
                                         np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 2], [0, 2, 2, 1]], dtype=int),
                                         np.array([[2, 0, 2, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                         np.array([[2, 0, 2, 2], [0, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                         np.array([[2, 0, 2, 2], [1, 1, 0, 2], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
                                         np.array([[2, 2, 2, 2], [1, 1, 1, 2], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int)]

        i: int

        for i in range(0, len(two_list_before)):
            self.assertEqual(add_2(two_coordinates_list[i],
                                   two_list_before[i]).all(), two_list_after[i].all())

    def test_display_coordinates(self):
        """
        It asserts that the coordinates to display are produced correctly by the
        helper method display_coordinates.
        """

        display_coordinates_lists: List[Union[List[Any], List[str]]] = [[],
                                                                        ['(0,0)'],
                                                                        ['(0,0)(0,1)',
                                                                         '(1,0)(1,1)'],
                                                                        ['(0,0)(0,1)(0,2)',
                                                                         '(1,0)(1,1)(1,2)',
                                                                         '(2,0)(2,1)(2,2)'],
                                                                        ['(0,0)(0,1)(0,2)(0,3)',
                                                                         '(1,0)(1,1)(1,2)(1,3)',
                                                                         '(2,0)(2,1)(2,2)(2,3)',
                                                                         '(3,0)(3,1)(3,2)(3,3)'],
                                                                        ['(0,0)(0,1)(0,2)(0,3)(0,4)',
                                                                         '(1,0)(1,1)(1,2)(1,3)(1,4)',
                                                                         '(2,0)(2,1)(2,2)(2,3)(2,4)',
                                                                         '(3,0)(3,1)(3,2)(3,3)(3,4)',
                                                                         '(4,0)(4,1)(4,2)(4,3)(4,4)']]

        i: int

        for i in range(0, len(display_coordinates_lists)):
            self.assertEqual(display_coordinates(i), display_coordinates_lists[i])

    def test_enter_the_coordinates_for_1_and_check_them(self):
        """
        It asserts that the coordinates entered by the player result in the
        correct placement of 1 in the numpy.ndarray passed in to the tested
        function (enter_the_coordinates_for_1_and_check_them).
        """

        one_list_before: List[ndarray] = \
            [np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=int),
             np.array([[2, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
             np.array([[2, 2, 0], [0, 1, 1], [0, 0, 0]], dtype=int),
             np.array([[2, 2, 0], [0, 1, 1], [0, 2, 1]], dtype=int),
             np.array([[2, 2, 0], [2, 1, 1], [1, 2, 1]], dtype=int),
             np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], dtype=int),
             np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
             np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
             np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 2, 1]], dtype=int),
             np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 2, 2, 1]], dtype=int),
             np.array([[2, 0, 2, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
             np.array([[2, 0, 2, 2], [0, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
             np.array([[2, 0, 2, 2], [1, 1, 0, 2], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int)]

        coordinates_list: List[str] = ["1 1", " 1 2", "2 2 ",
                                       "2 0", "0 2", "2 1",
                                       "2 0", "3 3", "2 2",
                                       "3 0", "1 1", "1 0",
                                       "1 2"]

        one_list_after: List[ndarray] = [
            np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
            np.array([[2, 0, 0], [0, 1, 1], [0, 0, 0]], dtype=int),
            np.array([[2, 2, 0], [0, 1, 1], [0, 0, 1]], dtype=int),
            np.array([[2, 2, 0], [0, 1, 1], [1, 2, 1]], dtype=int),
            np.array([[2, 2, 1], [2, 1, 1], [1, 2, 1]], dtype=int),
            np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]], dtype=int),
            np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
            np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 1]], dtype=int),
            np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 2, 0], [0, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 2, 2], [1, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 2, 2], [1, 1, 1, 2], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int)]

        i: int

        for i in range(0, len(one_list_before)):
            self.assertEqual(enter_the_coordinates_for_1_and_check_them(
                coordinates_list[i], one_list_before[i]).all(),
                             one_list_after[i].all())

    def test_enter_the_coordinates_for_2_and_check_them(self):
        """
        It asserts that the coordinates entered by the player result in the
        correct placement of 2 in the numpy.ndarray passed in to the tested
        function (enter_the_coordinates_for_2_and_check_them).
        """

        two_list_before: List[ndarray] = [
            np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
            np.array([[2, 0, 0], [0, 1, 1], [0, 0, 0]], dtype=int),
            np.array([[2, 2, 0], [0, 1, 1], [0, 0, 1]], dtype=int),
            np.array([[2, 2, 0], [0, 1, 1], [1, 2, 1]], dtype=int),
            np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]], dtype=int),
            np.array([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
            np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 1]], dtype=int),
            np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 2, 0], [0, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 2, 2], [1, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 2, 2], [1, 1, 1, 2], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int)]

        two_coordinates_list: List[str] = ["0 0", " 0 1", "2 1 ",
                                           " 1 0 ", "3 1", "0 0",
                                           "3 2", "2 3", "0 2",
                                           "0 3", "1 3", "0 1"]

        two_list_after: List[ndarray] = [
            np.array([[2, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=int),
            np.array([[2, 2, 0], [0, 1, 1], [0, 0, 0]], dtype=int),
            np.array([[2, 2, 0], [0, 1, 1], [0, 2, 1]], dtype=int),
            np.array([[2, 2, 0], [2, 1, 1], [1, 2, 1]], dtype=int),
            np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
            np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]], dtype=int),
            np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 2], [0, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 2, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 2, 2], [0, 1, 0, 0], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
            np.array([[2, 0, 2, 2], [1, 1, 0, 2], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int),
            np.array([[2, 2, 2, 2], [1, 1, 1, 2], [1, 1, 1, 0], [1, 2, 2, 1]], dtype=int)]

        i: int

        for i in range(0, len(two_list_before)):
            self.assertEqual(enter_the_coordinates_for_2_and_check_them(
                two_coordinates_list[i], two_list_before[i]).all(),
                             two_list_after[i].all())

    def test_diagonal_win_assert_true(self):
        """
        Asserts that the numpy.ndarrays with the same diagonal values different
        from 0 are correctly evaluated as having a diagonal win constitution.
        """

        diagonal_win_list: List[ndarray] = [
            np.array([[2, 1, 0], [0, 2, 1], [0, 1, 2]], dtype=int),
            np.array([[0, 0, 1], [2, 1, 0], [1, 0, 2]], dtype=int),
            np.array([[1, 2, 2, 2], [0, 1, 2, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=int),
            np.array([[1, 1, 1, 2], [1, 0, 2, 0], [1, 2, 0, 2], [2, 0, 2, 0]], dtype=int)
        ]

        i: int

        for i in range(0, len(diagonal_win_list)):
            self.assertTrue(diagonal_win(diagonal_win_list[i]))

    def test_diagonal_win_assert_false(self):
        """
        Asserts that the numpy.ndarrays not having all the diagonal values equal
        to 1 or to 2 are correctly evaluated as not having a diagonal win
        constitution.
        """

        diagonal_fail_list: List[List[List[int]]] = [
            [[1, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[1, 0, 0], [0, 0, 0], [0, 2, 0]],
            [[1, 0, 0], [0, 0, 0], [0, 2, 1]],
            [[1, 0, 2], [0, 0, 0], [0, 2, 1]],
            [[1, 0, 2], [0, 0, 1], [0, 2, 1]],
            [[1, 0, 2], [0, 2, 1], [0, 2, 1]],
            [[1, 0, 2], [1, 2, 1], [0, 2, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 1, 0]],
            [[0, 0, 0, 0], [0, 0, 1, 0], [0, 2, 0, 0], [0, 0, 1, 0]],
            [[0, 0, 0, 2], [0, 0, 1, 0], [0, 2, 0, 0], [0, 0, 1, 0]],
            [[0, 0, 0, 2], [0, 0, 1, 0], [0, 2, 1, 0], [0, 0, 1, 0]],
            [[0, 0, 0, 2], [0, 0, 1, 0], [0, 2, 1, 2], [0, 0, 1, 0]],
            [[0, 0, 0, 2], [0, 0, 1, 0], [0, 2, 1, 2], [0, 0, 1, 0]],
            [[0, 0, 0, 2], [0, 0, 1, 0], [0, 2, 1, 2], [0, 0, 1, 1]],
            [[0, 0, 0, 2], [0, 0, 1, 0], [0, 2, 1, 2], [0, 0, 1, 1]],
            [[2, 0, 0, 2], [0, 0, 1, 0], [0, 2, 1, 2], [0, 0, 1, 1]],
            [[2, 0, 0, 2], [0, 1, 1, 0], [0, 2, 1, 2], [0, 0, 1, 1]],
            [[2, 0, 0, 2], [0, 1, 1, 0], [0, 2, 1, 2], [2, 0, 1, 1]],
            [[2, 0, 1, 2], [0, 1, 1, 0], [0, 2, 1, 2], [2, 0, 1, 1]]
        ]

        fail_list: List[List[int]]

        for fail_list in diagonal_fail_list:
            self.assertFalse(diagonal_win(np.array(fail_list, dtype=int)))

    def test_draw_assert_true(self):
        """
        Asserts that the numpy.ndarrays having the draw constitution of the cells
        are correctly evaluated as having a draw cell constitution.
        """

        draws_list: List[List[List[int]]] = [
            [[2, 1, 1], [1, 2, 2], [2, 2, 1]],
            [[1, 2, 2, 1], [1, 1, 1, 2], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[2, 1, 1, 1], [2, 1, 1, 2], [1, 2, 2, 2], [2, 1, 2, 1]],
            [[1, 2, 2, 1, 1], [1, 2, 2, 2, 2], [2, 1, 1, 1, 2], [2, 1, 2, 2, 1],
             [2, 1, 1, 1, 2]],
            [[2, 1, 1, 1, 1, 1], [1, 2, 2, 2, 1, 2], [2, 1, 2, 2, 2, 2],
             [2, 2, 2, 1, 1, 2], [2, 1, 2, 1, 1, 1], [2, 2, 1, 1, 1, 1]],
            [[2, 2, 1, 2], [1, 2, 2, 1], [1, 1, 2, 2], [2, 1, 1, 1]],
            [[1, 1, 1, 2, 1], [2, 2, 2, 1, 2], [2, 2, 1, 2, 2], [1, 1, 2, 1, 1],
             [2, 2, 2, 1, 1]],
            [[1, 1, 2, 2], [1, 2, 1, 2], [2, 1, 1, 1], [2, 2, 2, 1]],
            [[2, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 1], [1, 2, 2, 1]]
        ]

        draw_list: List[List[int]]

        for draw_list in draws_list:
            self.assertTrue(draw(np.array(draw_list, dtype=int)))

    def test_draw_assert_false(self):
        """
        Asserts that the numpy.ndarrays not having the draw constitution of the cells
        are correctly evaluated as not having a draw cell constitution.
        """

        no_draw_list: List[List[List[int]]] = [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 1, 2]],
            [[0, 0, 0], [0, 0, 0], [1, 1, 2]],
            [[2, 0, 0], [0, 0, 0], [1, 1, 2]],
            [[2, 0, 0], [0, 1, 0], [1, 1, 2]],
            [[2, 0, 0], [0, 1, 2], [1, 1, 2]],
            [[2, 1, 0], [0, 1, 2], [1, 1, 2]],
            [[0, 0, 0], [0, 0, 0], [0, 2, 1]],
            [[0, 0, 0], [0, 0, 0], [2, 2, 1]],
            [[0, 1, 0], [0, 0, 0], [2, 2, 1]],
            [[0, 1, 0], [0, 2, 0], [2, 2, 1]],
            [[2, 1, 1], [0, 2, 0], [2, 2, 1]],
            [[2, 1, 1], [1, 2, 0], [2, 2, 1]],
            [[2, 1, 1], [1, 2, 0], [2, 2, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 1], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 1], [0, 0, 2, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 1], [0, 0, 2, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 1], [0, 0, 2, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 1], [1, 0, 2, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 1], [1, 2, 2, 1]],
            [[0, 0, 0, 0], [0, 1, 0, 0], [2, 2, 0, 1], [1, 2, 2, 1]],
            [[1, 0, 0, 0], [0, 1, 0, 0], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[1, 0, 2, 0], [0, 1, 0, 0], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[1, 0, 2, 0], [1, 1, 0, 0], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[1, 2, 2, 0], [1, 1, 0, 0], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[1, 2, 2, 0], [1, 1, 1, 0], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[1, 2, 2, 0], [1, 1, 1, 2], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [1, 2, 0]],
            [[0, 0, 0], [0, 0, 0], [1, 2, 0]],
            [[1, 0, 0], [0, 0, 0], [1, 2, 0]],
            [[1, 2, 0], [0, 0, 0], [1, 2, 0]],
            [[1, 2, 0], [0, 0, 0], [1, 2, 1]],
            [[1, 2, 2], [0, 0, 0], [1, 2, 1]],
            [[1, 2, 2], [0, 0, 1], [1, 2, 1]],
            [[1, 2, 2], [2, 0, 1], [1, 2, 1]],
            [[2, 0, 1, 2], [0, 1, 1, 0], [0, 2, 1, 2], [2, 0, 1, 1]],
            [[2, 1, 0], [0, 1, 2], [1, 1, 2]],
            [[2, 1, 2, 0], [0, 1, 2, 2], [1, 1, 1, 2], [2, 1, 2, 1]],
            [[1, 2, 1], [2, 2, 1], [1, 2, 2]],
            [[2, 1, 0], [0, 1, 0], [0, 1, 2]],
            [[1, 2, 1, 1], [0, 2, 0, 0], [0, 2, 0, 1], [2, 2, 2, 1]],
            [[1, 2, 1, 1, 2], [1, 1, 1, 0, 2], [2, 2, 2, 2, 2],
             [2, 1, 2, 0, 2], [1, 2, 1, 1, 1]],
            [[2, 2, 2, 2], [1, 1, 2, 0], [2, 1, 1, 1], [2, 1, 0, 1]],
            [[2, 2, 2, 2], [0, 0, 2, 2], [1, 0, 1, 0], [0, 1, 1, 1]],
            [[2, 2, 2, 2, 1, 1], [0, 2, 0, 0, 1, 2], [1, 1, 1, 1, 1, 1],
             [2, 2, 2, 1, 2, 1], [2, 1, 2, 1, 2, 1],
             [2, 2, 1, 1, 1, 2]],
            [[1, 2, 2], [1, 1, 1], [1, 2, 2]],
            [[1, 2, 0], [0, 2, 0], [1, 2, 0]],
            [[1, 1, 1, 2], [2, 0, 1, 2], [2, 2, 1, 2], [1, 1, 0, 2]]
        ]

        no_draw: List[List[int]]

        for no_draw in no_draw_list:
            self.assertFalse(draw(np.array(no_draw, dtype=int)))

    def test_vertical_and_horizontal_win_assert_true(self):
        """
        Asserts that the numpy.ndarrays having the vertical or the horizontal win
        constitution of the cells' values are correctly evaluated as having the
        vertical or the horizontal win constitution of the cells by the tested
        function (vertical_and_horizontal_win).
        """

        vertical_and_horizontal_win_list: List[List[List[int]]] = [
            [[2, 0, 1, 2], [0, 1, 1, 0], [0, 2, 1, 2], [2, 0, 1, 1]],
            [[2, 1, 0], [0, 1, 2], [1, 1, 2]],
            [[2, 1, 2, 0], [0, 1, 2, 2], [1, 1, 1, 2], [2, 1, 2, 1]],
            [[1, 2, 1], [2, 2, 1], [1, 2, 2]],
            [[2, 1, 0], [0, 1, 0], [0, 1, 2]],
            [[1, 2, 1, 1], [0, 2, 0, 0], [0, 2, 0, 1], [2, 2, 2, 1]],
            [[1, 2, 1, 1, 2], [1, 1, 1, 0, 2], [2, 2, 2, 2, 2], [2, 1, 2, 0, 2],
             [1, 2, 1, 1, 1]],
            [[2, 2, 2, 2], [1, 1, 2, 0], [2, 1, 1, 1], [2, 1, 0, 1]],
            [[2, 2, 2, 2], [0, 0, 2, 2], [1, 0, 1, 0], [0, 1, 1, 1]],
            [[2, 2, 2, 2, 1, 1], [0, 2, 0, 0, 1, 2], [1, 1, 1, 1, 1, 1],
             [2, 2, 2, 1, 2, 1], [2, 1, 2, 1, 2, 1], [2, 2, 1, 1, 1, 2]],
            [[1, 2, 2], [1, 1, 1], [1, 2, 2]],
            [[1, 2, 0], [0, 2, 0], [1, 2, 0]],
            [[1, 1, 1, 2], [2, 0, 1, 2], [2, 2, 1, 2], [1, 1, 0, 2]]]

        vertical_or_horizontal_win: List[List[int]]

        for vertical_or_horizontal_win in vertical_and_horizontal_win_list:
            self.assertTrue(vertical_and_horizontal_win(
                np.array(vertical_or_horizontal_win, dtype=int)))

    def test_vertical_and_horizontal_win_assert_false(self):
        """
        Asserts that the numpy.ndarrays not having the vertical or the horizontal
        win constitution of the cell values are correctly evaluated as not having
        the vertical or the horizontal win constitution of the cells by the tested
        function (vertical_and_horizontal_win).
        """

        draws_list: List[List[List[int]]] = [
            [[2, 1, 1], [1, 2, 2], [2, 2, 1]],
            [[1, 2, 2, 1], [1, 1, 1, 2], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[2, 1, 1, 1], [2, 1, 1, 2], [1, 2, 2, 2], [2, 1, 2, 1]],
            [[1, 2, 2, 1, 1], [1, 2, 2, 2, 2], [2, 1, 1, 1, 2], [2, 1, 2, 2, 1],
             [2, 1, 1, 1, 2]],
            [[2, 1, 1, 1, 1, 1], [1, 2, 2, 2, 1, 2], [2, 1, 2, 2, 2, 2],
             [2, 2, 2, 1, 1, 2],
             [2, 1, 2, 1, 1, 1], [2, 2, 1, 1, 1, 1]],
            [[2, 2, 1, 2], [1, 2, 2, 1], [1, 1, 2, 2], [2, 1, 1, 1]],
            [[1, 1, 1, 2, 1], [2, 2, 2, 1, 2], [2, 2, 1, 2, 2], [1, 1, 2, 1, 1],
             [2, 2, 2, 1, 1]],
            [[1, 1, 2, 2], [1, 2, 1, 2], [2, 1, 1, 1], [2, 2, 2, 1]],
            [[2, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 1], [1, 2, 2, 1]],
            [[1, 1, 2, 2, 2], [2, 1, 2, 2, 1], [2, 2, 1, 1, 1], [2, 1, 1, 1, 2],
             [0, 2, 1, 2, 1]],
            [[2, 2, 1, 1, 2], [1, 2, 2, 1, 1], [2, 2, 1, 2, 1], [2, 1, 1, 1, 2],
             [1, 1, 2, 2, 2]],
            [[2, 1, 1, 1, 1], [1, 1, 1, 2, 1], [2, 2, 2, 1, 2], [1, 2, 1, 2, 2],
             [1, 2, 1, 2, 2]],
            [[1, 1, 1, 2, 2], [1, 2, 1, 2, 1], [1, 1, 2, 2, 1], [1, 1, 1, 2, 2],
             [2, 2, 2, 1, 2]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 1, 2]],
            [[0, 0, 0], [0, 0, 0], [1, 1, 2]],
            [[2, 0, 0], [0, 0, 0], [1, 1, 2]],
            [[2, 0, 0], [0, 1, 0], [1, 1, 2]],
            [[2, 0, 0], [0, 1, 2], [1, 1, 2]],
            [[0, 0, 0], [0, 0, 0], [0, 2, 1]],
            [[0, 0, 0], [0, 0, 0], [2, 2, 1]],
            [[0, 1, 0], [0, 0, 0], [2, 2, 1]],
            [[0, 1, 0], [0, 2, 0], [2, 2, 1]],
            [[2, 1, 1], [0, 2, 0], [2, 2, 1]],
            [[2, 1, 1], [1, 2, 0], [2, 2, 1]],
            [[2, 1, 1], [1, 2, 0], [2, 2, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 1], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 1], [0, 0, 2, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 1], [0, 0, 2, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 1], [0, 0, 2, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 1], [1, 0, 2, 1]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 1], [1, 2, 2, 1]],
            [[0, 0, 0, 0], [0, 1, 0, 0], [2, 2, 0, 1], [1, 2, 2, 1]],
            [[1, 0, 0, 0], [0, 1, 0, 0], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[1, 0, 2, 0], [0, 1, 0, 0], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[1, 0, 2, 0], [1, 1, 0, 0], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[1, 2, 2, 0], [1, 1, 0, 0], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[1, 2, 2, 0], [1, 1, 1, 0], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[1, 2, 2, 0], [1, 1, 1, 2], [2, 2, 2, 1], [1, 2, 2, 1]],
            [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [1, 2, 0]],
            [[0, 0, 0], [0, 0, 0], [1, 2, 0]],
            [[1, 0, 0], [0, 0, 0], [1, 2, 0]],
            [[1, 2, 0], [0, 0, 0], [1, 2, 0]],
            [[1, 2, 0], [0, 0, 0], [1, 2, 1]],
            [[1, 2, 2], [0, 0, 0], [1, 2, 1]],
            [[1, 2, 2], [0, 0, 1], [1, 2, 1]],
            [[1, 2, 2], [2, 0, 1], [1, 2, 1]]]

        vertical_or_horizontal_fail: List[List[int]]

        for vertical_or_horizontal_fail in draws_list:
            self.assertFalse(vertical_and_horizontal_win(
                np.array(vertical_or_horizontal_fail, dtype=int)))

    def test_check_if_choice_int_assert_true(self):
        """
        Asserts that the tested function on receiving the range of
        integers returns True.
        """

        int_list: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        num: int

        for num in int_list:
            self.assertTrue(check_if_choice_int(num))

    def test_check_if_choice_int_assert_false(self):

        """
        Asserts that the tested function on receiving the range of
        non-integers returns False.
        """

        rubbish_list: List[Union[float, str]] = [1.2, 'f', 13.3, 1.0]

        presumed_not_int: Union[float, str]

        for presumed_not_int in rubbish_list:
            self.assertFalse(check_if_choice_int(presumed_not_int))

    def test_check_if_choice_in_range_assert_true(self):
        """
        Asserts, that the tested function on receiving 1 and 2
        returns True.
        """

        num_list: List[int] = [1, 2]

        num: int

        for num in num_list:
            self.assertTrue(check_if_choice_in_range(num))

    def test_check_if_choice_in_range_assert_false(self):
        """
        Asserts, that the tested function on receiving the range of integers
        that are not 1 or 2 returns False.
        """

        num_list: List[int] = [0, 3, 4, 5, 6, -1, 9, 10, 7]

        num: int

        for num in num_list:
            self.assertFalse(check_if_choice_in_range(num))

    def test_matrix_len(self):
        """
        Asserts that the tested function (matrix_len) correctly
        calculates the horizontal dimension of the passed-in numpy.ndarray.
        """

        matrices: List[List[List[int]]] = [[[0]],
                                           [[0, 0],
                                            [0, 0]],
                                           [[0, 0, 0],
                                            [0, 0, 0],
                                            [0, 0, 0]],
                                           [[0, 0, 0, 0],
                                            [0, 0, 0, 0],
                                            [0, 0, 0, 0],
                                            [0, 0, 0, 0]],
                                           [[0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0]],
                                           [[0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0]]]

        horizontal_len_of_matrices: List[int] = [1, 2, 3, 4, 5, 6]

        i: int

        for i in range(0, len(matrices)):
            self.assertEqual(
                matrix_len(np.array(matrices[i], dtype=int)), horizontal_len_of_matrices[i])

    def test_construct_adjacency_matrix(self):
        """
        Asserts that the method construct_adjacency_matrix correctly constructs
        adjacency matrices from the information about the number of vertices.
        """

        matrices: List[List[List[int]]] = [[[0]],
                                           [[0, 0],
                                            [0, 0]],
                                           [[0, 0, 0],
                                            [0, 0, 0],
                                            [0, 0, 0]],
                                           [[0, 0, 0, 0],
                                            [0, 0, 0, 0],
                                            [0, 0, 0, 0],
                                            [0, 0, 0, 0]],
                                           [[0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0]],
                                           [[0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0]]]

        vertices: List[int] = [0, 1, 2, 3, 4, 5]

        i: int

        for i in range(0, len(matrices)):
            self.assertEqual(
                construct_adjacency_matrix(
                    vertices[i]).all(), (np.array(matrices[i], dtype=int)).all())


if __name__ == '__main__':
    unittest.main()
