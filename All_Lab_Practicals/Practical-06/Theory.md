# Practical 06 – Alpha Beta Pruning

## Aim
To implement the concept of Alpha Beta Pruning for optimization in game development.

---

## Introduction
Alpha-Beta Pruning is an optimization technique used in the **Minimax algorithm** 
to reduce the number of nodes evaluated in the game tree. It helps improve the 
performance of decision-making algorithms used in Artificial Intelligence.

It eliminates branches in the search tree that do not affect the final decision.

---

## Minimax Concept
Minimax is used in two-player games where:

- **MAX player** tries to maximize the score
- **MIN player** tries to minimize the score

The algorithm explores all possible moves and chooses the best move.

---

## Alpha Beta Pruning
Alpha-Beta Pruning improves Minimax by removing unnecessary branches.

Two values are used:

Alpha (α)
- Best value that MAX can guarantee so far.

Beta (β)
- Best value that MIN can guarantee so far.

If at any point:

α ≥ β

the remaining branches are **pruned (ignored)**.

---

## Advantages
- Reduces computation time
- Improves efficiency of Minimax
- Allows deeper game tree search
- Widely used in game AI

---

## Applications
- Chess AI
- Tic Tac Toe AI
- Checkers
- Game decision systems

---

## Conclusion
Alpha-Beta Pruning optimizes the Minimax algorithm by reducing the number of 
nodes evaluated in the search tree. This makes AI decision-making faster and 
more efficient in game development.