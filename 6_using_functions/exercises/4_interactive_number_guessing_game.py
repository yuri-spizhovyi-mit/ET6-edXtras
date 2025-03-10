#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for an interactive number guessing game.

This program implements a number guessing game with difficulty levels,
hints, scoring system, and game statistics tracking.
Written in fully imperative style for refactoring exercises.

@author: Claude AI
"""

import random
import time
import os


def main():
    """Run the main program loop."""
    print("===== Number Guessing Game =====")
    print("Try to guess the secret number!")
    
    games_played = 0
    games_won = 0
    best_score = 0
    fastest_time = float('inf')
    
    play_game = True
    while play_game:
        print("\n=== New Game ===")
        print("Select difficulty level:")
        print("1. Easy (1-50, unlimited guesses)")
        print("2. Medium (1-100, 10 guesses)")
        print("3. Hard (1-200, 7 guesses)")
        print("4. Custom")
        
        difficulty = 0
        while difficulty not in [1, 2, 3, 4]:
            try:
                difficulty = int(input("Enter choice (1-4): "))
                if difficulty not in [1, 2, 3, 4]:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        if difficulty == 1:  
            max_number = 50
            max_guesses = float('inf')
            difficulty_multiplier = 1
        elif difficulty == 2:
            max_number = 100
            max_guesses = 10
            difficulty_multiplier = 2
        elif difficulty == 3:
            max_number = 200
            max_guesses = 7
            difficulty_multiplier = 3
        else:  
            while True:
                try:
                    min_number = int(input("Enter minimum number: "))
                    max_number = int(input("Enter maximum number: "))
                    if min_number >= max_number:
                        print("Maximum must be greater than minimum.")
                        continue
                    break
                except ValueError:
                    print("Please enter valid numbers.")
            
            while True:
                try:
                    max_guesses_input = input("Enter maximum guesses (leave blank for unlimited): ")
                    if not max_guesses_input:
                        max_guesses = float('inf')
                    else:
                        max_guesses = int(max_guesses_input)
                        if max_guesses <= 0:
                            print("Must allow at least 1 guess.")
                            continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    
            range_size = max_number - min_number + 1
            if max_guesses == float('inf'):
                difficulty_multiplier = range_size / 50  
            else:
                difficulty_multiplier = (range_size / 50) * (10 / max_guesses)
            
            if 'min_number' not in locals():
                min_number = 1
        
        if 'min_number' not in locals():
            min_number = 1
            
        secret_number = random.randint(min_number, max_number)
        
        guesses_taken = 0
        has_won = False
        start_time = time.time()
        hints_used = 0
        
        print(f"\nI'm thinking of a number between {min_number} and {max_number}.")
        if max_guesses == float('inf'):
            print("You have unlimited guesses.")
        else:
            print(f"You have {max_guesses} guesses.")
        
        while guesses_taken < max_guesses:
            guess = 0
            while True:
                try:
                    guess_input = input("\nEnter your guess (or 'h' for a hint): ")
                    
                    if guess_input.lower() == 'h':
                        hints_used += 1
                        hint_type = random.randint(1, 4)
                        
                        if hint_type == 1:
                            if secret_number % 2 == 0:
                                print("HINT: The number is even.")
                            else:
                                print("HINT: The number is odd.")
                        elif hint_type == 2:
                            range_size = max_number - min_number
                            if range_size > 20:
                                if secret_number <= (max_number + min_number) // 2:
                                    max_number = (max_number + min_number) // 2
                                    print(f"HINT: The number is between {min_number} and {max_number}.")
                                else:
                                    min_number = (max_number + min_number) // 2
                                    print(f"HINT: The number is between {min_number} and {max_number}.")
                            else:
                                is_prime = True
                                if secret_number <= 1:
                                    is_prime = False
                                elif secret_number <= 3:
                                    is_prime = True
                                elif secret_number % 2 == 0 or secret_number % 3 == 0:
                                    is_prime = False
                                else:
                                    i = 5
                                    while i * i <= secret_number:
                                        if secret_number % i == 0 or secret_number % (i + 2) == 0:
                                            is_prime = False
                                            break
                                        i += 6
                                
                                print(f"HINT: The number is {'prime' if is_prime else 'not prime'}.")
                        elif hint_type == 3:
                            digit_sum = sum(int(digit) for digit in str(secret_number))
                            print(f"HINT: The sum of the digits is {digit_sum}.")
                        else:
                            factors = []
                            for i in range(2, 11):
                                if secret_number % i == 0:
                                    factors.append(i)
                            
                            if factors:
                                print(f"HINT: The number is divisible by {random.choice(factors)}.")
                            else:
                                print(f"HINT: The number is not divisible by any number between 2 and 10.")
                        
                        continue  
                        
                    guess = int(guess_input)
                    if guess < min_number or guess > max_number:
                        print(f"Please enter a number between {min_number} and {max_number}.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            
            guesses_taken += 1
            
            if guess == secret_number:
                end_time = time.time()
                time_taken = end_time - start_time
                has_won = True
                print(f"\nCongratulations! You guessed the number in {guesses_taken} {'guess' if guesses_taken == 1 else 'guesses'}!")
                print(f"Time taken: {time_taken:.2f} seconds")
                
                if max_guesses == float('inf'):
                    max_score_factor = 1000  
                else:
                    max_score_factor = 1000 * (max_guesses / 10)  
                    
                guess_factor = max_score_factor / guesses_taken
                hint_penalty = 0.8 ** hints_used  
                time_factor = 0.9 ** (time_taken / 10) 
                final_score = int(guess_factor * difficulty_multiplier * hint_penalty * time_factor)
                
                print(f"Your score: {final_score}")
                print(f"Hints used: {hints_used}")
                
                games_played += 1
                games_won += 1
                if final_score > best_score:
                    best_score = final_score
                    print("New high score!")
                if time_taken < fastest_time:
                    fastest_time = time_taken
                    print("New fastest time!")
                    
                break
                
            feedback = "Too high!" if guess > secret_number else "Too low!"
            
            distance = abs(guess - secret_number)
            percentage = distance / max_number * 100
            
            if percentage < 5:
                temperature = "Very hot!"
            elif percentage < 10:
                temperature = "Hot"
            elif percentage < 20:
                temperature = "Warm"
            elif percentage < 30:
                temperature = "Cool"
            else:
                temperature = "Cold"
                
            guesses_left = "unlimited" if max_guesses == float('inf') else str(max_guesses - guesses_taken)
            print(f"{feedback} {temperature} (Guesses left: {guesses_left})")
            
        if not has_won:
            print(f"\nGame over! You've used all {max_guesses} guesses.")
            print(f"The secret number was {secret_number}.")
            games_played += 1
            
        play_again = input("\nPlay again? (y/n): ").lower().startswith('y')
        
        if not play_again or random.random() < 0.3:  
            win_percentage = (games_won / games_played * 100) if games_played > 0 else 0
            
            print("\n===== Game Statistics =====")
            print(f"Games played: {games_played}")
            print(f"Games won: {games_won}")
            print(f"Win percentage: {win_percentage:.1f}%")
            if best_score > 0:
                print(f"Best score: {best_score}")
            if fastest_time < float('inf'):
                print(f"Fastest win: {fastest_time:.2f} seconds")
                
            if not play_again:
                play_game = False
                print("Thanks for playing!")
            else:
                input("Press Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
