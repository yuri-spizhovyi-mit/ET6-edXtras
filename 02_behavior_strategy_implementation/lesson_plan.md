class: middle, center

<!-- this file is written for remark: https://github.com/gnab/remark/wiki -->

# Behavior, Strategy, Implementation

<br />

<img alt="Emerging Talent Logo" src="../.assets/emerging_talent_logo.png" height="50%"  width="50%">

---

class: middle

## Agenda

- **Learning Objectives**

- **Behavior, Strategy, Implementation**

- **Understanding Simple Functions**

- **Understanding Interactive Programs**

- **Understanding Complex Functions**

- **Q & A**

---

class: middle

## Learning Objectives

- Understand the difference between code's _behavior_, _strategy_ and _implementation_

- Describe a **simple function** step-by-step:

  - _behavior_ -> _implementation_ -> _strategy_

- Describe an **interactive program** step-by-step:

  - _zoom out_ -> _zoom in_ -> _connections_ -> _goals_

- Describe a **complex function** step-by-step:
  - _document & test_ -> _predictive stepping_ -> _purpose_ -> _connections_ -> _goals_

---

class: middle

## [Behavior, Strategy, Implementation](./behavior_strategy_implementation.md?study)

---

class: middle

## Understanding Simple Functions

1. **Describing Behavior**:

   - assertion testing
   - documenting
   - naming the function
   - writing type hints

2. **Describing Implementation**:

   - predictive stepping
   - line-by-line comments

3. **Describing Strategy**:

   - comment the _purpose_ of each line
   - comment _connections_ between lines of code
   - summarize the strategy's _goals_ with comments
   - rename parameters & variables

---

class: middle, center

**Understanding Simple Functions: 0**

_A Mysterious Function_

```py
def a(b, c):
    assert isinstance(b, float|int)
    assert isinstance(c, float|int)
    return b + c
```

---

class: middle, center

**Understanding Simple Functions: 1**

_Behavior_

```py
def sum_two(b: int|float = 0, c: int|float = 0) -> int|float:
    """ Adds two integers or floats.

    Args: ...
    Returns: ...
    Raises: ...
    """
    assert isinstance(b, float|int)
    assert isinstance(c, float|int)
    return b + c

assert sum_two(1.0, 1) == 2.0, 'test 1'
assert sum_two(1, -3) == -2, 'test 2'
assert sum_two(12, 1.2) == 13.2, 'test 3'
```

---

class: middle, center

**Understanding Simple Functions: 2**

_Implementation_

```py
def sum_two(b: int|float = 0, c: int|float = 0) -> int|float:
    """ Adds two integers or floats.

    Args: ...
    Returns: ...
    Raises: ...
    """
    # - assert that the arguments are either floats or ints
    assert isinstance(b, float|int)
    assert isinstance(c, float|int)

    # - return the sum of the values stored in b and c
    return b + c

assert sum_two(1.0, 1) == 2.0, 'test 1'
assert sum_two(1, -3) == -2, 'test 2'
assert sum_two(12, 1.2) == 13.2, 'test 3'
```

---

class: middle, center

**Understanding Simple Functions: 3**

_Strategy_

```py
def sum_two(left_num: int|float = 0, right_num: int|float = 0) -> int|float:
    """ Sum two integers or floats.

    Args: ...
    Returns: ...
    Raises: ...
    """
    # validate the arguments' types
    # - assert that the arguments are either floats or ints
    assert isinstance(left_num, float|int), 'First argument must be an int or float.'
    assert isinstance(right_num, float|int), 'Second argument must be an int or float.'

    # sum the validated arguments
    # - return the sum of the values stored in b and c
    return left_num + right_num

assert sum_two(1.0, 1) == 2.0, 'test 1'
assert sum_two(1, -3) == -2, 'test 2'
assert sum_two(12, 1.2) == 13.2, 'test 3'
```

---

class: middle

## [Understanding Interactive Programs](./describing_programs.md?study)

---

class: middle

## Understanding Complex Functions

Describe a complex function step-by-step:

1. **Behavior**: unit tests, documentation, function name, type hints
2. **Implementation**: comment _what_ each line of code does
3. **Strategy** pt. 1 - **_purpose_**: comment _why_ each line of code exists
4. **Strategy** pt. 2 - **_connections_**: describe how different lines interact
5. **strategy** pt. 3 - **_goals_**: summarize the strategy using sub-goals

---

class: middle, center

## Understanding Complex Functions

### `code-along!`

---

class: middle, center

## Q & A

---

class: middle, center

# Thank You

<br />

<img alt="Emerging Talent Logo" src="../.assets/emerging_talent_logo.png" height="50%"  width="50%">

---
