# File: ai_statistics.py
# Statistics and visualization for AI battles - including heat maps

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import os
import json

from ai_battle_arena import TournamentStats, GameResult


class BattleStatistics:
    """
    Comprehensive statistics analysis and visualization for AI battles.
    """
    
    def __init__(self, output_dir: str = "ai_battle_results"):
        """
        Initialize statistics analyzer.
        
        :param output_dir: Directory to save results and visualizations
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def generate_all_visualizations(self, stats: TournamentStats, 
                                    save: bool = True, show: bool = True) -> Dict[str, str]:
        """
        Generate all visualizations for a tournament.
        
        :param stats: Tournament statistics
        :param save: Save figures to files
        :param show: Display figures
        :return: Dictionary of saved file paths
        """
        saved_files = {}
        
        # 1. Move heat maps
        fig, path = self.plot_move_heatmaps(stats, save, show)
        if path:
            saved_files['move_heatmaps'] = path
        
        # 2. Winning positions heat map
        fig, path = self.plot_winning_positions(stats, save, show)
        if path:
            saved_files['winning_positions'] = path
        
        # 3. First move distribution
        fig, path = self.plot_first_moves(stats, save, show)
        if path:
            saved_files['first_moves'] = path
        
        # 4. Win rate comparison
        fig, path = self.plot_win_rates(stats, save, show)
        if path:
            saved_files['win_rates'] = path
        
        # 5. Game duration analysis
        fig, path = self.plot_game_durations(stats, save, show)
        if path:
            saved_files['game_durations'] = path
        
        # 6. Combined summary
        fig, path = self.plot_summary_dashboard(stats, save, show)
        if path:
            saved_files['summary_dashboard'] = path
        
        return saved_files
    
    def plot_move_heatmaps(self, stats: TournamentStats,
                          save: bool = True, show: bool = True) -> Tuple[plt.Figure, Optional[str]]:
        """
        Create heat maps showing where each AI prefers to play.
        """
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # Player 1 heat map
        ax1 = axes[0]
        heatmap1 = stats.move_heatmap_player1
        im1 = ax1.imshow(heatmap1, cmap='Reds', interpolation='nearest')
        ax1.set_title(f'{stats.ai1_name} Move Distribution\n(All moves made)', fontsize=12)
        self._add_heatmap_labels(ax1, heatmap1)
        plt.colorbar(im1, ax=ax1, label='Move Count')
        
        # Player 2 heat map
        ax2 = axes[1]
        heatmap2 = stats.move_heatmap_player2
        im2 = ax2.imshow(heatmap2, cmap='Blues', interpolation='nearest')
        ax2.set_title(f'{stats.ai2_name} Move Distribution\n(All moves made)', fontsize=12)
        self._add_heatmap_labels(ax2, heatmap2)
        plt.colorbar(im2, ax=ax2, label='Move Count')
        
        fig.suptitle(f'Move Heat Maps: {stats.ai1_name} vs {stats.ai2_name}\n'
                    f'({stats.total_games} games on {stats.board_size}x{stats.board_size} board)',
                    fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        
        path = None
        if save:
            path = os.path.join(self.output_dir, 
                               f'heatmap_moves_{stats.ai1_name}_vs_{stats.ai2_name}_{self.timestamp}.png')
            fig.savefig(path, dpi=150, bbox_inches='tight')
            print(f"📊 Saved: {path}")
        
        if show:
            plt.show()
        else:
            plt.close(fig)
        
        return fig, path
    
    def plot_winning_positions(self, stats: TournamentStats,
                               save: bool = True, show: bool = True) -> Tuple[plt.Figure, Optional[str]]:
        """
        Heat map of positions where winning moves were made.
        """
        fig, ax = plt.subplots(figsize=(8, 7))
        
        heatmap = stats.winning_move_heatmap
        
        # Use a custom colormap for winning positions
        im = ax.imshow(heatmap, cmap='YlOrRd', interpolation='nearest')
        
        ax.set_title(f'Winning Move Positions\n{stats.ai1_name} vs {stats.ai2_name}\n'
                    f'({stats.total_games} games)', fontsize=12)
        
        self._add_heatmap_labels(ax, heatmap)
        plt.colorbar(im, ax=ax, label='Winning Moves Count')
        
        # Add grid
        ax.set_xticks(np.arange(-.5, stats.board_size, 1), minor=True)
        ax.set_yticks(np.arange(-.5, stats.board_size, 1), minor=True)
        ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
        
        plt.tight_layout()
        
        path = None
        if save:
            path = os.path.join(self.output_dir,
                               f'heatmap_winning_{stats.ai1_name}_vs_{stats.ai2_name}_{self.timestamp}.png')
            fig.savefig(path, dpi=150, bbox_inches='tight')
            print(f"📊 Saved: {path}")
        
        if show:
            plt.show()
        else:
            plt.close(fig)
        
        return fig, path
    
    def plot_first_moves(self, stats: TournamentStats,
                         save: bool = True, show: bool = True) -> Tuple[plt.Figure, Optional[str]]:
        """
        Heat map of first move preferences.
        """
        fig, ax = plt.subplots(figsize=(8, 7))
        
        heatmap = stats.first_move_heatmap
        
        im = ax.imshow(heatmap, cmap='Greens', interpolation='nearest')
        
        ax.set_title(f'First Move Distribution\n{stats.ai1_name} vs {stats.ai2_name}\n'
                    f'({stats.total_games} games)', fontsize=12)
        
        self._add_heatmap_labels(ax, heatmap)
        plt.colorbar(im, ax=ax, label='First Move Count')
        
        # Add grid
        ax.set_xticks(np.arange(-.5, stats.board_size, 1), minor=True)
        ax.set_yticks(np.arange(-.5, stats.board_size, 1), minor=True)
        ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
        
        plt.tight_layout()
        
        path = None
        if save:
            path = os.path.join(self.output_dir,
                               f'heatmap_first_{stats.ai1_name}_vs_{stats.ai2_name}_{self.timestamp}.png')
            fig.savefig(path, dpi=150, bbox_inches='tight')
            print(f"📊 Saved: {path}")
        
        if show:
            plt.show()
        else:
            plt.close(fig)
        
        return fig, path
    
    def plot_win_rates(self, stats: TournamentStats,
                       save: bool = True, show: bool = True) -> Tuple[plt.Figure, Optional[str]]:
        """
        Bar chart comparing win rates.
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        categories = [stats.ai1_name, stats.ai2_name, 'Draws']
        values = [stats.ai1_wins, stats.ai2_wins, stats.draws]
        percentages = [stats.ai1_win_rate, stats.ai2_win_rate, stats.draw_rate]
        colors = ['#e74c3c', '#3498db', '#95a5a6']
        
        bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=1.2)
        
        # Add value labels on bars
        for bar, val, pct in zip(bars, values, percentages):
            height = bar.get_height()
            ax.annotate(f'{val}\n({pct:.1f}%)',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3), textcoords="offset points",
                       ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        ax.set_ylabel('Number of Wins', fontsize=12)
        ax.set_title(f'Win Distribution\n{stats.ai1_name} vs {stats.ai2_name}\n'
                    f'({stats.total_games} games)', fontsize=14, fontweight='bold')
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.tight_layout()
        
        path = None
        if save:
            path = os.path.join(self.output_dir,
                               f'winrates_{stats.ai1_name}_vs_{stats.ai2_name}_{self.timestamp}.png')
            fig.savefig(path, dpi=150, bbox_inches='tight')
            print(f"📊 Saved: {path}")
        
        if show:
            plt.show()
        else:
            plt.close(fig)
        
        return fig, path
    
    def plot_game_durations(self, stats: TournamentStats,
                            save: bool = True, show: bool = True) -> Tuple[plt.Figure, Optional[str]]:
        """
        Histogram of game durations and moves per game.
        """
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Game durations
        durations = [g.game_duration * 1000 for g in stats.games]  # Convert to ms
        ax1 = axes[0]
        if durations:
            ax1.hist(durations, bins=30, color='#9b59b6', edgecolor='black', alpha=0.7)
            ax1.axvline(np.mean(durations), color='red', linestyle='--',
                       label=f'Mean: {np.mean(durations):.2f}ms')
            ax1.set_xlabel('Game Duration (ms)', fontsize=11)
            ax1.set_ylabel('Frequency', fontsize=11)
            ax1.set_title('Game Duration Distribution', fontsize=12)
            ax1.legend()
        else:
            ax1.text(0.5, 0.5, 'No game duration data', ha='center', va='center', transform=ax1.transAxes, fontsize=12)
            ax1.set_xticks([])
            ax1.set_yticks([])
        
        # Moves per game
        moves = [g.total_moves for g in stats.games]
        ax2 = axes[1]
        if moves:
            ax2.hist(moves, bins=range(min(moves), max(moves) + 2),
                    color='#1abc9c', edgecolor='black', alpha=0.7)
            ax2.axvline(np.mean(moves), color='red', linestyle='--',
                       label=f'Mean: {np.mean(moves):.1f}')
            ax2.set_xlabel('Moves per Game', fontsize=11)
            ax2.set_ylabel('Frequency', fontsize=11)
            ax2.set_title('Moves per Game Distribution', fontsize=12)
            ax2.legend()
        else:
            ax2.text(0.5, 0.5, 'No move data', ha='center', va='center', transform=ax2.transAxes, fontsize=12)
            ax2.set_xticks([])
            ax2.set_yticks([])
        
        fig.suptitle(f'Game Metrics: {stats.ai1_name} vs {stats.ai2_name}',
                    fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        
        path = None
        if save:
            path = os.path.join(self.output_dir,
                               f'durations_{stats.ai1_name}_vs_{stats.ai2_name}_{self.timestamp}.png')
            fig.savefig(path, dpi=150, bbox_inches='tight')
            print(f"📊 Saved: {path}")
        
        if show:
            plt.show()
        else:
            plt.close(fig)
        
        return fig, path
    
    def plot_summary_dashboard(self, stats: TournamentStats,
                               save: bool = True, show: bool = True) -> Tuple[plt.Figure, Optional[str]]:
        """
        Create a comprehensive dashboard with all key visualizations.
        """
        fig = plt.figure(figsize=(16, 12))
        
        # Create grid for subplots
        gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.3)
        
        # 1. Win rates pie chart (top left)
        ax1 = fig.add_subplot(gs[0, 0])
        sizes = [stats.ai1_wins, stats.ai2_wins, stats.draws]
        labels = [f'{stats.ai1_name}\n({stats.ai1_win_rate:.1f}%)',
                 f'{stats.ai2_name}\n({stats.ai2_win_rate:.1f}%)',
                 f'Draws\n({stats.draw_rate:.1f}%)']
        colors = ['#e74c3c', '#3498db', '#95a5a6']
        explode = (0.05, 0.05, 0)
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
               autopct=lambda pct: f'{int(pct/100*stats.total_games)}' if pct > 0 else '',
               shadow=True, startangle=90)
        ax1.set_title('Win Distribution', fontsize=12, fontweight='bold')
        
        # 2. Player 1 heat map (top middle)
        ax2 = fig.add_subplot(gs[0, 1])
        im2 = ax2.imshow(stats.move_heatmap_player1, cmap='Reds', interpolation='nearest')
        ax2.set_title(f'{stats.ai1_name} Moves', fontsize=11)
        self._add_heatmap_labels(ax2, stats.move_heatmap_player1, fontsize=8)
        plt.colorbar(im2, ax=ax2, shrink=0.8)
        
        # 3. Player 2 heat map (top right)
        ax3 = fig.add_subplot(gs[0, 2])
        im3 = ax3.imshow(stats.move_heatmap_player2, cmap='Blues', interpolation='nearest')
        ax3.set_title(f'{stats.ai2_name} Moves', fontsize=11)
        self._add_heatmap_labels(ax3, stats.move_heatmap_player2, fontsize=8)
        plt.colorbar(im3, ax=ax3, shrink=0.8)
        
        # 4. Winning positions heat map (middle left)
        ax4 = fig.add_subplot(gs[1, 0])
        im4 = ax4.imshow(stats.winning_move_heatmap, cmap='YlOrRd', interpolation='nearest')
        ax4.set_title('Winning Positions', fontsize=11)
        self._add_heatmap_labels(ax4, stats.winning_move_heatmap, fontsize=8)
        plt.colorbar(im4, ax=ax4, shrink=0.8)
        
        # 5. First moves heat map (middle center)
        ax5 = fig.add_subplot(gs[1, 1])
        im5 = ax5.imshow(stats.first_move_heatmap, cmap='Greens', interpolation='nearest')
        ax5.set_title('First Move Preferences', fontsize=11)
        self._add_heatmap_labels(ax5, stats.first_move_heatmap, fontsize=8)
        plt.colorbar(im5, ax=ax5, shrink=0.8)
        
        # 6. Stats summary text (middle right)
        ax6 = fig.add_subplot(gs[1, 2])
        ax6.axis('off')
        summary_text = (
            f"📊 TOURNAMENT STATISTICS\n"
            f"{'─' * 30}\n\n"
            f"Board Size: {stats.board_size}×{stats.board_size}\n"
            f"Total Games: {stats.total_games}\n\n"
            f"🔴 {stats.ai1_name}: {stats.ai1_wins} wins\n"
            f"🔵 {stats.ai2_name}: {stats.ai2_wins} wins\n"
            f"⚪ Draws: {stats.draws}\n\n"
            f"⏱️ Avg Duration: {stats.avg_game_duration*1000:.2f}ms\n"
            f"🎯 Avg Moves: {stats.avg_moves_per_game:.1f}\n"
            f"⌛ Total Time: {stats.total_duration:.2f}s"
        )
        ax6.text(0.1, 0.9, summary_text, transform=ax6.transAxes,
                fontsize=11, verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # 7. Moves histogram (bottom left + center)
        ax7 = fig.add_subplot(gs[2, :2])
        moves = [g.total_moves for g in stats.games]
        if moves:
            ax7.hist(moves, bins=range(min(moves), max(moves) + 2),
                    color='#1abc9c', edgecolor='black', alpha=0.7)
            ax7.axvline(np.mean(moves), color='red', linestyle='--', linewidth=2,
                       label=f'Mean: {np.mean(moves):.1f}')
            ax7.set_xlabel('Moves per Game', fontsize=11)
            ax7.set_ylabel('Frequency', fontsize=11)
            ax7.set_title('Game Length Distribution', fontsize=12)
            ax7.legend()
        else:
            ax7.text(0.5, 0.5, 'No game length data', ha='center', va='center', transform=ax7.transAxes, fontsize=12)
            ax7.set_xticks([])
            ax7.set_yticks([])
        
        # 8. Win progression (bottom right)
        ax8 = fig.add_subplot(gs[2, 2])
        n_games = len(stats.games)
        if n_games == 0:
            ax8.text(0.5, 0.5, 'No games played', ha='center', va='center', transform=ax8.transAxes, fontsize=12)
            ax8.set_xticks([])
            ax8.set_yticks([])
        else:
            cumulative_ai1 = np.cumsum([1 if g.winner == 1 else 0 for g in stats.games[:n_games//2]] +
                                       [1 if g.winner == 2 else 0 for g in stats.games[n_games//2:]])
            cumulative_ai2 = np.cumsum([1 if g.winner == 2 else 0 for g in stats.games[:n_games//2]] +
                                       [1 if g.winner == 1 else 0 for g in stats.games[n_games//2:]])
            ax8.plot(cumulative_ai1, color='#e74c3c', linewidth=2, label=stats.ai1_name)
            ax8.plot(cumulative_ai2, color='#3498db', linewidth=2, label=stats.ai2_name)
            ax8.set_xlabel('Game Number', fontsize=11)
            ax8.set_ylabel('Cumulative Wins', fontsize=11)
            ax8.set_title('Win Progression', fontsize=12)
            ax8.legend()
            ax8.grid(True, alpha=0.3)
        
        fig.suptitle(f'🏆 AI Battle Dashboard: {stats.ai1_name} vs {stats.ai2_name}',
                    fontsize=16, fontweight='bold', y=0.98)
        
        path = None
        if save:
            path = os.path.join(self.output_dir,
                               f'dashboard_{stats.ai1_name}_vs_{stats.ai2_name}_{self.timestamp}.png')
            fig.savefig(path, dpi=150, bbox_inches='tight')
            print(f"📊 Saved: {path}")
        
        if show:
            plt.show()
        else:
            plt.close(fig)
        
        return fig, path
    
    def plot_round_robin_results(self, results: Dict[str, TournamentStats],
                                  save: bool = True, show: bool = True) -> Tuple[plt.Figure, Optional[str]]:
        """
        Visualize results from a round-robin tournament.
        """
        # Extract all AI names
        ai_names = set()
        for stats in results.values():
            ai_names.add(stats.ai1_name)
            ai_names.add(stats.ai2_name)
        ai_names = sorted(list(ai_names))
        n_ais = len(ai_names)
        
        # Create win matrix
        win_matrix = np.zeros((n_ais, n_ais))
        
        for matchup, stats in results.items():
            i = ai_names.index(stats.ai1_name)
            j = ai_names.index(stats.ai2_name)
            win_matrix[i, j] = stats.ai1_win_rate
            win_matrix[j, i] = stats.ai2_win_rate
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 8))
        
        im = ax.imshow(win_matrix, cmap='RdYlGn', vmin=0, vmax=100)
        
        # Add labels
        ax.set_xticks(np.arange(n_ais))
        ax.set_yticks(np.arange(n_ais))
        ax.set_xticklabels(ai_names, rotation=45, ha='right')
        ax.set_yticklabels(ai_names)
        
        # Add text annotations
        for i in range(n_ais):
            for j in range(n_ais):
                if i != j:
                    text = ax.text(j, i, f'{win_matrix[i, j]:.1f}%',
                                  ha='center', va='center', fontsize=10,
                                  color='white' if win_matrix[i, j] > 50 else 'black')
                else:
                    ax.text(j, i, '-', ha='center', va='center', fontsize=12)
        
        ax.set_title('Round Robin Win Rates\n(Row AI vs Column AI)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Opponent', fontsize=12)
        ax.set_ylabel('AI', fontsize=12)
        
        plt.colorbar(im, ax=ax, label='Win Rate (%)')
        plt.tight_layout()
        
        path = None
        if save:
            path = os.path.join(self.output_dir, f'round_robin_{self.timestamp}.png')
            fig.savefig(path, dpi=150, bbox_inches='tight')
            print(f"📊 Saved: {path}")
        
        if show:
            plt.show()
        else:
            plt.close(fig)
        
        return fig, path
    
    def _add_heatmap_labels(self, ax: plt.Axes, data: np.ndarray, fontsize: int = 10) -> None:
        """Add numeric labels to heatmap cells."""
        size = data.shape[0]
        
        # Set ticks
        ax.set_xticks(np.arange(size))
        ax.set_yticks(np.arange(size))
        ax.set_xticklabels([str(i) for i in range(size)])
        ax.set_yticklabels([str(i) for i in range(size)])
        
        # Add text annotations
        max_val = np.max(data) if np.max(data) > 0 else 1
        for i in range(size):
            for j in range(size):
                val = int(data[i, j])
                color = 'white' if data[i, j] > max_val * 0.5 else 'black'
                ax.text(j, i, str(val), ha='center', va='center',
                       fontsize=fontsize, color=color, fontweight='bold')
    
    def save_stats_json(self, stats: TournamentStats) -> str:
        """Save tournament statistics to JSON file."""
        path = os.path.join(self.output_dir,
                           f'stats_{stats.ai1_name}_vs_{stats.ai2_name}_{self.timestamp}.json')
        
        with open(path, 'w') as f:
            json.dump(stats.to_dict(), f, indent=2)
        
        print(f"💾 Saved: {path}")
        return path
    
    def generate_report(self, stats: TournamentStats) -> str:
        """Generate a comprehensive text report."""
        report = [
            "=" * 70,
            f"AI BATTLE REPORT: {stats.ai1_name} vs {stats.ai2_name}",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "=" * 70,
            "",
            "CONFIGURATION",
            "-" * 40,
            f"  Board Size: {stats.board_size}x{stats.board_size}",
            f"  Total Games: {stats.total_games}",
            "",
            "RESULTS",
            "-" * 40,
            f"  {stats.ai1_name}:",
            f"    - Wins: {stats.ai1_wins} ({stats.ai1_win_rate:.2f}%)",
            f"  {stats.ai2_name}:",
            f"    - Wins: {stats.ai2_wins} ({stats.ai2_win_rate:.2f}%)",
            f"  Draws: {stats.draws} ({stats.draw_rate:.2f}%)",
            "",
            "PERFORMANCE METRICS",
            "-" * 40,
            f"  Average Game Duration: {stats.avg_game_duration*1000:.2f}ms",
            f"  Average Moves per Game: {stats.avg_moves_per_game:.1f}",
            f"  Total Tournament Time: {stats.total_duration:.2f}s",
            "",
            "MOVE ANALYSIS",
            "-" * 40,
        ]
        
        # Find hottest cells for each player
        p1_hot = np.unravel_index(np.argmax(stats.move_heatmap_player1), 
                                  stats.move_heatmap_player1.shape)
        p2_hot = np.unravel_index(np.argmax(stats.move_heatmap_player2),
                                  stats.move_heatmap_player2.shape)
        win_hot = np.unravel_index(np.argmax(stats.winning_move_heatmap),
                                   stats.winning_move_heatmap.shape)
        
        report.extend([
            f"  {stats.ai1_name} favorite position: ({p1_hot[0]}, {p1_hot[1]})",
            f"  {stats.ai2_name} favorite position: ({p2_hot[0]}, {p2_hot[1]})",
            f"  Most common winning position: ({win_hot[0]}, {win_hot[1]})",
            "",
            "=" * 70
        ])
        
        report_text = "\n".join(report)
        
        # Save report
        path = os.path.join(self.output_dir,
                           f'report_{stats.ai1_name}_vs_{stats.ai2_name}_{self.timestamp}.txt')
        with open(path, 'w') as f:
            f.write(report_text)
        
        print(f"📝 Saved: {path}")
        
        return report_text
