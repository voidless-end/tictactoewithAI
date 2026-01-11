# File: ai_battle_arena.py
# AI vs AI Battle Arena - Run tournaments between different AI strategies

import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
import time
import json

from ai_strategies import BaseAI, create_ai, AI_TYPES


@dataclass
class GameResult:
    """Stores the result of a single game."""
    winner: int  # 0 for draw, 1 or 2 for player
    ai1_name: str
    ai2_name: str
    board_size: int
    moves: List[Tuple[int, int, int]]  # (row, col, player)
    final_board: np.ndarray
    game_duration: float
    total_moves: int
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'winner': self.winner,
            'ai1_name': self.ai1_name,
            'ai2_name': self.ai2_name,
            'board_size': self.board_size,
            'moves': self.moves,
            'final_board': self.final_board.tolist(),
            'game_duration': self.game_duration,
            'total_moves': self.total_moves
        }


@dataclass
class TournamentStats:
    """Statistics for a tournament of games."""
    ai1_name: str
    ai2_name: str
    board_size: int
    total_games: int
    ai1_wins: int = 0
    ai2_wins: int = 0
    draws: int = 0
    total_duration: float = 0.0
    games: List[GameResult] = field(default_factory=list)
    move_heatmap_player1: np.ndarray = None
    move_heatmap_player2: np.ndarray = None
    winning_move_heatmap: np.ndarray = None
    first_move_heatmap: np.ndarray = None
    
    def __post_init__(self):
        """Initialize heatmaps after creation."""
        if self.move_heatmap_player1 is None:
            self.move_heatmap_player1 = np.zeros((self.board_size, self.board_size))
        if self.move_heatmap_player2 is None:
            self.move_heatmap_player2 = np.zeros((self.board_size, self.board_size))
        if self.winning_move_heatmap is None:
            self.winning_move_heatmap = np.zeros((self.board_size, self.board_size))
        if self.first_move_heatmap is None:
            self.first_move_heatmap = np.zeros((self.board_size, self.board_size))
    
    @property
    def ai1_win_rate(self) -> float:
        return self.ai1_wins / self.total_games * 100 if self.total_games > 0 else 0
    
    @property
    def ai2_win_rate(self) -> float:
        return self.ai2_wins / self.total_games * 100 if self.total_games > 0 else 0
    
    @property
    def draw_rate(self) -> float:
        return self.draws / self.total_games * 100 if self.total_games > 0 else 0
    
    @property
    def avg_game_duration(self) -> float:
        return self.total_duration / self.total_games if self.total_games > 0 else 0
    
    @property
    def avg_moves_per_game(self) -> float:
        if not self.games:
            return 0
        return sum(g.total_moves for g in self.games) / len(self.games)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'ai1_name': self.ai1_name,
            'ai2_name': self.ai2_name,
            'board_size': self.board_size,
            'total_games': self.total_games,
            'ai1_wins': self.ai1_wins,
            'ai2_wins': self.ai2_wins,
            'draws': self.draws,
            'ai1_win_rate': self.ai1_win_rate,
            'ai2_win_rate': self.ai2_win_rate,
            'draw_rate': self.draw_rate,
            'avg_game_duration': self.avg_game_duration,
            'avg_moves_per_game': self.avg_moves_per_game,
            'total_duration': self.total_duration,
            'move_heatmap_player1': self.move_heatmap_player1.tolist(),
            'move_heatmap_player2': self.move_heatmap_player2.tolist(),
            'winning_move_heatmap': self.winning_move_heatmap.tolist(),
            'first_move_heatmap': self.first_move_heatmap.tolist()
        }
    
    def summary(self) -> str:
        """Generate a text summary of the tournament."""
        lines = [
            "=" * 60,
            f"TOURNAMENT SUMMARY: {self.ai1_name} vs {self.ai2_name}",
            "=" * 60,
            f"Board Size: {self.board_size}x{self.board_size}",
            f"Total Games: {self.total_games}",
            "-" * 60,
            f"  {self.ai1_name} (Player 1): {self.ai1_wins} wins ({self.ai1_win_rate:.1f}%)",
            f"  {self.ai2_name} (Player 2): {self.ai2_wins} wins ({self.ai2_win_rate:.1f}%)",
            f"  Draws: {self.draws} ({self.draw_rate:.1f}%)",
            "-" * 60,
            f"Average Game Duration: {self.avg_game_duration:.4f}s",
            f"Average Moves per Game: {self.avg_moves_per_game:.1f}",
            f"Total Tournament Time: {self.total_duration:.2f}s",
            "=" * 60
        ]
        return "\n".join(lines)


