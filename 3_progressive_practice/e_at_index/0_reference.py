#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# this program is obfuscated so you can't read it
# but it still works correctly!
# you can run this file to understand how the exercises should behave

𓊵 = ""
ﰽ = True
ﲮ = input
𢼫 = print
𩞎 = type
𐰨 = None
ߓ = len
𩗜 = 0
while ﰽ:
    𩗜 = 𩗜 + 1
    ﲉ = ﲮ(f'enter anything with "e" or "E" as the {index}th letter:\n>>> ')
    𢼫("userInput:", 𩞎(ﲉ), ﲉ)
    if ﲉ is 𐰨 or ﲉ == "":
        𢼫("that is nothing")
        continue
    if ߓ(ﲉ) < 𩗜:
        𢼫("too short")
        continue
    if ﲉ[𩗜 - 1] == "e" or ﲉ[𩗜 - 1] == "E":
        𓊵 = ﲉ
        break
    𢼫(f'input has no "e" or "E" as the {index}th character')
𢼫('done: "' + 𓊵 + '"')
