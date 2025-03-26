#!/usr/bin/env python3

def gather_scores(prompt: str = 'Enter a score') -> list[float]:
    scores = []
    while True:
        user_input = input(prompt)
        
        if user_input.lower() == 'done':
            break
        
        try:
            score = float(user_input)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Score must be between 0 and 100")
        except ValueError:
            print(f"'{user_input}' is not a valid score")
    
    return scores

def calculate_grade_distribution(scores: list[float]) -> dict:
    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    
    for score in scores:
        if score >= 90:
            grade_counts['A'] += 1
        elif score >= 80:
            grade_counts['B'] += 1
        elif score >= 70:
            grade_counts['C'] += 1
        elif score >= 60:
            grade_counts['D'] += 1
        else:
            grade_counts['F'] += 1
    
    return grade_counts

def calculate_average(scores: list[float]) -> float:
    return sum(scores) / len(scores) if scores else 0

def main():
    print("\nQuiz Score Tracker\n")

    scores = gather_scores("Enter a quiz score (0-100) or 'done' to finish:\n>>> ")
    grade_counts = calculate_grade_distribution(scores)
    total_average = calculate_average(scores)

    print("\nScores:", scores)
    print("Average Score:", total_average)
    print("Grade Distribution:", grade_counts)

main()
main()
