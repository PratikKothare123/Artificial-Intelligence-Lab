# Practical 5 – Cryptarithmetic Puzzle Solver

## Aim
Analyze a suitable technique to implement a Cryptarithmetic Puzzle and implement the same using Python.

---

## Introduction
Cryptarithmetic puzzles are mathematical puzzles where letters represent digits. 
Each letter corresponds to a unique digit from 0–9, and the goal is to find the 
correct digit substitution so that the arithmetic equation becomes valid.

Example:

  SEND
+ MORE
------
 MONEY

Each letter represents a unique digit. The program must determine which digits
correspond to each letter so that the equation holds true.

---

## Technique Used
The Cryptarithmetic puzzle is solved using the **Backtracking algorithm**.

Backtracking is a problem-solving technique that tries all possible combinations 
and eliminates those that do not satisfy the constraints.

---

## Working Principle
1. Identify all unique characters in the puzzle.
2. Assign digits (0–9) to characters.
3. Ensure no two characters have the same digit.
4. Convert the characters into numbers.
5. Check whether the arithmetic equation is satisfied.
6. If the equation is correct, the solution is found.

---

## Example Puzzle

SEND + MORE = MONEY


Possible Solution:


SEND = 9567
MORE = 1085
MONEY = 10652


---

## Algorithm
1. Read the words involved in the puzzle.
2. Identify unique characters.
3. Assign digits using backtracking.
4. Convert characters to numbers.
5. Verify the arithmetic equation.
6. Print the solution if valid.

---

## Applications
- Artificial Intelligence problem solving
- Constraint satisfaction problems
- Logical reasoning systems
- Puzzle solving algorithms

---

## Conclusion
The Cryptarithmetic puzzle demonstrates how Artificial Intelligence techniques 
like **backtracking and constraint satisfaction** can be used to solve logical 
problems efficiently.
