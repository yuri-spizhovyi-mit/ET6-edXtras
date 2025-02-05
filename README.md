# ET6: edXtras

This repository contains examples and exercises to complement 6.00.1x and 6.00.2x.

## Running Scripts in this Repository

- **Running a plain Python script**:
  - _Simply run the script_: `$ python path/to/file.py`
  - _Print the program's trace to the console_:
    `$ python -m trace -t path/to/file.py`
  - _Count how many times each line is executed_:
    `$ python -m trace -c path/to/file.py`
- **Run a file with Unit Tests**:
  - _as a script_:`$ python -m unittest path/to/tests/test_file.py`
  - _as a module_:`$ python -m unittest path.to.tests.test_file`
