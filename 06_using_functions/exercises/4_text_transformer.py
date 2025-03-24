#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

@author: Claude AI, Evan
"""

import re


def main():
    print("===== Interactive Text Transformer =====")
    print("Transform your text with various operations")

    while True:
        print("\nEnter text to transform (or 'exit' to quit):")
        original_text = input("> ").strip()

        if original_text.lower() == "exit":
            print("Goodbye!")
            break

        if not original_text:
            print("Please enter some text to transform.")
            continue

        transformed_text = original_text

        transformation_history = [("Original", original_text)]

        while True:
            print("\nCurrent text:")
            print(f'"{transformed_text}"')

            print("\nChoose a transformation:")
            print("1. Change case (upper/lower/title/sentence)")
            print("2. Replace characters")
            print("3. Remove patterns (regex)")
            print("4. Add prefix/suffix")
            print("5. Reverse (all/words/sentences)")
            print("6. View transformation history")
            print("7. Undo last transformation")
            print("8. Start over with new text")
            print("9. Exit program")

            choice = input("Enter choice (1-9): ").strip()

            if choice == "1":
                print("\nSelect case transformation:")
                print("a. UPPERCASE")
                print("b. lowercase")
                print("c. Title Case")
                print("d. Sentence case")

                case_choice = input("Enter choice (a-d): ").lower()

                old_text = transformed_text
                if case_choice == "a":
                    transformed_text = transformed_text.upper()
                    operation = "UPPERCASE"
                elif case_choice == "b":
                    transformed_text = transformed_text.lower()
                    operation = "lowercase"
                elif case_choice == "c":
                    transformed_text = transformed_text.title()
                    operation = "Title Case"
                elif case_choice == "d":
                    sentences = re.split(r"(?<=[.!?])\s+", transformed_text)
                    capitalized_sentences = []
                    for sentence in sentences:
                        if sentence:
                            capitalized_sentences.append(
                                sentence[0].upper() + sentence[1:]
                            )
                    transformed_text = " ".join(capitalized_sentences)
                    operation = "Sentence case"
                else:
                    print("Invalid choice. No change applied.")
                    continue

                if old_text != transformed_text:
                    transformation_history.append((operation, transformed_text))

            elif choice == "2":
                old_text = transformed_text
                find_text = input("Enter characters to replace: ")
                if not find_text:
                    print("Nothing to replace. Operation cancelled.")
                    continue

                replace_text = input("Enter replacement text: ")
                transformed_text = transformed_text.replace(find_text, replace_text)
                operation = f"Replace '{find_text}' with '{replace_text}'"

                if old_text != transformed_text:
                    transformation_history.append((operation, transformed_text))

            elif choice == "3":
                old_text = transformed_text
                try:
                    pattern = input("Enter regex pattern to remove: ")
                    if not pattern:
                        print("No pattern entered. Operation cancelled.")
                        continue

                    transformed_text = re.sub(pattern, "", transformed_text)
                    operation = f"Remove pattern '{pattern}'"

                    if old_text != transformed_text:
                        transformation_history.append((operation, transformed_text))
                except re.error:
                    print("Invalid regex pattern. Please try again.")

            elif choice == "4":
                old_text = transformed_text
                prefix = input("Enter prefix (leave empty for none): ")
                suffix = input("Enter suffix (leave empty for none): ")

                transformed_text = prefix + transformed_text + suffix
                operation = f"Add prefix/suffix"

                if old_text != transformed_text:
                    transformation_history.append((operation, transformed_text))

            elif choice == "5":
                print("\nSelect reversal type:")
                print("a. Reverse entire text")
                print("b. Reverse each word")
                print("c. Reverse each sentence")

                reverse_choice = input("Enter choice (a-c): ").lower()
                old_text = transformed_text

                if reverse_choice == "a":
                    transformed_text = transformed_text[::-1]
                    operation = "Reverse entire text"
                elif reverse_choice == "b":
                    words = transformed_text.split()
                    reversed_words = [word[::-1] for word in words]
                    transformed_text = " ".join(reversed_words)
                    operation = "Reverse each word"
                elif reverse_choice == "c":
                    sentences = re.split(r"(?<=[.!?])\s+", transformed_text)
                    reversed_sentences = [sentence[::-1] for sentence in sentences]
                    transformed_text = " ".join(reversed_sentences)
                    operation = "Reverse each sentence"
                else:
                    print("Invalid choice. No change applied.")
                    continue

                if old_text != transformed_text:
                    transformation_history.append((operation, transformed_text))

            elif choice == "6":
                print("\n===== Transformation History =====")
                for i, (operation, text) in enumerate(transformation_history):
                    print(f"{i}. {operation}:")
                    print(f'   "{text}"')
                input("\nPress Enter to continue...")

            elif choice == "7":
                if len(transformation_history) > 1:
                    transformation_history.pop()
                    operation, transformed_text = transformation_history[-1]
                    print(f"Undid last transformation. Reverted to: {operation}")
                else:
                    print("Nothing to undo.")

            elif choice == "8":
                print("Starting over with new text.")
                break

            elif choice == "9":
                print("Goodbye!")
                return

            else:
                print("Invalid choice. Please enter a number from 1-9.")


if __name__ == "__main__":
    main()
