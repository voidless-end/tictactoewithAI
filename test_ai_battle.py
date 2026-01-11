# File: test_ai_battle.py
# Automated tests for AI strategies, battle arena, and statistics

import pytest
import numpy as np
import os
import tempfile
import shutil

from ai_strategies import (
    BaseAI, RandomAI, MinimaxAI, MonteCarloAI, StrategicAI, AggressiveAI,
    create_ai, AI_TYPES
)
from ai_battle_arena import AIBattleArena, GameResult, TournamentStats, quick_battle
from ai_statistics import BattleStatistics


# ============================================================================
# AI Strategies Tests
# ============================================================================

class TestBaseAI:
    """Tests for BaseAI utility methods."""
    
    def test_get_empty_cells_empty_board(self):
        """Empty board should return all cells."""
        ai = RandomAI(1)
        board = np.zeros((3, 3), dtype=int)
        empty = ai.get_empty_cells(board)
        assert len(empty) == 9
    
    def test_get_empty_cells_partial_board(self):
        """Partial board should return only empty cells."""
        ai = RandomAI(1)
        board = np.array([[1, 0, 2], [0, 1, 0], [2, 0, 0]], dtype=int)
        empty = ai.get_empty_cells(board)
        assert len(empty) == 5
        assert (0, 0) not in empty
        assert (0, 1) in empty
    
    def test_get_empty_cells_full_board(self):
        """Full board should return no cells."""
        ai = RandomAI(1)
        board = np.array([[1, 2, 1], [2, 1, 2], [2, 1, 2]], dtype=int)
        empty = ai.get_empty_cells(board)
        assert len(empty) == 0
    
    def test_check_winner_row(self):
        """Detect row win."""
        ai = RandomAI(1)
        board = np.array([[1, 1, 1], [0, 2, 0], [2, 0, 0]], dtype=int)
        assert ai.check_winner(board) == 1
    
    def test_check_winner_column(self):
        """Detect column win."""
        ai = RandomAI(1)
        board = np.array([[2, 1, 0], [2, 1, 0], [2, 0, 1]], dtype=int)
        assert ai.check_winner(board) == 2
    
    def test_check_winner_diagonal(self):
        """Detect diagonal win."""
        ai = RandomAI(1)
        board = np.array([[1, 2, 0], [2, 1, 0], [0, 0, 1]], dtype=int)
        assert ai.check_winner(board) == 1
    
    def test_check_winner_anti_diagonal(self):
        """Detect anti-diagonal win."""
        ai = RandomAI(1)
        board = np.array([[0, 2, 1], [2, 1, 0], [1, 0, 2]], dtype=int)
        assert ai.check_winner(board) == 1
    
    def test_check_winner_draw(self):
        """Detect draw (full board, no winner)."""
        ai = RandomAI(1)
        board = np.array([[1, 2, 1], [1, 2, 2], [2, 1, 1]], dtype=int)
        assert ai.check_winner(board) == 0
    
    def test_check_winner_ongoing(self):
        """Detect ongoing game."""
        ai = RandomAI(1)
        board = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 0]], dtype=int)
        assert ai.check_winner(board) is None

    arena = AIBattleArena(board_size=board_size, verbose=verbose)
    return arena.run_tournament(ai1, ai2, num_games)


class TestRandomAI:
    """Tests for RandomAI."""
    
    def test_random_ai_returns_valid_move(self):
        """RandomAI should return a valid empty cell."""
        ai = RandomAI(1)
        board = np.array([[1, 0, 2], [0, 1, 0], [2, 0, 0]], dtype=int)
        move = ai.get_move(board)
        assert board[move] == 0
    
    def test_random_ai_full_board(self):
        """RandomAI should return (-1, -1) on full board."""
        ai = RandomAI(1)
        board = np.array([[1, 2, 1], [2, 1, 2], [2, 1, 2]], dtype=int)
        move = ai.get_move(board)
        assert move == (-1, -1)
    
    def test_random_ai_name(self):
        """RandomAI should have correct name."""
        ai = RandomAI(1)
        assert ai.name == "RandomAI"


