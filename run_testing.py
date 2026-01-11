# File run_testing.py: Choose the number of the games you want to play
# in the automatic building mode, choose the starting symbol and the
# dimensions of the matrix. The summaries are printed at the end and
# saved to a text file. Textfiles have descriptive names:
# "testing_{starting_symbol}_game_{dimensions_of_the_matrix}_
# {number_of_the_games_played}_{result of calling of the
# time.time() function trimmed to a integer format}.txt".

from choice_testing import TheGame

if __name__ == '__main__':
    game = TheGame()
