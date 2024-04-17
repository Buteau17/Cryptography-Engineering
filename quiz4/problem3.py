import random
import numpy as np
from itertools import permutations

def basic_shuffle(deck):
    # Shuffle a deck of cards using a simple method
    deck_length = len(deck)
    for idx in range(deck_length):
        random_index = random.randint(0, deck_length - 1)
        # Swap the current card with another randomly selected card
        deck[idx], deck[random_index] = deck[random_index], deck[idx]
    return deck

def efficient_shuffle(deck):
    # Implementing the Fisher-Yates shuffle for more uniform distribution
    for current_position in reversed(range(1, len(deck))):
        random_position = random.randint(0, current_position)
        # Swap the current card with a randomly chosen earlier card
        deck[current_position], deck[random_position] = deck[random_position], deck[current_position]
    return deck

def simulate_shuffling(method, trials=1000000):
    # Simulation to assess the distribution of shuffling methods
    initial_deck = [1, 2, 3, 4]
    possible_outcomes = list(permutations(initial_deck))
    outcome_frequency = {outcome: 0 for outcome in possible_outcomes}
    
    for _ in range(trials):
        shuffled_deck = method(initial_deck.copy())
        outcome_frequency[tuple(shuffled_deck)] += 1

    frequencies = list(outcome_frequency.values())
    mean_value = np.mean(frequencies)
    standard_dev = np.std(frequencies)

    return outcome_frequency, mean_value, standard_dev

basic_results, basic_mean, basic_sd = simulate_shuffling(basic_shuffle)
efficient_results, efficient_mean, efficient_sd = simulate_shuffling(efficient_shuffle)

# Displaying results in a more informative way
print("Basic Shuffle Method(Naive algorithm):")
for outcome in sorted(basic_results):
    print(f"{outcome}: {basic_results[outcome]}")
print(f"Mean: {basic_mean}, Standard Deviation: {basic_sd}")

print("\nEfficient Shuffle (Fisher-Yates):")
for outcome in sorted(efficient_results):
    print(f"{outcome}: {efficient_results[outcome]}")
print(f"Mean: {efficient_mean}, Standard Deviation: {efficient_sd}")
