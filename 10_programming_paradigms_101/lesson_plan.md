class: middle, center

<!-- this file is written for remark: https://github.com/gnab/remark/wiki -->

# Encapsulation

_This workshops builds on [Using Functions](../06_using_functions/)_

<br />
<br />

<img alt="Emerging Talent Logo" src="../.assets/emerging_talent_logo.png" height="50%"  width="50%">

---

class: middle

## Agenda

- **Learning Objectives**

- **Programming Paradigms**

- **Understand Programming Paradigms via Data Flow**

- **Code-Along!**

---

class: middle

## Learning Objectives

- **Program State** - _Core_ data vs. other data.

- **Programming Paradigms** - _How data and instructions unite._

- **Encapsulation** - _Bundling data with instructions._

- **Annotating & Tracing Data Flows** - _data from -> data use -> data to_

- ~~**_Refactoring_ Scripts to Functions**~~ (_see [Using Functions](../06_using_functions/)_)

- ~~**_Refactoring_ Functions to Classes**~~ (_self-study with the exercises_)

---

class: middle

# Programming Paradigms

- **Imperative Programming**:

  - Step-by-step _instructions_ acting on shared program _state_
  - Imperative programs are usually _scripts_ that run top-to-bottom

- **Procedural Programming**:

  - Instructions are _abstracted_ behind reusable functions (_procedures_)
  - Procedures can receive arguments, manage local variables
  - Procedures can or access global variables, but it's best if they don't
  - Core program state is often managed in a `main` function

- **Object Oriented Programming**:

  - Instructions are _abstracted_ behind in reusable classes methods.
  - A class _instance_ encapsulates\* and manages it's own _state_
  - Methods receive args, use local variables, _and_ access _instance state_
  - Methods can access global variables, but it's best if they don't
  - When a full program is modeled with a class, it often has a `main` method

\*_Encapsulation -> bundling data with instruction that act on it._

---

class: middle

## Annotating Data Flow

- **Annotating Variable Use** - Stepping through can be helpful.

  1. _Where does the data come from?_
  2. _How Is the data used or transformed?_
  3. _Where is the data stored?_

- **Annotating Instruction Sets** - Black Boxes with multiple entrances & exits.

  1. _Where do the instruction sets get it's data?_
  2. _What does the instruction set do with the data?_
  3. _Where does the instruction set send it's data?_

- **Tracing Data Flow** - How is _state_ managed in the program?

  1. _What is the program's **entry point**?_
  2. _What "path" does each piece of data follow? (back-tracing!)_
  3. _Which data is "core" to the program, and which is not?_

---

class: middle, center

## Code-Along!

---

class: middle, center

# Thank You

<br />

<img alt="Emerging Talent Logo" src="../.assets/emerging_talent_logo.png" height="50%"  width="50%">

---
