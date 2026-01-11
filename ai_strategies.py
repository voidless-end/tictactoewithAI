# File: ai_strategies.py
# Different AI strategies for Tic-Tac-Toe: Random, Minimax, Monte Carlo

import numpy as np
from typing import Tuple, List, Optional
from random import randint, choice
from abc import ABC, abstractmethod
import copy
import math


class BaseAI(ABC):
    """Abstract base class for all AI strategies."""
    
    def __init__(self, player_symbol: int):
        """
        Initialize the AI with a player symbol.
        
        :param player_symbol: 1 or 2, the symbol this AI plays as
        """
        self.player_symbol = player_symbol
        self.opponent_symbol = 2 if player_symbol == 1 else 1
        self.name = "BaseAI"
    
    @abstractmethod
    def get_move(self, matrix: np.ndarray) -> Tuple[int, int]:
        """
        Get the next move for the AI.
        
        :param matrix: Current game board state
        :return: Tuple of (row, col) coordinates for the move
        """
        pass
    
    def get_empty_cells(self, matrix: np.ndarray) -> List[Tuple[int, int]]:
        """Get all empty cells on the board."""
        empty = []
        size = matrix.shape[0]
        for i in range(size):
            for j in range(size):
                if matrix[i, j] == 0:
                    empty.append((i, j))
        return empty
    
    def check_winner(self, matrix: np.ndarray) -> Optional[int]:
        """
        Check if there's a winner.
        
        :return: 1 if player 1 wins, 2 if player 2 wins, 0 for draw, None for ongoing
        """
        size = matrix.shape[0]
        
        # Check rows
        for i in range(size):
            if matrix[i, 0] != 0 and all(matrix[i, j] == matrix[i, 0] for j in range(size)):
                return matrix[i, 0]
        
        # Check columns
        for j in range(size):
            if matrix[0, j] != 0 and all(matrix[i, j] == matrix[0, j] for i in range(size)):
                return matrix[0, j]
        
        # Check main diagonal
        if matrix[0, 0] != 0 and all(matrix[i, i] == matrix[0, 0] for i in range(size)):
            return matrix[0, 0]
        
        # Check anti-diagonal
        if matrix[0, size-1] != 0 and all(matrix[i, size-1-i] == matrix[0, size-1] for i in range(size)):
            return matrix[0, size-1]
        
        # Check for draw (no empty cells)
        if len(self.get_empty_cells(matrix)) == 0:
            return 0
        
        return None  # Game ongoing


class RandomAI(BaseAI):
    """AI that plays randomly - selects any available cell."""
    
    def __init__(self, player_symbol: int):
        super().__init__(player_symbol)
        self.name = "RandomAI"
    
    def get_move(self, matrix: np.ndarray) -> Tuple[int, int]:
        """Select a random empty cell."""
        empty_cells = self.get_empty_cells(matrix)
        if empty_cells:
            return choice(empty_cells)
        return (-1, -1)