class TestMinimaxAI:
    """Tests for MinimaxAI."""
    
    def test_minimax_takes_winning_move(self):
        """MinimaxAI should take immediate winning move."""
        ai = MinimaxAI(1)
        board = np.array([[1, 1, 0], [2, 2, 0], [0, 0, 0]], dtype=int)
        move = ai.get_move(board)
        assert move == (0, 2)  # Win by completing row
    
    def test_minimax_blocks_opponent_win(self):
        """MinimaxAI should block opponent winning move."""
        ai = MinimaxAI(1)
        board = np.array([[2, 2, 0], [1, 0, 0], [0, 0, 1]], dtype=int)
        move = ai.get_move(board)
        assert move == (0, 2)  # Block opponent's row win
    
    def test_minimax_returns_valid_move(self):
        """MinimaxAI should always return valid move."""
        ai = MinimaxAI(1)
        board = np.zeros((3, 3), dtype=int)
        move = ai.get_move(board)
        assert 0 <= move[0] < 3
        assert 0 <= move[1] < 3
    
    def test_minimax_name(self):
        """MinimaxAI should have correct name."""
        ai = MinimaxAI(1)
        assert ai.name == "MinimaxAI"


class TestMonteCarloAI:
    """Tests for MonteCarloAI."""
    
    def test_montecarlo_returns_valid_move(self):
        """MonteCarloAI should return valid move."""
        ai = MonteCarloAI(1, simulations=100)
        board = np.array([[1, 0, 2], [0, 0, 0], [0, 0, 0]], dtype=int)
        move = ai.get_move(board)
        assert board[move] == 0
    
    def test_montecarlo_takes_winning_move(self):
        """MonteCarloAI should likely take winning move."""
        ai = MonteCarloAI(1, simulations=500)
        board = np.array([[1, 1, 0], [2, 2, 0], [0, 0, 0]], dtype=int)
        move = ai.get_move(board)
        # Should take the winning move most of the time
        assert move == (0, 2)
    
    def test_montecarlo_name(self):
        """MonteCarloAI should have correct name."""
        ai = MonteCarloAI(1)
        assert ai.name == "MonteCarloAI"


class TestStrategicAI:
    """Tests for StrategicAI."""
    
    def test_strategic_takes_winning_move(self):
        """StrategicAI should take winning move."""
        ai = StrategicAI(1)
        board = np.array([[1, 1, 0], [2, 2, 0], [0, 0, 0]], dtype=int)
        move = ai.get_move(board)
        assert move == (0, 2)
    
    def test_strategic_blocks_opponent(self):
        """StrategicAI should block opponent win."""
        ai = StrategicAI(1)
        board = np.array([[2, 2, 0], [1, 0, 0], [0, 0, 1]], dtype=int)
        move = ai.get_move(board)
        assert move == (0, 2)
    
    def test_strategic_takes_center(self):
        """StrategicAI should prefer center on empty board."""
        ai = StrategicAI(1)
        board = np.zeros((3, 3), dtype=int)
        move = ai.get_move(board)
        assert move == (1, 1)
    
    def test_strategic_name(self):
        """StrategicAI should have correct name."""
        ai = StrategicAI(1)
        assert ai.name == "StrategicAI"


class TestAggressiveAI:
    """Tests for AggressiveAI."""
    
    def test_aggressive_takes_winning_move(self):
        """AggressiveAI should take winning move."""
        ai = AggressiveAI(1)
        board = np.array([[1, 1, 0], [2, 2, 0], [0, 0, 0]], dtype=int)
        move = ai.get_move(board)
        assert move == (0, 2)
    
    def test_aggressive_blocks_immediate_loss(self):
        """AggressiveAI should block immediate loss."""
        ai = AggressiveAI(1)
        board = np.array([[2, 2, 0], [1, 0, 0], [0, 0, 1]], dtype=int)
        move = ai.get_move(board)
        assert move == (0, 2)
    
    def test_aggressive_name(self):
        """AggressiveAI should have correct name."""
        ai = AggressiveAI(1)
        assert ai.name == "AggressiveAI"


