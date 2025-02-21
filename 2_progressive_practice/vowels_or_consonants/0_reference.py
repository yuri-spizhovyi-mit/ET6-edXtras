#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# this program is obfuscated so you can't read it
# but it still works correctly!
# you can run this file to understand how the exercises should behave

𩘟 = False
ﰭ = input
𮘁 = None
𣤣 = print
𞤝 = ""
ڂ = 𩘟
while not ڂ:
    𞤝 = ﰭ("enter a word to filter:\n>>> ")
    if 𞤝 == "" or 𞤝 is 𮘁:
        𣤣("nope, enter something:\n>>> ")
        continue
    ﯾ = re.compile(r"\s")
    if ﯾ.search(𞤝):
        𣤣("words can't have white space")
        continue
    𘌷 = "do you want to filter this word?\n\n" + '- "' + 𞤝 + '"'
    ڂ = ﰭ(𘌷).lower() in ["y", "yes", "true"]
𤢋 = ﰭ(
    f'what would you like to remove from "{userInput}"?\n- yes: vowels\n- no: consonants\n'
).lower() in ["y", "yes", "true"]
𥗕 = "aeiou" if 𤢋 else "bcdfghjklmnpqrstvwxyz"
𤵚 = ""
for 𐫋 in 𞤝:
    𐽅 = 𐫋.lower()
    if not 𥗕.__contains__(𐽅):
        𤵚 += 𐫋
ې = f'"{userInput}" -> "{filteredInput}"'
𣤣(ې)
