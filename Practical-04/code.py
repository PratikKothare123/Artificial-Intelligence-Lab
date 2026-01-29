import heapq

def a_star_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]

        for neighbor, cost in graph[current].items():
            temp_g = g_score[current] + cost

            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None


# Graph representation
graph = {
    'S': {'A': 1, 'G': 10},
    'A': {'B': 2, 'C': 1},
    'B': {'D': 5},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 2},
    'G': {}
}

# Heuristic values
heuristic = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0
}

start = 'S'
goal = 'G'

result = a_star_search(graph, start, goal, heuristic)

if result:
    print("Shortest Path:", result)
    cost = 0
    for i in range(len(result)-1):
        cost += graph[result[i]][result[i+1]]
    print("Total Cost:", cost)
else:
    print("No path found")
