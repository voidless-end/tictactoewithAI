#!/usr/bin/env python3
# File: run_ai_battle.py
# Main entry point for AI vs AI battles with statistics and visualizations

"""
🤖 AI Battle Arena - Tic-Tac-Toe
================================

Pit different AI strategies against each other and analyze their performance
with heat maps and comprehensive statistics.

Available AI Types:
  - random: Picks random empty cells
  - minimax: Optimal play using minimax with alpha-beta pruning
  - montecarlo: Monte Carlo Tree Search simulations
  - strategic: Rule-based (win/block/center/corners)
  - aggressive: Focuses on building threats

Usage Examples:
  python run_ai_battle.py                          # Interactive mode
  python run_ai_battle.py minimax random -n 100   # Quick battle
  python run_ai_battle.py --round-robin -n 50     # Full tournament
"""

import argparse
import sys
from typing import List, Optional

from ai_strategies import AI_TYPES, create_ai
from ai_battle_arena import AIBattleArena, quick_battle
from ai_statistics import BattleStatistics


def print_banner():
    """Print the welcome banner."""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🤖 AI BATTLE ARENA - TIC-TAC-TOE 🎮                      ║
║                                                              ║
║     Watch AI strategies compete against each other!          ║
║     Analyze with heat maps and statistics.                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)


def print_ai_descriptions():
    """Print descriptions of available AI types."""
    descriptions = {
        'random': '🎲 Picks random empty cells - baseline strategy',
        'minimax': '🧠 Optimal minimax with alpha-beta - unbeatable on 3x3',
        'montecarlo': '🎯 Monte Carlo simulations - good for larger boards',
        'strategic': '📋 Rule-based: win/block/center/corners',
        'aggressive': '⚔️  Builds threats aggressively, less defensive'
    }
    
    print("\n📋 Available AI Types:")
    print("-" * 50)
    for ai_type in AI_TYPES:
        print(f"  {ai_type:12} - {descriptions.get(ai_type, '')}")
    print()


