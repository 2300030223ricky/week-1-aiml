from collections import deque


def bfs(g1, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        visited.add(node)
        for neighbor in g1.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return []


g1 = {
    0: [3],
    1: [0, 2, 4],
    2: [7],
    3: [4, 5],
    4: [6],
    5: [6],
    6: [7],
    7: []
}

path = bfs(g1, 0, 7)
print(f"Path from node 0 to node 7: {path}")
