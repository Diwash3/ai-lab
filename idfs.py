def IDDFS(graph, start, goal, depth=0):
    if start == goal:
        return [start]
    if depth == 0:
        return []
    if start in graph:
        for child in graph[start]:
            path = IDDFS(graph, child, goal, depth-1)
            if path:
                return [start] + path
    return []

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }
    start, goal = "A", "F"
    print("Graph:", graph)
    print("Start:", start)
    print("Goal:", goal)
    for depth in range(1, len(graph)+1):
        path = IDDFS(graph, start, goal, depth)
        if path:
            print("Goal found at depth", depth, ":", path)
            break
    else:
        print("Goal node not found")
