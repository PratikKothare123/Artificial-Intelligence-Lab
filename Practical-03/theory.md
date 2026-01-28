# 🎮 Theory – Tic Tac Toe Game (Artificial Intelligence)

## Introduction
Tic Tac Toe is a simple two-player game commonly used to demonstrate **Artificial Intelligence concepts** such as decision making, rule-based systems, and game logic. In this practical, one player is a **human**, and the other is a **computer (AI)** that makes decisions based on predefined rules.

The game is played on a **3×3 grid**, where the goal is to place three identical symbols in a row, column, or diagonal.

---

## Objective
The objective of this practical is to:
- Implement a Tic Tac Toe game using Python  
- Apply **rule-based decision making**
- Understand game state evaluation  
- Simulate human vs computer interaction  

---

## Game Rules
1. The game is played on a 3×3 board.
2. Player uses symbol **X**.
3. Computer uses symbol **O**.
4. Players take turns placing their symbol.
5. A player wins if:
   - Three symbols match in a row, column, or diagonal.
6. If all cells are filled and no one wins, the game ends in a **draw**.

---

## State Representation
The board is represented using a 2D list:
```
-------------
| X | O | X |
-------------
| X | O | X |
-------------
|   | X | O |
-------------
```

Each cell represents the current state of the game.

---

## Production Rules Used
The AI follows these production rules:

1. If AI can win → make winning move  
2. If opponent can win → block opponent  
3. Else → make a random valid move  
4. If no empty cells → declare draw  

These rules help the AI make logical decisions during gameplay.

---

## Algorithm
1. Initialize empty 3×3 board.
2. Allow player to make the first move.
3. Check for winning condition after each move.
4. Computer applies rule-based logic to choose move.
5. Repeat until:
   - Player wins  
   - Computer wins  
   - Game is drawn  
6. Display final result.

---

## Advantages
- Simple and easy to understand  
- Demonstrates AI decision-making  
- Uses rule-based reasoning  
- Improves understanding of game logic  

---

## Applications
- Game development  
- Artificial Intelligence learning  
- Decision-making systems  
- Human-computer interaction  

---

## Conclusion
The Tic Tac Toe program successfully demonstrates the use of **production rules and artificial intelligence logic** to simulate a game environment. The AI is able to make decisions based on the game state and provides an effective example of rule-based problem solving.

