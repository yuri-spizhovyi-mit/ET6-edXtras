# Using Functions

Practice writing I/O programs that use utility functions to _abstract_ core logic. The exercises come in four levels:

1. Call an existing function to complete a program.
2. Write the function used by an existing program.
3. _Extract_ a function from an existing program with labeled goals.
4. _Identify_ program goals that can be extracted to _pure functions_.
   - there may be more than one per program
   - you may need to _refactor_ some goals before you can extract them as pure functions (eg. move `print` or `input` calls outside of the goal you are refactoring)
   - level 4 programs _may_ have some bugs ;)
   - _see [Behavior, Strategy, Implementation](../2_behavior_strategy_implementation/) to review program goals_
