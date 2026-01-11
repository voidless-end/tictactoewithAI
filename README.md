run.py:  The non-classic 2-player tic-tac-toe console game with the
dimensions which you can choose and the choice of the playing symbol
(1 or 2 instead of "O" or "X"). Inspired by the adjacency matrix.

run_automatic_gameplay.py: The non-classic 2-player (simulated)
tic-tac-toe console gameplay with the pseudorandomly chosen dimensions
(from 3 to 101) and the pseudorandom choice of the starting symbol (1
or 2 instead of "O" and "X") for the automatic building and testing
purposes.

run_automatic_smaller.py: The non-classic 2-player (simulated)
tic-tac-toe console gameplay with the pseudorandomly chosen dimensions
(from 3 to 6) and the pseudorandom choice of the starting symbol (1
or 2 instead of "O" and "X") for the automatic building and testing
purposes.

run_automatic_gameplay_choice_of_dimensions.py: The non-classic
2-player (simulated) tic-tac-toe console gameplay with the
dimensions chosen by the player and the pseudorandom choice of the
starting symbol (1 or 2 instead of "O" and "X") for the automatic
building and testing purposes.

run_choice_symbol_choice_dimensions_automatic_gameplay.py: The non-classic
2-player (simulated) tic-tac-toe console gameplay with the
dimensions chosen by the player and the choice of the
starting symbol (1 or 2 instead of "O" and "X") for the automatic
building and testing purposes.

run_2_choices.py - The non-classic 1-player (playing against the
computer, pseudorandomly) tic-tac-toe console gameplay with the
dimensions chosen by the player and the choice of the
starting symbol (1 or 2 instead of "O" and "X").

run_2_choices_automatic_build.py - The simulation of the aforementioned
game for the automatic building and testing purposes.

run_testing.py - Choose the dimensions, a starting symbol and the number
of the games you want to play in the automatic build mode. The summaries of 
the results are printed at the end and saved to a text file. Textfiles have descriptive names:
testing_{starting_symbol}_game_{dimensions_of_the_matrix}_{number_of_the_games_played}_{result of calling of the
time.time() function trimmed to a integer format}.txt

run_testing_automatic_smaller.py - The automatic version of 
the aforementioned game with a starting symbol drawn pseudorandomly,
the number of games from 1 000 to 100 000, and the dimensions
of the grid drawn pseudorandomly from a range of integers, 
where integer ∈ <3, 6>. The summaries of the results are printed
at the end and saved to a text file. Textfiles have descriptive names:
testing_{starting_symbol}_game_{dimensions_of_the_matrix}_{number_of_the_games_played}_{result of calling of the
time.time() function trimmed to a integer format}.txt
# tictactoewithAI
