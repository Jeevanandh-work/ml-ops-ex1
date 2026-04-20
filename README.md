# Experiment No.1 - Crafting Effective Test Cases for Python Functions

## Objective
Develop and execute comprehensive test cases for Python functions to verify correctness, reliability, and edge-case behavior.

## Project Structure
- src/q1_factorial.py
- src/q2_palindrome.py
- src/q3_prime.py
- src/q4_sort.py
- src/q5_fibonacci.py
- tests/test_q1_factorial.py
- tests/test_q2_palindrome.py
- tests/test_q3_prime.py
- tests/test_q4_sort.py
- tests/test_q5_fibonacci.py

## Behavior Decisions Used
- Factorial: negative input raises ValueError.
- Palindrome: ignores case and non-alphanumeric characters.
- Prime: numbers <= 1 are non-prime.
- Sorting: returns a new ascending list.
- Fibonacci: returns values up to numeric limit n; negative raises ValueError.

## Run Steps
1. Install dependencies:
   pip install -r requirements.txt
2. Run tests:
   pytest -q