class MinimaxAI(BaseAI):
    """
    AI that uses the Minimax algorithm with alpha-beta pruning.
    Plays optimally on small boards (3x3, 4x4).
    """
    
    def __init__(self, player_symbol: int, max_depth: int = 6):
        super().__init__(player_symbol)
        self.name = "MinimaxAI"
        self.max_depth = max_depth
    
    def get_move(self, matrix: np.ndarray) -> Tuple[int, int]:
        """Get the best move using minimax with alpha-beta pruning."""
        empty_cells = self.get_empty_cells(matrix)
        if not empty_cells:
            return (-1, -1)
        
        # For larger boards, limit depth more aggressively
        size = matrix.shape[0]
        if size > 4:
            self.max_depth = min(4, self.max_depth)
        
        best_score = float('-inf')
        best_move = empty_cells[0]
        alpha = float('-inf')
        beta = float('inf')
        
        for move in empty_cells:
            test_matrix = matrix.copy()
            test_matrix[move] = self.player_symbol
            
            score = self._minimax(test_matrix, 0, False, alpha, beta)
            
            if score > best_score:
                best_score = score
                best_move = move
            
            alpha = max(alpha, score)
        
        return best_move
    
    def _minimax(self, matrix: np.ndarray, depth: int, is_maximizing: bool,
                 alpha: float, beta: float) -> float:
        """Minimax algorithm with alpha-beta pruning."""
        winner = self.check_winner(matrix)
        
        if winner == self.player_symbol:
            return 10 - depth
        elif winner == self.opponent_symbol:
            return depth - 10
        elif winner == 0:  # Draw
            return 0
        
        if depth >= self.max_depth:
            return self._evaluate_position(matrix)
        
        empty_cells = self.get_empty_cells(matrix)
        
        if is_maximizing:
            max_score = float('-inf')
            for move in empty_cells:
                test_matrix = matrix.copy()
                test_matrix[move] = self.player_symbol
                score = self._minimax(test_matrix, depth + 1, False, alpha, beta)
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_score
        else:
            min_score = float('inf')
            for move in empty_cells:
                test_matrix = matrix.copy()
                test_matrix[move] = self.opponent_symbol
                score = self._minimax(test_matrix, depth + 1, True, alpha, beta)
                min_score = min(min_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score
    
    def _evaluate_position(self, matrix: np.ndarray) -> float:
        """Heuristic evaluation for positions when depth limit is reached."""
        score = 0
        size = matrix.shape[0]
        
        # Count how many winning lines each player threatens
        lines = self._get_all_lines(matrix)
        
        for line in lines:
            my_count = sum(1 for cell in line if cell == self.player_symbol)
            opp_count = sum(1 for cell in line if cell == self.opponent_symbol)
            
            if opp_count == 0 and my_count > 0:
                score += my_count ** 2
            elif my_count == 0 and opp_count > 0:
                score -= opp_count ** 2
        
        return score / 10.0  # Normalize
    
    def _get_all_lines(self, matrix: np.ndarray) -> List[List[int]]:
        """Get all rows, columns, and diagonals."""
        size = matrix.shape[0]
        lines = []
        
        # Rows
        for i in range(size):
            lines.append([matrix[i, j] for j in range(size)])
        
        # Columns
        for j in range(size):
            lines.append([matrix[i, j] for i in range(size)])
        
        # Diagonals
        lines.append([matrix[i, i] for i in range(size)])
        lines.append([matrix[i, size-1-i] for i in range(size)])
        
        return lines


class MonteCarloAI(BaseAI):
    """
    AI that uses Monte Carlo Tree Search (MCTS).
    Good for larger boards where minimax is too slow.
    """
    
    def __init__(self, player_symbol: int, simulations: int = 1000):
        super().__init__(player_symbol)
        self.name = "MonteCarloAI"
        self.simulations = simulations
    
    def get_move(self, matrix: np.ndarray) -> Tuple[int, int]:
        """Get the best move using Monte Carlo simulations."""
        empty_cells = self.get_empty_cells(matrix)
        if not empty_cells:
            return (-1, -1)
        
        # Adjust simulations based on board size
        size = matrix.shape[0]
        sims_per_move = max(50, self.simulations // len(empty_cells))
        
        move_scores = {}
        
        for move in empty_cells:
            wins = 0
            for _ in range(sims_per_move):
                result = self._simulate_game(matrix, move)
                if result == self.player_symbol:
                    wins += 2
                elif result == 0:  # Draw
                    wins += 1
            move_scores[move] = wins
        
        # Return move with highest win rate
        best_move = max(move_scores, key=move_scores.get)
        return best_move
    
    def _simulate_game(self, matrix: np.ndarray, first_move: Tuple[int, int]) -> int:
        """Simulate a random game from current position."""
        sim_matrix = matrix.copy()
        sim_matrix[first_move] = self.player_symbol
        
        current_player = self.opponent_symbol
        
        while True:
            winner = self.check_winner(sim_matrix)
            if winner is not None:
                return winner
            
            empty = self.get_empty_cells(sim_matrix)
            if not empty:
                return 0
            
            move = choice(empty)
            sim_matrix[move] = current_player
            current_player = 1 if current_player == 2 else 2


class StrategicAI(BaseAI):
    """
    AI that uses strategic rules: block wins, take wins, control center/corners.
    A middle-ground between random and minimax.
    """
    
    def __init__(self, player_symbol: int):
        super().__init__(player_symbol)
        self.name = "StrategicAI"
    
    def get_move(self, matrix: np.ndarray) -> Tuple[int, int]:
        """Get move using strategic rules."""
        size = matrix.shape[0]
        empty_cells = self.get_empty_cells(matrix)
        
        if not empty_cells:
            return (-1, -1)
        
        # 1. Check for winning move
        for move in empty_cells:
            test_matrix = matrix.copy()
            test_matrix[move] = self.player_symbol
            if self.check_winner(test_matrix) == self.player_symbol:
                return move
        
        # 2. Block opponent's winning move
        for move in empty_cells:
            test_matrix = matrix.copy()
            test_matrix[move] = self.opponent_symbol
            if self.check_winner(test_matrix) == self.opponent_symbol:
                return move
        
        # 3. Take center if available
        center = size // 2
        if (center, center) in empty_cells:
            return (center, center)
        
        # 4. Take corners
        corners = [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]
        available_corners = [c for c in corners if c in empty_cells]
        if available_corners:
            return choice(available_corners)
        
        # 5. Take any edge
        return choice(empty_cells)


class AggressiveAI(BaseAI):
    """
    AI that aggressively builds winning threats.
    Prioritizes creating two-way wins over blocking.
    """
    
    def __init__(self, player_symbol: int):
        super().__init__(player_symbol)
        self.name = "AggressiveAI"
    
    def get_move(self, matrix: np.ndarray) -> Tuple[int, int]:
        """Get move using aggressive strategy."""
        empty_cells = self.get_empty_cells(matrix)
        
        if not empty_cells:
            return (-1, -1)
        
        # 1. Win if possible
        for move in empty_cells:
            test_matrix = matrix.copy()
            test_matrix[move] = self.player_symbol
            if self.check_winner(test_matrix) == self.player_symbol:
                return move
        
        # 2. Block ONLY if opponent can win next move
        for move in empty_cells:
            test_matrix = matrix.copy()
            test_matrix[move] = self.opponent_symbol
            if self.check_winner(test_matrix) == self.opponent_symbol:
                return move
        
        # 3. Find move that creates most threats
        best_move = empty_cells[0]
        best_threat_count = -1
        
        for move in empty_cells:
            test_matrix = matrix.copy()
            test_matrix[move] = self.player_symbol
            threat_count = self._count_threats(test_matrix)
            
            if threat_count > best_threat_count:
                best_threat_count = threat_count
                best_move = move
        
        return best_move
    
    def _count_threats(self, matrix: np.ndarray) -> int:
        """Count how many lines have potential wins (n-1 in a row with empty)."""
        size = matrix.shape[0]
        threats = 0
        
        # Check all lines
        lines_coords = self._get_all_lines_coords(size)
        
        for line_coords in lines_coords:
            line = [matrix[coord] for coord in line_coords]
            my_count = sum(1 for cell in line if cell == self.player_symbol)
            empty_count = sum(1 for cell in line if cell == 0)
            opp_count = sum(1 for cell in line if cell == self.opponent_symbol)
            
            # A threat is n-1 of my symbols with 1 empty and no opponent
            if my_count == size - 1 and empty_count == 1 and opp_count == 0:
                threats += 2  # Immediate threat
            elif my_count >= size // 2 and opp_count == 0:
                threats += 1  # Building threat
        
        return threats
    
    def _get_all_lines_coords(self, size: int) -> List[List[Tuple[int, int]]]:
        """Get coordinates of all lines (rows, cols, diags)."""
        lines = []
        
        # Rows
        for i in range(size):
            lines.append([(i, j) for j in range(size)])
        
        # Columns
        for j in range(size):
            lines.append([(i, j) for i in range(size)])
        
        # Diagonals
        lines.append([(i, i) for i in range(size)])
        lines.append([(i, size-1-i) for i in range(size)])
        
        return lines


# Factory function to create AI by name
def create_ai(name: str, player_symbol: int, **kwargs) -> BaseAI:
    """
    Factory function to create AI instances by name.
    
    :param name: AI type - 'random', 'minimax', 'montecarlo', 'strategic', 'aggressive'
    :param player_symbol: 1 or 2
    :param kwargs: Additional arguments for specific AIs
    :return: AI instance
    """
    ai_classes = {
        'random': RandomAI,
        'minimax': MinimaxAI,
        'montecarlo': MonteCarloAI,
        'strategic': StrategicAI,
        'aggressive': AggressiveAI,
    }
    
    name_lower = name.lower()
    if name_lower not in ai_classes:
        raise ValueError(f"Unknown AI type: {name}. Available: {list(ai_classes.keys())}")
    
    return ai_classes[name_lower](player_symbol, **kwargs) if kwargs else ai_classes[name_lower](player_symbol)


# List of all available AI types
AI_TYPES = ['random', 'minimax', 'montecarlo', 'strategic', 'aggressive']
