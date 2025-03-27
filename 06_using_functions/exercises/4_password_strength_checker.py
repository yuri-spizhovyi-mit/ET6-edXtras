#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""

@author: Claude AI, Evan
"""

import re
import getpass

print("===== Password Strength Checker =====")
print("This program will help you evaluate and improve your password security.")

continue_checking = True
while continue_checking:
    print("\nEnter a password to check (input will be hidden):")
    password = getpass.getpass()

    if not password:
        print("Password cannot be empty. Please try again.")
        continue

    strength_score = 0
    feedback = []

    if len(password) < 8:
        feedback.append("- TOO SHORT: Password should be at least 8 characters")
    elif len(password) >= 12:
        strength_score += 2
        feedback.append("+ GOOD LENGTH: Password has 12+ characters")
    else:
        strength_score += 1
        feedback.append("~ FAIR LENGTH: Consider using 12+ characters")

    if re.search(r"[a-z]", password):
        strength_score += 1
        feedback.append("+ LOWERCASE: Contains lowercase letters")
    else:
        feedback.append("- MISSING LOWERCASE: Add lowercase letters")

    if re.search(r"[A-Z]", password):
        strength_score += 1
        feedback.append("+ UPPERCASE: Contains uppercase letters")
    else:
        feedback.append("- MISSING UPPERCASE: Add uppercase letters")

    if re.search(r"\d", password):
        strength_score += 1
        feedback.append("+ NUMBERS: Contains digits")
    else:
        feedback.append("- MISSING NUMBERS: Add numeric digits")

    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?]', password):
        strength_score += 1
        feedback.append("+ SPECIAL CHARS: Contains special characters")
    else:
        feedback.append("- MISSING SPECIAL CHARS: Add special characters")

    if re.search(r"(.)\1\1", password):
        feedback.append("- REPEATED CHARS: Contains 3+ repeated characters")

    common_patterns = [
        "123",
        "abc",
        "qwerty",
        "password",
        "admin",
        "welcome",
        "letmein",
        "monkey",
        "dragon",
    ]

    for pattern in common_patterns:
        if pattern.lower() in password.lower():
            strength_score -= 1
            feedback.append(f"- COMMON PATTERN: Contains '{pattern}'")
            break

    if strength_score <= 2:
        rating = "Weak"
        rating_color = "\033[91m"  # Red
    elif strength_score <= 4:
        rating = "Moderate"
        rating_color = "\033[93m"  # Yellow
    else:
        rating = "Strong"
        rating_color = "\033[92m"  # Green

    reset_color = "\033[0m"  # Reset color

    print("\n===== Password Analysis =====")
    print(f"Strength Rating: {rating_color}{rating}{reset_color} ({strength_score}/6)")
    print("\nFeedback:")
    for item in feedback:
        if item.startswith("+"):
            print(f"\033[92m{item}{reset_color}")  # Green
        elif item.startswith("-"):
            print(f"\033[91m{item}{reset_color}")  # Red
        else:
            print(f"\033[93m{item}{reset_color}")  # Yellow

    while True:
        choice = input("\nCheck another password? (y/n): ").lower()
        if choice in ["y", "yes"]:
            break
        elif choice in ["n", "no"]:
            continue_checking = False
            break
        else:
            print("Please enter 'y' or 'n'")

print("\nThank you for using the Password Strength Checker!")
