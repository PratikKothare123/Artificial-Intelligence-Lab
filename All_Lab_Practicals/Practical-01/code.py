# Function to generate Magic Square
def generateSquare(n):
    # Create empty matrix
    magicSquare = [[0 for _ in range(n)] for _ in range(n)]

    # Starting position
    i = n // 2
    j = n - 1

    num = 1
    while num <= n * n:
        # Condition 1
        if i == -1 and j == n:
            i = 0
            j = n - 2

        # Condition 2
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        # Condition 3
        if magicSquare[i][j] != 0:
            j -= 2
            i += 1
            continue
        else:
            magicSquare[i][j] = num
            num += 1

        j += 1
        i -= 1

    # Print Magic Square
    print("\nMagic Square for n =", n)
    print("Sum of each row/column =", n * (n * n + 1) // 2, "\n")

    for row in magicSquare:
        for num in row:
            print(f"{num:2}", end=" ")
        print()


# Driver Code
n = int(input("Enter an odd number: "))
generateSquare(n)
