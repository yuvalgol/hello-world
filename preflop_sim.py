import sys
import random
from treys import Deck, Evaluator, Card


def parse_hand(hand_str):
    parts = hand_str.split()
    if len(parts) != 2:
        raise ValueError("Hand must contain two cards like 'As Ks'")
    return [Card.new(parts[0]), Card.new(parts[1])]


def simulate(hand_str, num_opponents=1, iterations=10000):
    hero_cards = parse_hand(hand_str)
    evaluator = Evaluator()
    wins = 0
    ties = 0

    for _ in range(iterations):
        deck = Deck()
        for c in hero_cards:
            deck.cards.remove(c)
        opponents = [deck.draw(2) for _ in range(num_opponents)]
        community = deck.draw(5)

        hero_score = evaluator.evaluate(hero_cards, community)
        opp_scores = [evaluator.evaluate(o, community) for o in opponents]
        best_score = min([hero_score] + opp_scores)
        num_best = ([hero_score] + opp_scores).count(best_score)

        if hero_score == best_score and num_best == 1:
            wins += 1
        elif hero_score == best_score:
            ties += 1

    win_pct = wins / iterations * 100
    tie_pct = ties / iterations * 100
    equity = win_pct + tie_pct / num_opponents
    return win_pct, tie_pct, equity


def main():
    if len(sys.argv) < 2:
        print("Usage: python preflop_sim.py 'As Ks' [num_opponents] [iterations]")
        return
    hand = sys.argv[1]
    num_opponents = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    iterations = int(sys.argv[3]) if len(sys.argv) > 3 else 10000
    win, tie, equity = simulate(hand, num_opponents, iterations)
    print(f"Hand: {hand}")
    print(f"Opponents: {num_opponents}")
    print(f"Iterations: {iterations}")
    print("--------------------------")
    print(f"Win %: {win:.2f}")
    print(f"Tie %: {tie:.2f}")
    print(f"Equity: {equity:.2f}")


if __name__ == "__main__":
    main()
