class: middle, center

<!-- this file is written for remark: https://github.com/gnab/remark/wiki -->

# Using Functions

<br />

<img alt="Emerging Talent Logo" src="../.assets/emerging_talent_logo.png" height="50%"  width="50%">

---

class: middle

## Agenda

- **Learning Objectives**

- Documentation, unit tests, use cases - _a refresher_

- "Function Signature" - _a vocabulary word_

- **1. Calling Functions**

- "Abstracting" - _a vocabulary word_

- **2. Writing Functions**

- "Refactoring" - _a vocabulary word_

- **3. Extracting Functions**

- "Pure Functions" - _a vocabulary word_

- **4. Extracting Pure Functions**

- **Q & A**

---

class: middle

## Learning Objectives

- Understand the relationship between:

  - **docstring** - _a precise, readable description_ of a function's behavior
  - **unit tests** - _automated verification_ of a function's behavior
  - **use cases** - _practical applications_ of a function's behavior

- Understand _documentation as a **contract**_ between developers

  - You will play both the _authoring_ and _consuming_ developer

- Understand how **abstraction** makes programs easier to build

  - _hiding_ strategy and implementation, so you can _focus_ on behavior

- Use _program goals_ as a guide for _function **extraction**_

---

class: middle

## Describing Function Behavior

1. **docstring** - _a precise, readable description_

   - Intended primarily for _humans_ to read
   - Focuses on the function **in isolation** from real world uses

2. **unit tests** - _automated verification_

   - Intended primarily for _computers_ to run
   - Verifies that the function works as expected **in isolation**

3. **use cases** - _practical applications_

   - Intended primarily for _humans_ to read
   - Demonstrates how and why to use a function **in context**

---

class: middle

## Function Behavior: _a docstring_

```py
"""Count the number of vowels in a string. Case insensitive.

Parameters:
    str - the input string to check

Returns -> int: number of vowels in the text

Raises:
    AssertionError: if the argument is not a string

>>> count_vowels("hello")
2
>>> count_vowels("APPLE")
2
>>> count_vowels("rtbf")
0
"""
```

---

class: middle

## Function Behavior: _unit tests_

```py
class TestCountVowels(unittest.TestCase):
    """Test the count_vowels function!"""

    def test_no_vowels(self):
        """It should return 0 for strings without vowels"""
        self.assertEqual(count_vowels("jklmn"), 0)

    def test_all_vowels(self):
        """It should count all vowels in a string"""
        self.assertEqual(count_vowels("aUiO"), 4)

    def test_mixed_case(self):
        """It should handle mixed case strings"""
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_not_string(self):
        """It should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            count_vowels(123)
```

---

class: middle

## Function Behavior: _a use case_

```py
if what_to_count == 'v':
    count = count_vowels(text)
    message = f"your text has {count} vowels."

elif what_to_count == 'c:
    count = count_consonants(text)
    message = f"your text has {count} consonants."

else:
    message = f"'{what_to_count}' is not a supported option."
```

---

class: middle

## Signature - _a vocabulary word_

A function's **signature** shows _how to call it_ in a program, it includes:

- The function's name

- The arguments' names

- The arguments' types & default values

- The function's return type

A function signature DOES NOT document the behavior, so name your functions carefully!

<br/>

> `function_name(arg_1: str='', arg_2: int=0, ...) -> str`

<br/>

---

class: middle

## 1. Calling Functions

Practice _calling_ a function in different programs:

- See how a single function's behavior can be **reused** in different programs

- See how documentation acts as a **contract** between developers

- See how _unit tests_ help developers collaborate with **confidence**

- Practice using functions as an **abstraction** for more readable code

---

class: middle, center

## 1. Calling Functions: _demo_

---

class: middle

## Abstracting - _a vocabulary word_

Hiding code's _strategy_ and _implementation_ so you can focus on it's _behavior_:

- Helps write programs that describe _what_ happens, not _how_ it happens (_declarative_)

- Requires less knowledge to work with the code (_documentation!_)

- Avoids writing the same code over and over again

- Allows you to develop and test code _in isolation_

For now, _abstracting_ means writing a chunk of code into a _function_.

---

class: middle

## 2. Writing Functions

Practice _implementing_ a function that is used in multiple programs:

- See how a single function can be **reused** in different contexts

- See how functions + _unit tests_ help develop code **in isolation** with **confidence**

- Understand the value of **abstracting** away tricky bits of logic in a program

---

class: middle, center

## 2. Writing Functions: _demo_

---

class: middle

## Refactoring - _a vocabulary word_

Changing code's _strategy_ and/or _implementation_ WITHOUT changing its _behavior_. Why?

- To make your code more readable

- To align with code conventions

- To practice new coding techniques

- To make your code more efficient

- Because you have a better understanding of the problem

---

class: middle

## 3. Extracting Functions

Practice _refactoring_ programs by _extracting_ isolated goals to a new function:

- Understand how program data _flows through_, and _is transformed by_, each goal

- Identify goals that can be _abstracted_ with a manageable _function signature_

- Write in a _declarative_ style that describes _what_ happens, now _how_ it happens

---

class: middle, center

## 3. Extracting Functions: _demo_

---

---

class: middle

## Pure Functions - _a vocabulary word_

_Pure functions_: don't modify arguments, always return, do not interact with the user.

- Easy to document

- Easy to unit test

- Easy to reason about in context

- Easy to reuse in different programs

---

class: middle

## 4. Extracting Pure Functions

Practice _identifying_ goals that can be refactored to _pure functions_.

- Identify goals that can be _abstracted_ with a manageable _function signature_

- Learn to separate _program logic_ from _user interactions_

- Create programs that are easier to _understand_, _develop_, and _maintain_

---

class: middle, center

## 4. Extracting Pure Functions: _demo_

---

class: middle, center

## Q & A

---

class: middle, center

# Thank You

<br />

<img alt="Emerging Talent Logo" src="../.assets/emerging_talent_logo.png" height="50%"  width="50%">

---
