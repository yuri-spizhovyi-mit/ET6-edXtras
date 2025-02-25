# Describing Programs

> "Code tells you how, comments tell you why."
>
> - [Jeff Atwood](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/)

This guide will help you learn how to do a close reading of Python programs. You'll practice writing detailed comments to describe what is happening and why.

- [Zooming Out](#1-zooming-out)
- [Zooming In](#2-zooming-in)
- [Connections](#3-connections)
- [Goals](#4-goals)
- [Commenting Best Practices](#commenting-best-practices)

## 0. Basic Example Structure

```python
"""
(describe what the program does from the user's perspective)

A user can...
- given...
- given...

Test cases:
- given...
  'input' -> 'output'
  'input' -> 'output'
- given...
  ...
"""

# -- goal (an important step in the program) --

# what code is written in this line of the program?
#  why is this line of code here?
#  what variables does it use?
#  how does it relate to other lines?
#  ... anything else you notice?
line = 'of code'

# -- goal (another important step) --

# what code is written in this line of the program?
#  why is this line of code here?
#  what variables does it use?
#  how does it relate to other lines?
#  ... anything else you notice?
print(line)
```

## 1. Zooming Out

Understanding what the entire program does just by running it, without looking at any single line of code.

- Can a user interact with the program?
  - When do they interact? (beginning, middle, end, ...)
  - How is the user's input processed?
  - Can the user's input influence the program's flow?
- What data exists at the beginning of the program?
- What data exists at the end of the program?
- What is the user's journey? How many different paths can it take?
- ... what else can you say about the program?

Here's an example of documenting program behavior with user stories and input/output examples:

```python
"""
A user can input anything, if the input is "yes" the program is excited
- given the user interrupts (Ctrl+C), the program is sad
- given the user inputs 'yes' (case insensitive) the program is excited
- given any other inputs, the program says it's "baaaaad"

Test cases:
- the user interrupts
  KeyboardInterrupt -> ':('
- any sort of 'yes'
  'yes' -> 'yes!'
  'Yes' -> 'Yes!'
  'yES' -> 'yES!'
- any other input
  'hello' -> 'baaaaad: hello'
  '' -> 'baaaaad: '
  'good bye' -> 'baaaaad: good bye'
"""

try:
    user_input = input('enter the word "yes", upper or lower case: ')
except KeyboardInterrupt:
    reaction = ':('
else:
    if user_input.lower() == 'yes':
        reaction = user_input + '!'
    else:
        reaction = 'baaaaad: ' + user_input

print(reaction)
```

## 2. Zooming In

Understanding what each line of code does and how it works, without taking a step back to understand the whole program.

- What Python features are used in each line?
- What data types and operators are in the program?
- What do the variable names tell you about the code?
- What control flow structures do you see?
- ... what else do you notice about each line?

> Use `!` to mark important lines
> Use `?` for unclear or complex lines
> Use `#` for lines to revisit later

Here's the same program with detailed line-by-line analysis:

```python
"""
A user can input anything, if the input is "yes" the program is excited
- given the user interrupts (Ctrl+C), the program is sad
- given the user inputs 'yes' (case insensitive) the program is excited
- given any other inputs, the program says it's "baaaaad"

Test cases:
- the user interrupts
  KeyboardInterrupt -> ':('
- any sort of 'yes'
  'yes' -> 'yes!'
  'Yes' -> 'Yes!'
  'yES' -> 'yES!'
- any other input
  'hello' -> 'baaaaad: hello'
  '' -> 'baaaaad: '
  'good bye' -> 'baaaaad: good bye'
"""

# try-except block: handle potential keyboard interrupt
# this replaces JS's null check since Python's input() doesn't return null
try:
    # call input(): get string from user
    # declare, init: store user's input as string
    user_input = input('enter the word "yes", upper or lower case: ')
except KeyboardInterrupt:
    # assign: sad face for interrupted input
    reaction = ':('
else:
    # check: convert input to lower case and compare to 'yes'
    if user_input.lower() == 'yes':
        # assign: the input concatenated with exclamation mark
        reaction = user_input + '!'
    else:
        # assign: baaaad concatenated with the input
        reaction = 'baaaaad: ' + user_input

# call print: show the final reaction
print(reaction)
```

## 3. Connections

Start finding connections between different lines of code across the program.

- Which lines of code are related?
- How is each variable used?
- ... what other connections do you notice between lines?

```python
"""
A user can input anything, if the input is "yes" the program is excited
- given the user interrupts (Ctrl+C), the program is sad
- given the user inputs 'yes' (case insensitive) the program is excited
- given any other inputs, the program says it's "baaaaad"

Test cases:
- the user interrupts
  KeyboardInterrupt -> ':('
- any sort of 'yes'
  'yes' -> 'yes!'
  'Yes' -> 'Yes!'
  'yES' -> 'yES!'
- any other input
  'hello' -> 'baaaaad: hello'
  '' -> 'baaaaad: '
  'good bye' -> 'baaaaad: good bye'
"""

# try-except block: handle potential keyboard interrupt
# this structure ensures we handle all possible ways the user might interact
try:
    # call input(): get string from user
    # declare, init: store user's input as string
    #   this line explains to the user what they need to input
    #   the user_input variable is used later to check if they entered valid input
    user_input = input('enter the word "yes", upper or lower case: ')
except KeyboardInterrupt:
    # assign: sad face for interrupted input
    #   this handles the case where the user doesn't want to provide input
    #   similar to handling null in the JS version
    reaction = ':('
else:
    # check: convert input to lower case and compare to 'yes'
    #   checking the user input to validate their response
    #   using .lower() makes the check case-insensitive
    if user_input.lower() == 'yes':
        # assign: the input concatenated with exclamation mark
        #   this is the success path for valid user inputs
        #   we keep their original casing in the response
        reaction = user_input + '!'
    else:
        # assign: baaaad concatenated with the input
        #   this is the path for invalid user inputs (anything but "yes")
        #   shows users what they typed wrong
        reaction = 'baaaaad: ' + user_input

# call print: show the final reaction
#  all logic is complete, just need to show the reaction to the user
print(reaction)
```

## 4. Goals

So you know what the program does, and how the lines of code work, it's time to
start zooming out again!

A "goal" an important step in the program, it can be a single line of code or
many lines of code. What's important is that a goal achieves one important step
along the way from the program's initial input to it's final output. One way to
decide which lines belong to the same goal is to look at your _connections_
comments. If you see a group of lines that seem to be closely connected, you may
be looking at a goal:

- How does each line of code contribute to the program's overall behavior?
- Which line(s) of code seem the most important?
- How does the program's data change from before to after a goal?

You can label goals with commented line dividers and a short title describe what
important step happens in those lines:


```python
"""
A user can input anything, if the input is "yes" the program is excited
- given the user interrupts (Ctrl+C), the program is sad
- given the user inputs 'yes' (case insensitive) the program is excited
- given any other inputs, the program says it's "baaaaad"

Test cases:
- the user interrupts
  KeyboardInterrupt -> ':('
- any sort of 'yes'
  'yes' -> 'yes!'
  'Yes' -> 'Yes!'
  'yES' -> 'yES!'
- any other input
  'hello' -> 'baaaaad: hello'
  '' -> 'baaaaad: '
  'good bye' -> 'baaaaad: good bye'
"""

# --- gather user input safely ---

try:
    # get user input while handling potential interruption
    user_input = input('enter the word "yes", upper or lower case: ')
except KeyboardInterrupt:
    reaction = ':('

# --- process input and create reaction ---

else:
    # determine appropriate reaction based on input
    if user_input.lower() == 'yes':
        reaction = user_input + '!'
    else:
        reaction = 'baaaaad: ' + user_input

# --- display result to user ---

# show final reaction
print(reaction)
```

## Commenting Best Practices

> You should never write so many comments in a program, this is just an exercise!

Good comments should:

1. Explain WHY, not just WHAT
2. Provide context for complex logic
3. Document assumptions and edge cases
4. Help others (and future you) understand the code's purpose

For additional reading on commenting best practices:

- [Python documentation on docstrings (PEP 257)](https://peps.python.org/pep-0257/)
- [Google Python Style Guide - Comments](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [better-programming](https://medium.com/better-programming/javascript-clean-code-comments-c926d5aae2cb)
- [elegantthemes](https://www.elegantthemes.com/blog/wordpress/how-to-comment-your-code-like-a-pro-best-practices-and-good-habits)
- [4 reasons to comment](https://blog.submain.com/4-reasons-need-code-comments/)
- [the pros and cons](https://www.techrepublic.com/article/the-pros-and-cons-but-mostly-pros-of-comments-in-code/)
- [comments in your code](https://medium.com/better-programming/comments-in-your-code-730cfd1dde02)
- [the good, the bad, the ugly](https://www.freecodecamp.org/news/code-comments-the-good-the-bad-and-the-ugly-be9cc65fbf83/)


---
---

> adapted from [Welcome to JS](https://github.com/DeNepo/welcome-to-js/tree/main/3-understanding-programs/4-describing-programs)