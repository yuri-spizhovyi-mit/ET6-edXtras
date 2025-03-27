#!/usr/bin/env python3

import csv
import math


class DataPreprocessor:
    def __init__(self, filename):
        self.filename = filename
        self.headers = []
        self.raw_data = []
        self.feature_stats = {}
        self.normalized_data = []

    def load_data(self):
        with open(self.filename, "r") as file:
            csv_reader = csv.reader(file)
            self.headers = next(csv_reader)

            for row in csv_reader:
                # Convert to numeric, handle non-numeric
                numeric_row = []
                for value in row:
                    try:
                        numeric_row.append(float(value))
                    except ValueError:
                        numeric_row.append(0)  # Default replacement

                self.raw_data.append(numeric_row)

    def calculate_feature_stats(self):
        for col_index in range(len(self.headers)):
            column = [row[col_index] for row in self.raw_data]

            mean = sum(column) / len(column)
            variance = sum((x - mean) ** 2 for x in column) / len(column)
            std_dev = math.sqrt(variance)

            self.feature_stats[self.headers[col_index]] = {
                "mean": mean,
                "std_dev": std_dev,
            }

    def normalize_data(self):
        for row in self.raw_data:
            normalized_row = []
            for col_index, value in enumerate(row):
                feature = self.headers[col_index]
                normalized_value = (
                    value - self.feature_stats[feature]["mean"]
                ) / self.feature_stats[feature]["std_dev"]
                normalized_row.append(normalized_value)

            self.normalized_data.append(normalized_row)

    def print_results(self):
        print("Feature Statistics:")
        for feature, stats in self.feature_stats.items():
            print(
                f"{feature}: Mean = {stats['mean']:.2f}, Std Dev = {stats['std_dev']:.2f}"
            )

        print("\nFirst 5 Normalized Data Points:")
        for row in self.normalized_data[:5]:
            print(row)

    def preprocess(self):
        print("\nMachine Learning Data Preprocessor\n")

        self.load_data()
        self.calculate_feature_stats()
        self.normalize_data()
        self.print_results()


# Usage
preprocessor = DataPreprocessor("dataset.csv")
preprocessor.preprocess()
