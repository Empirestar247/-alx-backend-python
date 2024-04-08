# 0x03. Unittests and Integration Tests

## Introduction
This repository contains solutions and tests for tasks related to unit testing and integration testing in Python. It covers fundamental concepts such as mocking, parameterization, fixtures, and more.

## Testing Concepts
- **Unit Testing**: Ensures that individual units or components of the code work correctly in isolation. Focuses on testing the logic within functions and methods, often using mocks for external dependencies [[1](https://github.com/sarven/unit-testing-tips/blob/main/README.md)].
  
- **Integration Testing**: Verifies that different parts of the system work together as expected. Tests interactions between components, including external dependencies like HTTP requests, file I/O, and database operations [[2](https://www.yeeply.com/en/blog/digitalisation/types-of-software-testing-unit-testing-vs-integration-testing-vs-end-to-end-testing-e2e/)].

## Key Features
- **Parameterization**: Tests are parameterized to cover various scenarios and inputs, enhancing test coverage [[3](https://github.com/andredesousa/javascript-unit-testing-best-practices/blob/main/README.md)].

- **Mocking**: Utilizes mocking techniques to isolate units for testing and avoid external dependencies [[4](https://stackoverflow.com/questions/47976784/how-would-you-unit-test-a-method-whose-only-purpose-to-make-a-database-call)].

- **Memoization**: Explores memoization techniques for efficient caching of function results [[5](https://en.wikipedia.org/wiki/Memoization)].

## Execution
To execute tests, run:
```
$ python -m unittest path/to/test_file.py
```

## Requirements
- Ubuntu 18.04 LTS with Python 3.7
- Code style adheres to PEP 8 guidelines
- All files must be executable and properly documented
- Functions, classes, and modules must be thoroughly annotated with type hints

## File Structure
- `utils.py`: Contains utility functions for testing.
- `client.py`: Implements client functionalities.
- `fixtures.py`: Provides fixtures for integration testing.

## Tasks
The repository addresses several tasks covering unit testing, integration testing, parameterization, mocking, and more.

## Learning Objectives
By completing this project, learners will gain a deep understanding of unit testing, integration testing, and common testing patterns.

For detailed task descriptions and solutions, refer to the respective files in the repository.

## Sources
1. [Testing Tips](https://github.com/sarven/unit-testing-tips/blob/main/README.md)
2. [Types of Software Testing](https://www.yeeply.com/en/blog/digitalisation/types-of-software-testing-unit-testing-vs-integration-testing-vs-end-to-end-testing-e2e/)
3. [Unit Testing a Method](https://stackoverflow.com/questions/47976784/how-would-you-unit-test-a-method-whose-only-purpose-to-make-a-database-call)
4. [Mocking an External Function](https://softwareengineering.stackexchange.com/questions/436744/is-it-ok-to-test-an-external-function)
5. [End-to-End Testing vs Integration Testing](https://katalon.com/resources-center/blog/end-to-end-testing-integration-testing)
