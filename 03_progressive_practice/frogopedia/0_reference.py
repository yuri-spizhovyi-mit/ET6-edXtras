#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# this program is obfuscated so you can't read it
# but it still works correctly!
# you can run this file to understand how the exercises should behave

𞡠 = ""
𬚵 = False
𫨻 = input
褾 = print
𐰝 = type
ﮓ = None
ﵘ = True
𣔩 = 𬚵
while not 𣔩:
    𞡠 = 𫨻("tell me something about frogs:\n>>> ")
    褾("userInput:", 𐰝(𞡠), 𞡠)
    if 𞡠 == "" or 𞡠 is ﮓ:
        褾("that is not something")
        continue
    if "frog" in 𞡠.lower():
        𣔩 = ﵘ
        continue
    褾("nope, not about frogs.  try again.")
𐢜 = 'i just learned something cool about frogs!\n\n- "' + 𞡠 + '"'
褾(𐢜)
