# File run_testing_automatic_smaller.py: The gameplay for the automatic
# testing and building purposes. The symbol to start with is drawn
# pseudorandomly, the number of games to play is drawn pseudorandomly from
# the range of integers, where integer ∈ <1000, 100 000>, and the
# dimensions of the game's grid are drawn pseudorandomly from the range
# of integers, where integer ∈ <3, 6>. The summaries are printed at the
# end and are saved to a text file. Text files have descriptive names:
# "testing_{starting_symbol}_game_{dimensions_of_the_matrix}_
# {number_of_the_games_played}_{result of calling of the
# time.time() function trimmed to a integer format}.txt".

from choice_testing_automatic_smaller import TheGame

if __name__ == '__main__':
    game = TheGame()
