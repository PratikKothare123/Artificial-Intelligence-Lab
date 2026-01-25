

📘 Theory – Magic Square (AI Lab)
🔹 Introduction

A Magic Square is a square matrix of size n × n in which the sum of numbers in each row, each column, and both main diagonals is the same. This common sum is called the Magic Constant.

Magic squares are commonly used in mathematics, artificial intelligence, and problem-solving techniques to understand logical placement and pattern generation.

🔹 Magic Constant Formula

For a magic square of order n, the magic constant is calculated as:

𝑀
=
𝑛
(
𝑛
2
+
1
)
2
M=
2
n(n
2
+1)
	​


Example:
For n = 3,

𝑀
=
3
(
9
+
1
)
2
=
15
M=
2
3(9+1)
	​

=15
🔹 Working Principle

The magic square is generated using the Siamese Method, which works only for odd numbers.

Steps:

Place number 1 in the middle of the top row.

Move up and right for the next number.

If the position goes out of the grid:

Wrap around to the opposite side.

If the cell is already filled:

Move down one step instead.

Repeat until all numbers are placed.

🔹 Algorithm Used

Create an empty 2D list of size n × n.

Initialize position at middle of first row.

Place numbers from 1 to n² using the Siamese method.

Apply boundary conditions.

Display the final magic square.

🔹 Applications

Used in artificial intelligence problem solving

Helps in understanding matrix manipulation

Used in puzzles and mathematical games

Useful for learning algorithm design

🔹 Conclusion

The Magic Square program demonstrates logical thinking and matrix manipulation in Python. It efficiently generates a square where the sum of rows, columns, and diagonals are equal, making it a useful example of algorithmic problem solving.