class AIBattleArena:
    """
    Battle arena for pitting AI strategies against each other.
    """
    
    def __init__(self, board_size: int = 3, verbose: bool = False):
        """
        Initialize the battle arena.
        
        :param board_size: Size of the tic-tac-toe board
        :param verbose: Whether to print game progress
        """
        self.board_size = board_size
        self.verbose = verbose
    
    def create_board(self) -> np.ndarray:
        """Create an empty game board."""
        return np.zeros((self.board_size, self.board_size), dtype=int)
    
    def check_winner(self, matrix: np.ndarray) -> Optional[int]:
        """
        Check if there's a winner.
        
        :return: 1 if player 1 wins, 2 if player 2 wins, 0 for draw, None for ongoing
        """
        size = matrix.shape[0]
        
        # Check rows
        for i in range(size):
            if matrix[i, 0] != 0 and all(matrix[i, j] == matrix[i, 0] for j in range(size)):
                return int(matrix[i, 0])
        
        # Check columns
        for j in range(size):
            if matrix[0, j] != 0 and all(matrix[i, j] == matrix[0, j] for i in range(size)):
                return int(matrix[0, j])
        
        # Check main diagonal
        if matrix[0, 0] != 0 and all(matrix[i, i] == matrix[0, 0] for i in range(size)):
            return int(matrix[0, 0])
        
        # Check anti-diagonal
        if matrix[0, size-1] != 0 and all(matrix[i, size-1-i] == matrix[0, size-1] for i in range(size)):
            return int(matrix[0, size-1])
        
        # Check for draw (no empty cells)
        if not np.any(matrix == 0):
            return 0
        
        return None  # Game ongoing
    
    def display_board(self, matrix: np.ndarray) -> None:
        """Display the board in console."""
        size = matrix.shape[0]
        print("-" * (2 * size + 1))
        for row in matrix:
            print(" ".join(str(int(cell)) for cell in row))
        print()
    
    def play_single_game(self, ai1: BaseAI, ai2: BaseAI) -> GameResult:
        """
        Play a single game between two AIs.
        
        :param ai1: AI playing as player 1 (goes first)
        :param ai2: AI playing as player 2
        :return: GameResult with all game data
        """
        board = self.create_board()
        moves = []
        current_player = 1
        ais = {1: ai1, 2: ai2}
        
        start_time = time.time()
        
        if self.verbose:
            print(f"\n🎮 Game: {ai1.name} (1) vs {ai2.name} (2)")
            self.display_board(board)
        
        while True:
            # Get move from current AI
            current_ai = ais[current_player]
            move = current_ai.get_move(board)
            
            if move == (-1, -1) or board[move] != 0:
                # Invalid move - shouldn't happen, but handle it
                break
            
            # Make the move
            board[move] = current_player
            moves.append((move[0], move[1], current_player))
            
            if self.verbose:
                print(f"Player {current_player} ({current_ai.name}) -> {move}")
                self.display_board(board)
            
            # Check for winner
            winner = self.check_winner(board)
            if winner is not None:
                duration = time.time() - start_time
                
                if self.verbose:
                    if winner == 0:
                        print("🤝 Draw!")
                    else:
                        print(f"🏆 Player {winner} ({ais[winner].name}) wins!")
                
                return GameResult(
                    winner=winner,
                    ai1_name=ai1.name,
                    ai2_name=ai2.name,
                    board_size=self.board_size,
                    moves=moves,
                    final_board=board.copy(),
                    game_duration=duration,
                    total_moves=len(moves)
                )
            
            # Switch player
            current_player = 2 if current_player == 1 else 1
        
        # Should never reach here
        duration = time.time() - start_time
        return GameResult(
            winner=0,
            ai1_name=ai1.name,
            ai2_name=ai2.name,
            board_size=self.board_size,
            moves=moves,
            final_board=board.copy(),
            game_duration=duration,
            total_moves=len(moves)
        )
    
    def run_tournament(self, ai1_type: str, ai2_type: str, 
                       num_games: int = 100,
                       swap_sides: bool = True) -> TournamentStats:
        """
        Run a tournament between two AI types.
        
        :param ai1_type: Type of first AI (e.g., 'random', 'minimax')
        :param ai2_type: Type of second AI
        :param num_games: Number of games to play
        :param swap_sides: If True, swap who goes first halfway through
        :return: TournamentStats with all results
        """
        stats = TournamentStats(
            ai1_name=ai1_type,
            ai2_name=ai2_type,
            board_size=self.board_size,
            total_games=num_games
        )
        
        games_per_side = num_games // 2 if swap_sides else num_games
        
        print(f"\n🏟️  Starting Tournament: {ai1_type} vs {ai2_type}")
        print(f"   Board: {self.board_size}x{self.board_size}, Games: {num_games}")
        print("-" * 50)
        
        start_time = time.time()
        
        # First half: ai1 goes first
        for i in range(games_per_side):
            ai1 = create_ai(ai1_type, 1)
            ai2 = create_ai(ai2_type, 2)
            
            result = self.play_single_game(ai1, ai2)
            self._update_stats(stats, result, ai1_first=True)
            
            if (i + 1) % max(1, num_games // 10) == 0:
                print(f"   Progress: {i + 1}/{num_games} games...")
        
        # Second half: ai2 goes first (if swap_sides)
        if swap_sides:
            for i in range(games_per_side, num_games):
                # Swap: ai2 plays as player 1 (goes first)
                ai2 = create_ai(ai2_type, 1)
                ai1 = create_ai(ai1_type, 2)
                
                result = self.play_single_game(ai2, ai1)
                self._update_stats(stats, result, ai1_first=False)
                
                if (i + 1) % max(1, num_games // 10) == 0:
                    print(f"   Progress: {i + 1}/{num_games} games...")
        
        stats.total_duration = time.time() - start_time
        
        print(stats.summary())
        
        return stats
    
    def _update_stats(self, stats: TournamentStats, result: GameResult, 
                      ai1_first: bool) -> None:
        """Update tournament statistics with a game result."""
        stats.games.append(result)
        
        # Determine actual winner from original AI perspective
        if ai1_first:
            if result.winner == 1:
                stats.ai1_wins += 1
            elif result.winner == 2:
                stats.ai2_wins += 1
            else:
                stats.draws += 1
        else:
            # AI positions were swapped
            if result.winner == 1:
                stats.ai2_wins += 1
            elif result.winner == 2:
                stats.ai1_wins += 1
            else:
                stats.draws += 1
        
        # Update heatmaps
        for row, col, player in result.moves:
            if ai1_first:
                if player == 1:
                    stats.move_heatmap_player1[row, col] += 1
                else:
                    stats.move_heatmap_player2[row, col] += 1
            else:
                # Swapped
                if player == 1:
                    stats.move_heatmap_player2[row, col] += 1
                else:
                    stats.move_heatmap_player1[row, col] += 1
        
        # Track first moves
        if result.moves:
            first_row, first_col, _ = result.moves[0]
            stats.first_move_heatmap[first_row, first_col] += 1
        
        # Track winning positions
        if result.winner != 0 and result.moves:
            last_row, last_col, _ = result.moves[-1]
            stats.winning_move_heatmap[last_row, last_col] += 1
    
    def run_round_robin(self, ai_types: List[str] = None, 
                        num_games: int = 100) -> Dict[str, TournamentStats]:
        """
        Run a round-robin tournament between all AI types.
        
        :param ai_types: List of AI types to include (default: all)
        :param num_games: Games per matchup
        :return: Dictionary mapping matchup names to stats
        """
        if ai_types is None:
            ai_types = AI_TYPES
        
        results = {}
        
        print("\n" + "=" * 60)
        print("🏆 ROUND ROBIN TOURNAMENT")
        print("=" * 60)
        print(f"Participants: {', '.join(ai_types)}")
        print(f"Games per matchup: {num_games}")
        print("=" * 60)
        
        for i, ai1 in enumerate(ai_types):
            for ai2 in ai_types[i+1:]:
                matchup_name = f"{ai1}_vs_{ai2}"
                stats = self.run_tournament(ai1, ai2, num_games)
                results[matchup_name] = stats
        
        # Print final standings
        self._print_round_robin_summary(results, ai_types)
        
        return results
    
    def _print_round_robin_summary(self, results: Dict[str, TournamentStats],
                                    ai_types: List[str]) -> None:
        """Print summary of round robin tournament."""
        # Calculate total wins for each AI
        win_counts = {ai: 0 for ai in ai_types}
        game_counts = {ai: 0 for ai in ai_types}
        
        for matchup, stats in results.items():
            win_counts[stats.ai1_name] += stats.ai1_wins
            win_counts[stats.ai2_name] += stats.ai2_wins
            game_counts[stats.ai1_name] += stats.total_games
            game_counts[stats.ai2_name] += stats.total_games
        
        # Sort by win count
        rankings = sorted(win_counts.items(), key=lambda x: -x[1])
        
        print("\n" + "=" * 60)
        print("📊 FINAL STANDINGS")
        print("=" * 60)
        for rank, (ai, wins) in enumerate(rankings, 1):
            games = game_counts[ai]
            win_rate = wins / games * 100 if games > 0 else 0
            print(f"  {rank}. {ai}: {wins} wins ({win_rate:.1f}%)")
        print("=" * 60)


def quick_battle(ai1: str, ai2: str, board_size: int = 3, 
                 num_games: int = 100, verbose: bool = False) -> TournamentStats:
    """
    Convenience function to quickly run an AI battle.
    
    :param ai1: First AI type
    :param ai2: Second AI type
    :param board_size: Board size
    :param num_games: Number of games
    :param verbose: Print game-by-game output
    :return: Tournament statistics
    """
    arena = AIBattleArena(board_size=board_size, verbose=verbose)
    return arena.run_tournament(ai1, ai2, num_games)


if __name__ == "__main__":
    # Demo: Run a quick tournament
    print("🤖 AI Battle Arena Demo")
    print("Available AI types:", AI_TYPES)
    
    # Quick battle
    stats = quick_battle('random', 'minimax', board_size=3, num_games=50)
