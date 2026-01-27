# Theory – Water Jug Problem

## Introduction
The Water Jug Problem is a classic problem in Artificial Intelligence used to demonstrate
problem-solving using **production rules** and **state space search**.  
It involves two jugs of different capacities and the goal is to measure an exact amount of water
using a set of valid operations.

## Problem Description
We are given:
- A 4-gallon jug
- A 3-gallon jug
- Unlimited water supply
- No measuring scale on the jugs

The objective is to obtain **exactly 2 gallons of water** in the 4-gallon jug.

## State Representation
Each state is represented as:
(x, y)

Where:
- x → amount of water in 4-gallon jug
- y → amount of water in 3-gallon jug

Initial State:
(0, 0)

Goal State:
(2, 0)

## Production Rules
The following production rules are used:

1. Fill Jug 1 completely  
2. Fill Jug 2 completely  
3. Empty Jug 1  
4. Empty Jug 2  
5. Pour water from Jug 1 to Jug 2  
6. Pour water from Jug 2 to Jug 1  

These rules generate new states until the goal state is reached.

## Algorithm Used
The problem is solved using **Breadth First Search (BFS)**:
1. Start from the initial state.
2. Apply all possible production rules.
3. Avoid repeated states using a visited set.
4. Continue until the goal state is reached.
5. Display the sequence of steps.

## Conclusion
The Water Jug Problem demonstrates how production rules and state space search can be used to solve logical problems in Artificial Intelligence. The problem was successfully solved using BFS by systematically exploring all possible valid states.
