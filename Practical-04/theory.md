# Theory – A* Search Algorithm

## Introduction
A* (A-star) is a popular and efficient path-finding algorithm used in Artificial Intelligence.
It finds the shortest path from a start node to a goal node using both:
- Actual cost from start (g)
- Heuristic estimated cost to goal (h)

The total cost is calculated as:
f(n) = g(n) + h(n)

## Objective
To implement the A* search algorithm to find the shortest path between two nodes in a graph.

## Working Principle
The A* algorithm works using:
- Open List: nodes to be explored
- Closed List: nodes already visited
- Heuristic function: estimates distance to goal

At every step, the node with the lowest f(n) value is selected.

## Algorithm Steps
1. Initialize open list with the start node.
2. Set g(start) = 0 and calculate f(start).
3. Select node with lowest f value.
4. If node is goal, stop and return path.
5. Otherwise, explore neighbors.
6. Update cost and parent if better path is found.
7. Repeat until goal is reached.

## Advantages
- Finds optimal solution
- Efficient and complete
- Widely used in AI and games

## Applications
- Path finding
- Robotics navigation
- Game AI
- Route optimization

## Conclusion
The A* algorithm efficiently finds the shortest path using heuristic-based search. It combines the advantages of greedy search and uniform cost search, making it one of the most widely used AI algorithms.