def interactive_mode():
    """Run in interactive mode with user prompts."""
    print_banner()
    print_ai_descriptions()
    
    while True:
        print("\n🎮 MENU:")
        print("  1. Quick Battle (AI vs AI)")
        print("  2. Round Robin Tournament")
        print("  3. Watch a Single Game (verbose)")
        print("  4. Exit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            run_quick_battle_interactive()
        elif choice == '2':
            run_round_robin_interactive()
        elif choice == '3':
            run_single_game_interactive()
        elif choice == '4':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")


def run_quick_battle_interactive():
    """Interactive quick battle setup."""
    print("\n" + "=" * 50)
    print("⚔️  QUICK BATTLE SETUP")
    print("=" * 50)
    
    print(f"\nAvailable AIs: {', '.join(AI_TYPES)}")
    
    ai1 = input("Enter AI 1 type: ").strip().lower()
    if ai1 not in AI_TYPES:
        print(f"❌ Unknown AI: {ai1}. Using 'random'")
        ai1 = 'random'
    
    ai2 = input("Enter AI 2 type: ").strip().lower()
    if ai2 not in AI_TYPES:
        print(f"❌ Unknown AI: {ai2}. Using 'random'")
        ai2 = 'random'
    
    try:
        board_size = int(input("Board size (3-10, default=3): ").strip() or "3")
        board_size = max(3, min(10, board_size))
    except ValueError:
        board_size = 3
    
    try:
        num_games = int(input("Number of games (default=100): ").strip() or "100")
        num_games = max(1, min(10000, num_games))
    except ValueError:
        num_games = 100
    
    # Run battle
    arena = AIBattleArena(board_size=board_size, verbose=False)
    stats = arena.run_tournament(ai1, ai2, num_games)
    
    # Generate visualizations
    visualize = input("\nGenerate visualizations? (y/n, default=y): ").strip().lower()
    if visualize != 'n':
        analyzer = BattleStatistics()
        analyzer.generate_all_visualizations(stats, save=True, show=True)
        analyzer.save_stats_json(stats)
        analyzer.generate_report(stats)


def run_round_robin_interactive():
    """Interactive round robin setup."""
    print("\n" + "=" * 50)
    print("🏆 ROUND ROBIN TOURNAMENT")
    print("=" * 50)
    
    print(f"\nAvailable AIs: {', '.join(AI_TYPES)}")
    print("Press Enter to use all, or enter comma-separated list:")
    
    ai_input = input("AIs to include: ").strip()
    if ai_input:
        ai_types = [a.strip().lower() for a in ai_input.split(',')]
        ai_types = [a for a in ai_types if a in AI_TYPES]
        if len(ai_types) < 2:
            print("❌ Need at least 2 valid AIs. Using all.")
            ai_types = AI_TYPES
    else:
        ai_types = AI_TYPES
    
    try:
        board_size = int(input("Board size (3-10, default=3): ").strip() or "3")
        board_size = max(3, min(10, board_size))
    except ValueError:
        board_size = 3
    
    try:
        num_games = int(input("Games per matchup (default=50): ").strip() or "50")
        num_games = max(1, min(1000, num_games))
    except ValueError:
        num_games = 50
    
    # Run tournament
    arena = AIBattleArena(board_size=board_size, verbose=False)
    results = arena.run_round_robin(ai_types, num_games)
    
    # Generate visualizations
    visualize = input("\nGenerate visualizations? (y/n, default=y): ").strip().lower()
    if visualize != 'n':
        analyzer = BattleStatistics()
        analyzer.plot_round_robin_results(results, save=True, show=True)
        
        # Generate individual dashboards for each matchup
        for matchup, stats in results.items():
            analyzer.plot_summary_dashboard(stats, save=True, show=False)
            analyzer.save_stats_json(stats)


def run_single_game_interactive():
    """Watch a single game with verbose output."""
    print("\n" + "=" * 50)
    print("🎬 WATCH A SINGLE GAME")
    print("=" * 50)
    
    print(f"\nAvailable AIs: {', '.join(AI_TYPES)}")
    
    ai1 = input("Enter AI 1 type: ").strip().lower()
    if ai1 not in AI_TYPES:
        ai1 = 'random'
    
    ai2 = input("Enter AI 2 type: ").strip().lower()
    if ai2 not in AI_TYPES:
        ai2 = 'random'
    
    try:
        board_size = int(input("Board size (3-10, default=3): ").strip() or "3")
        board_size = max(3, min(10, board_size))
    except ValueError:
        board_size = 3
    
    # Run single game with verbose output
    arena = AIBattleArena(board_size=board_size, verbose=True)
    ai1_obj = create_ai(ai1, 1)
    ai2_obj = create_ai(ai2, 2)
    
    result = arena.play_single_game(ai1_obj, ai2_obj)
    
    print(f"\n📊 Game Summary:")
    print(f"   Winner: {result.winner if result.winner != 0 else 'Draw'}")
    print(f"   Total Moves: {result.total_moves}")
    print(f"   Duration: {result.game_duration*1000:.2f}ms")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='🤖 AI Battle Arena - Tic-Tac-Toe AI vs AI with statistics',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              # Interactive mode
  %(prog)s minimax random               # Minimax vs Random, 100 games
  %(prog)s minimax strategic -n 200     # 200 games
  %(prog)s --round-robin -n 50          # All AIs tournament
  %(prog)s minimax random -s 4          # On 4x4 board
  %(prog)s minimax random -v            # Verbose (show each game)
        """
    )
    
    parser.add_argument('ai1', nargs='?', help=f'First AI type: {", ".join(AI_TYPES)}')
    parser.add_argument('ai2', nargs='?', help=f'Second AI type: {", ".join(AI_TYPES)}')
    parser.add_argument('-n', '--num-games', type=int, default=100,
                        help='Number of games to play (default: 100)')
    parser.add_argument('-s', '--board-size', type=int, default=3,
                        help='Board size (default: 3)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Show each game as it plays')
    parser.add_argument('--round-robin', action='store_true',
                        help='Run round robin tournament with all AIs')
    parser.add_argument('--no-viz', action='store_true',
                        help='Skip visualization generation')
    parser.add_argument('--output-dir', type=str, default='ai_battle_results',
                        help='Output directory for results')
    parser.add_argument('--list-ais', action='store_true',
                        help='List available AI types and exit')
    
    args = parser.parse_args()
    
    # List AIs and exit
    if args.list_ais:
        print_ai_descriptions()
        return
    
    # Interactive mode if no AI specified
    if args.ai1 is None and not args.round_robin:
        interactive_mode()
        return
    
    # Validate AIs
    if args.ai1 and args.ai1.lower() not in AI_TYPES:
        print(f"❌ Unknown AI: {args.ai1}")
        print(f"Available: {', '.join(AI_TYPES)}")
        sys.exit(1)
    
    if args.ai2 and args.ai2.lower() not in AI_TYPES:
        print(f"❌ Unknown AI: {args.ai2}")
        print(f"Available: {', '.join(AI_TYPES)}")
        sys.exit(1)
    
    # Clamp board size
    board_size = max(3, min(10, args.board_size))
    
    print_banner()
    
    # Create analyzer
    analyzer = BattleStatistics(output_dir=args.output_dir)
    
    if args.round_robin:
        # Round robin tournament
        arena = AIBattleArena(board_size=board_size, verbose=args.verbose)
        results = arena.run_round_robin(AI_TYPES, args.num_games)
        
        if not args.no_viz:
            analyzer.plot_round_robin_results(results, save=True, show=True)
            for matchup, stats in results.items():
                analyzer.plot_summary_dashboard(stats, save=True, show=False)
                analyzer.save_stats_json(stats)
    else:
        # Single matchup
        if not args.ai2:
            print("❌ Please specify two AIs for battle")
            print("Usage: python run_ai_battle.py AI1 AI2")
            sys.exit(1)
        
        arena = AIBattleArena(board_size=board_size, verbose=args.verbose)
        stats = arena.run_tournament(args.ai1.lower(), args.ai2.lower(), args.num_games)
        
        if not args.no_viz:
            analyzer.generate_all_visualizations(stats, save=True, show=True)
            analyzer.save_stats_json(stats)
            analyzer.generate_report(stats)
    
    print("\n✅ Battle complete! Check the output directory for results.")


if __name__ == "__main__":
    main()
