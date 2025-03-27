#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" """

while True:
    phrase = input("Enter a phrase to search: ")
    if phrase:
        confirm = input(f"Is this correct? '{phrase}' (yes/no): ").strip().lower()
        if confirm == "yes":
            break

case_sensitive = (
    input("Do you want a case-sensitive search? (yes/no): ").strip().lower() == "yes"
)

while True:
    query = input("Enter a search query: ")
    if query:
        confirm = input(f"Is this correct? '{query}' (yes/no): ").strip().lower()
        if confirm == "yes":
            break

if case_sensitive:
    phrase_includes_query = query in phrase
else:
    phrase_includes_query = query.lower() in phrase.lower()

does_or_not = "does" if phrase_includes_query else "does not"

print(f'"{phrase}" {does_or_not} include "{query}"\nCase sensitive: {case_sensitive}')
