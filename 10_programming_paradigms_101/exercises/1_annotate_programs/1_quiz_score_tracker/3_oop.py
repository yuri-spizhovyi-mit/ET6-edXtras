#!/usr/bin/env python3


class QuizScoreTracker:
    def __init__(self):
        self.scores = []
        self.grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        self.total_average = 0

    def gather_scores(self, prompt: str = "Enter a score"):
        while True:
            user_input = input(prompt)

            if user_input.lower() == "done":
                break

            try:
                score = float(user_input)
                if 0 <= score <= 100:
                    self.scores.append(score)
                else:
                    print("Score must be between 0 and 100")
            except ValueError:
                print(f"'{user_input}' is not a valid score")

    def calculate_grade_distribution(self):
        for score in self.scores:
            if score >= 90:
                self.grade_counts["A"] += 1
            elif score >= 80:
                self.grade_counts["B"] += 1
            elif score >= 70:
                self.grade_counts["C"] += 1
            elif score >= 60:
                self.grade_counts["D"] += 1
            else:
                self.grade_counts["F"] += 1

    def calculate_average(self):
        self.total_average = sum(self.scores) / len(self.scores) if self.scores else 0

    def main(self):
        print("\nQuiz Score Tracker\n")

        self.gather_scores("Enter a quiz score (0-100) or 'done' to finish:\n>>> ")
        self.calculate_grade_distribution()
        self.calculate_average()

        print("\nScores:", self.scores)
        print("Average Score:", self.total_average)
        print("Grade Distribution:", self.grade_counts)


tracker_1 = QuizScoreTracker()
tracker_1.main()

tracker_2 = QuizScoreTracker()
tracker_2.main()
