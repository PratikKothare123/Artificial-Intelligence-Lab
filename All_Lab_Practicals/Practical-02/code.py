from collections import deque
from math import gcd

def water_jug_problem(capacity1, capacity2, target):

    # If target is not achievable
    if target > max(capacity1, capacity2) or target % gcd(capacity1, capacity2) != 0:
        return None

    visited = set()
    queue = deque()
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        # Goal reached
        if jug1 == target or jug2 == target:
            return path

        states = []

        # Fill jugs
        states.append((capacity1, jug2))   # Fill jug1
        states.append((jug1, capacity2))   # Fill jug2

        # Empty jugs
        states.append((0, jug2))            # Empty jug1
        states.append((jug1, 0))            # Empty jug2

        # Pour jug1 → jug2
        pour = min(jug1, capacity2 - jug2)
        states.append((jug1 - pour, jug2 + pour))

        # Pour jug2 → jug1
        pour = min(jug2, capacity1 - jug1)
        states.append((jug1 + pour, jug2 - pour))

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None


capacity1 = int(input("Enter capacity of jug 1: "))
capacity2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

solution = water_jug_problem(capacity1, capacity2, target)

if solution:
    print("\nSolution Found:")
    for step in solution:
        print(step)
else:
    print("No solution exists")
