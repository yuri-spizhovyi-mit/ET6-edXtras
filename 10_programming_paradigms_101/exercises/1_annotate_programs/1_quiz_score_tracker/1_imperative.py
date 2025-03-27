#!/usr/bin/env python3

print("\nQuiz Score Tracker\n")

scores = []
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

while True:
    user_input = input("Enter a quiz score (0-100) or 'done' to finish:\n>>> ")

    if user_input.lower() == "done":
        break

    try:
        score = float(user_input)
        if 0 <= score <= 100:
            scores.append(score)

            if score >= 90:
                grade_counts["A"] += 1
            elif score >= 80:
                grade_counts["B"] += 1
            elif score >= 70:
                grade_counts["C"] += 1
            elif score >= 60:
                grade_counts["D"] += 1
            else:
                grade_counts["F"] += 1
        else:
            print("Score must be between 0 and 100")
    except ValueError:
        print(f"'{user_input}' is not a valid score")

total_average = sum(scores) / len(scores) if scores else 0

print("\nScores:", scores)
print("Average Score:", total_average)
print("Grade Distribution:", grade_counts)
