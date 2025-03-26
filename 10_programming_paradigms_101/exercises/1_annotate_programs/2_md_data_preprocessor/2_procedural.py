#!/usr/bin/env python3

import csv
import math

def load_data(filename):
    raw_data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        
        for row in csv_reader:
            # Convert to numeric, handle non-numeric
            numeric_row = []
            for value in row:
                try:
                    numeric_row.append(float(value))
                except ValueError:
                    numeric_row.append(0)  # Default replacement
            
            raw_data.append(numeric_row)
    
    return headers, raw_data

def calculate_feature_stats(headers, raw_data):
    feature_stats = {}
    for col_index in range(len(headers)):
        column = [row[col_index] for row in raw_data]
        
        mean = sum(column) / len(column)
        variance = sum((x - mean) ** 2 for x in column) / len(column)
        std_dev = math.sqrt(variance)
        
        feature_stats[headers[col_index]] = {
            'mean': mean,
            'std_dev': std_dev
        }
    
    return feature_stats

def normalize_data(headers, raw_data, feature_stats):
    normalized_data = []
    for row in raw_data:
        normalized_row = []
        for col_index, value in enumerate(row):
            feature = headers[col_index]
            normalized_value = (value - feature_stats[feature]['mean']) / feature_stats[feature]['std_dev']
            normalized_row.append(normalized_value)
        
        normalized_data.append(normalized_row)
    
    return normalized_data

def print_results(feature_stats, normalized_data):
    print("Feature Statistics:")
    for feature, stats in feature_stats.items():
        print(f"{feature}: Mean = {stats['mean']:.2f}, Std Dev = {stats['std_dev']:.2f}")

    print("\nFirst 5 Normalized Data Points:")
    for row in normalized_data[:5]:
        print(row)

def main():
    print("\nMachine Learning Data Preprocessor\n")
    
    headers, raw_data = load_data('dataset.csv')
    feature_stats = calculate_feature_stats(headers, raw_data)
    normalized_data = normalize_data(headers, raw_data, feature_stats)
    
    print_results(feature_stats, normalized_data)

main()