class TestCreateAI:
    """Tests for AI factory function."""
    
    def test_create_all_ai_types(self):
        """Should create all AI types successfully."""
        for ai_type in AI_TYPES:
            ai = create_ai(ai_type, 1)
            assert ai is not None
            assert ai.player_symbol == 1
    
    def test_create_ai_player_2(self):
        """Should create AI for player 2."""
        ai = create_ai('random', 2)
        assert ai.player_symbol == 2
        assert ai.opponent_symbol == 1
    
    def test_create_ai_invalid_type(self):
        """Should raise error for invalid AI type."""
        with pytest.raises(ValueError):
            create_ai('invalid_ai', 1)
    
    def test_ai_types_list(self):
        """AI_TYPES should contain expected strategies."""
        assert 'random' in AI_TYPES
        assert 'minimax' in AI_TYPES
        assert 'montecarlo' in AI_TYPES
        assert 'strategic' in AI_TYPES
        assert 'aggressive' in AI_TYPES


# ============================================================================
# Battle Arena Tests
# ============================================================================

class TestAIBattleArena:
    """Tests for AIBattleArena."""
    
    def test_create_board(self):
        """Should create empty board of correct size."""
        arena = AIBattleArena(board_size=3)
        board = arena.create_board()
        assert board.shape == (3, 3)
        assert np.all(board == 0)
    
    def test_create_board_larger(self):
        """Should create larger boards."""
        arena = AIBattleArena(board_size=5)
        board = arena.create_board()
        assert board.shape == (5, 5)
    
    def test_check_winner_row(self):
        """Arena should detect row win."""
        arena = AIBattleArena(board_size=3)
        board = np.array([[1, 1, 1], [0, 2, 0], [2, 0, 0]], dtype=int)
        assert arena.check_winner(board) == 1
    
    def test_check_winner_draw(self):
        """Arena should detect draw."""
        arena = AIBattleArena(board_size=3)
        board = np.array([[1, 2, 1], [1, 2, 2], [2, 1, 1]], dtype=int)
        assert arena.check_winner(board) == 0
    
    def test_play_single_game(self):
        """Should play complete game and return result."""
        arena = AIBattleArena(board_size=3, verbose=False)
        ai1 = RandomAI(1)
        ai2 = RandomAI(2)
        result = arena.play_single_game(ai1, ai2)
        
        assert isinstance(result, GameResult)
        assert result.winner in [0, 1, 2]
        assert result.board_size == 3
        assert len(result.moves) > 0
        assert result.total_moves == len(result.moves)
        assert result.game_duration >= 0
    
    def test_run_tournament(self):
        """Should run tournament and return stats."""
        arena = AIBattleArena(board_size=3, verbose=False)
        stats = arena.run_tournament('random', 'random', num_games=10)
        
        assert isinstance(stats, TournamentStats)
        assert stats.total_games == 10
        assert stats.ai1_wins + stats.ai2_wins + stats.draws == 10
        assert len(stats.games) == 10
    
    def test_tournament_heatmaps_populated(self):
        """Tournament should populate heatmaps."""
        arena = AIBattleArena(board_size=3, verbose=False)
        stats = arena.run_tournament('random', 'random', num_games=20)
        
        assert np.sum(stats.move_heatmap_player1) > 0
        assert np.sum(stats.move_heatmap_player2) > 0
        assert np.sum(stats.first_move_heatmap) > 0


class TestTournamentStats:
    """Tests for TournamentStats dataclass."""
    
    def test_stats_initialization(self):
        """Stats should initialize with correct defaults."""
        stats = TournamentStats(
            ai1_name='test1', ai2_name='test2',
            board_size=3, total_games=100
        )
        assert stats.ai1_wins == 0
        assert stats.ai2_wins == 0
        assert stats.draws == 0
        assert stats.move_heatmap_player1.shape == (3, 3)
    
    def test_win_rate_calculation(self):
        """Win rates should calculate correctly."""
        stats = TournamentStats(
            ai1_name='test1', ai2_name='test2',
            board_size=3, total_games=100
        )
        stats.ai1_wins = 60
        stats.ai2_wins = 30
        stats.draws = 10
        
        assert stats.ai1_win_rate == 60.0
        assert stats.ai2_win_rate == 30.0
        assert stats.draw_rate == 10.0
    
    def test_stats_to_dict(self):
        """Stats should convert to dictionary."""
        stats = TournamentStats(
            ai1_name='test1', ai2_name='test2',
            board_size=3, total_games=10
        )
        d = stats.to_dict()
        assert 'ai1_name' in d
        assert 'ai2_name' in d
        assert 'move_heatmap_player1' in d


