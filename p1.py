def a_star(graph, start, end, heuristic):
    heap = [(heuristic[start], start, [start])]
    visited = set()
    while heap:
        heap = sorted(heap, key=lambda x: x[0])
        (cost, current, path) = heap.pop(0)
        if current == end:
            return path, cost
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph[current]:
            total_cost = cost - heuristic[current] + graph[current][neighbor] + heuristic[neighbor]
            heap.append((total_cost, neighbor, path + [neighbor]))
    return 0


graph = {
    'A': {'B': 2, 'F': 3},
    'B': {'A': 2, 'C': 3, 'D': 2},
    'C': {'B': 3,'D': 1, 'E': 5},
    'D': {'B': 2,'C': 1, 'E': 8},
    'E': {'C': 5,'D': 8, 'I': 5, 'J': 5},
    'F': {'A': 3,'G': 1, 'H': 7},
    'G': {'F': 1,'I': 3},
    'H': {'F': 7,'I': 2},
    'I': {'E': 5,'G': 3, 'H': 2, 'J': 3},
}
heuristic = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    
}
result = a_star(graph, 'A', 'J', heuristic)
if result == 0:
    print("Path not found")
else:
    path, cost = result
    print(path)
    print(cost) 