class TestGameResult:
    """Tests for GameResult dataclass."""
    
    def test_game_result_creation(self):
        """GameResult should store all fields."""
        board = np.zeros((3, 3), dtype=int)
        result = GameResult(
            winner=1,
            ai1_name='test1',
            ai2_name='test2',
            board_size=3,
            moves=[(0, 0, 1), (1, 1, 2)],
            final_board=board,
            game_duration=0.5,
            total_moves=2
        )
        assert result.winner == 1
        assert result.total_moves == 2
    
    def test_game_result_to_dict(self):
        """GameResult should convert to dictionary."""
        board = np.zeros((3, 3), dtype=int)
        result = GameResult(
            winner=1, ai1_name='test1', ai2_name='test2',
            board_size=3, moves=[], final_board=board,
            game_duration=0.1, total_moves=0
        )
        d = result.to_dict()
        assert d['winner'] == 1
        assert 'final_board' in d


class TestQuickBattle:
    """Tests for quick_battle convenience function."""
    
    def test_quick_battle(self):
        """quick_battle should run and return stats."""
        stats = quick_battle('random', 'random', board_size=3, num_games=5)
        assert isinstance(stats, TournamentStats)
        assert stats.total_games == 5


# ============================================================================
# Statistics & Visualization Tests
# ============================================================================

class TestBattleStatistics:
    """Tests for BattleStatistics visualization class."""
    
    @pytest.fixture
    def temp_output_dir(self):
        """Create temporary directory for test outputs."""
        dirpath = tempfile.mkdtemp()
        yield dirpath
        shutil.rmtree(dirpath)
    
    @pytest.fixture
    def sample_stats(self):
        """Create sample tournament stats for testing."""
        stats = TournamentStats(
            ai1_name='random', ai2_name='minimax',
            board_size=3, total_games=5
        )
        # Add some dummy games
        for i in range(5):
            board = np.zeros((3, 3), dtype=int)
            board[0, 0] = 1
            result = GameResult(
                winner=1 if i % 2 == 0 else 2,
                ai1_name='random', ai2_name='minimax',
                board_size=3,
                moves=[(0, 0, 1), (1, 1, 2), (0, 1, 1)],
                final_board=board,
                game_duration=0.01 + i * 0.001,
                total_moves=3
            )
            stats.games.append(result)
            stats.move_heatmap_player1[0, 0] += 1
            stats.move_heatmap_player1[0, 1] += 1
            stats.move_heatmap_player2[1, 1] += 1
            stats.first_move_heatmap[0, 0] += 1
            if result.winner != 0:
                stats.winning_move_heatmap[0, 1] += 1
        
        stats.ai1_wins = 3
        stats.ai2_wins = 2
        stats.draws = 0
        stats.total_duration = 0.05
        return stats
    
    def test_statistics_init(self, temp_output_dir):
        """BattleStatistics should initialize correctly."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        assert os.path.exists(temp_output_dir)
    
    def test_plot_move_heatmaps(self, temp_output_dir, sample_stats):
        """Should generate move heatmaps without error."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        fig, path = bs.plot_move_heatmaps(sample_stats, save=True, show=False)
        assert fig is not None
        assert path is not None
        assert os.path.exists(path)
    
    def test_plot_winning_positions(self, temp_output_dir, sample_stats):
        """Should generate winning positions heatmap."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        fig, path = bs.plot_winning_positions(sample_stats, save=True, show=False)
        assert fig is not None
        assert path is not None
    
    def test_plot_first_moves(self, temp_output_dir, sample_stats):
        """Should generate first moves heatmap."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        fig, path = bs.plot_first_moves(sample_stats, save=True, show=False)
        assert fig is not None
        assert path is not None
    
    def test_plot_win_rates(self, temp_output_dir, sample_stats):
        """Should generate win rates chart."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        fig, path = bs.plot_win_rates(sample_stats, save=True, show=False)
        assert fig is not None
        assert path is not None
    
    def test_plot_game_durations(self, temp_output_dir, sample_stats):
        """Should generate game duration histogram."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        fig, path = bs.plot_game_durations(sample_stats, save=True, show=False)
        assert fig is not None
        assert path is not None
    
    def test_plot_summary_dashboard(self, temp_output_dir, sample_stats):
        """Should generate summary dashboard."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        fig, path = bs.plot_summary_dashboard(sample_stats, save=True, show=False)
        assert fig is not None
        assert path is not None
    
    def test_save_stats_json(self, temp_output_dir, sample_stats):
        """Should save stats to JSON file."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        path = bs.save_stats_json(sample_stats)
        assert os.path.exists(path)
        assert path.endswith('.json')
    
    def test_generate_report(self, temp_output_dir, sample_stats):
        """Should generate text report."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        report = bs.generate_report(sample_stats)
        assert 'random' in report
        assert 'minimax' in report
        assert 'CONFIGURATION' in report
    
    def test_empty_stats_handling(self, temp_output_dir):
        """Should handle empty stats gracefully."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        stats = TournamentStats(
            ai1_name='a', ai2_name='b',
            board_size=3, total_games=0
        )
        # Should not raise exceptions
        fig, path = bs.plot_game_durations(stats, save=False, show=False)
        assert fig is not None
    
    def test_generate_all_visualizations(self, temp_output_dir, sample_stats):
        """Should generate all visualizations."""
        bs = BattleStatistics(output_dir=temp_output_dir)
        saved = bs.generate_all_visualizations(sample_stats, save=True, show=False)
        assert len(saved) > 0
        for path in saved.values():
            assert os.path.exists(path)


class TestRoundRobinVisualization:
    """Tests for round robin visualization."""
    
    @pytest.fixture
    def temp_output_dir(self):
        dirpath = tempfile.mkdtemp()
        yield dirpath
        shutil.rmtree(dirpath)
    
    def test_round_robin_plot(self, temp_output_dir):
        """Should generate round robin results plot."""
        # Create minimal round robin results
        results = {}
        for matchup in ['random_vs_strategic']:
            stats = TournamentStats(
                ai1_name='random', ai2_name='strategic',
                board_size=3, total_games=2
            )
            stats.ai1_wins = 1
            stats.ai2_wins = 1
            results[matchup] = stats
        
        bs = BattleStatistics(output_dir=temp_output_dir)
        fig, path = bs.plot_round_robin_results(results, save=True, show=False)
        assert fig is not None


# ============================================================================
# Integration Tests
# ============================================================================

class TestIntegration:
    """Integration tests for the full system."""
    
    def test_full_tournament_flow(self):
        """Test complete tournament flow from start to finish."""
        # Run tournament
        arena = AIBattleArena(board_size=3, verbose=False)
        stats = arena.run_tournament('random', 'strategic', num_games=10)
        
        # Verify results
        assert stats.total_games == 10
        assert stats.ai1_wins + stats.ai2_wins + stats.draws == 10
        
        # Verify heatmaps
        assert stats.move_heatmap_player1.shape == (3, 3)
        assert np.sum(stats.move_heatmap_player1) > 0
    
    def test_minimax_vs_random_dominance(self):
        """Minimax should dominate random on 3x3 board."""
        arena = AIBattleArena(board_size=3, verbose=False)
        stats = arena.run_tournament('minimax', 'random', num_games=20)
        
        # Minimax should win or draw most games
        minimax_success = stats.ai1_wins + stats.draws
        assert minimax_success >= 15  # At least 75% success rate
    
    def test_larger_board_tournament(self):
        """Tournament should work on larger boards."""
        arena = AIBattleArena(board_size=4, verbose=False)
        stats = arena.run_tournament('random', 'strategic', num_games=5)
        
        assert stats.board_size == 4
        assert stats.move_heatmap_player1.shape == (4, 4)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
