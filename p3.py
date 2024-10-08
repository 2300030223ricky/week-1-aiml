from collections import deque


def bfs(g1, start, goal):
    queue = deque([(start, [start])])  # Initialize queue with start node and path
    visited = set()  # Set to keep track of visited nodes

    while queue:
        node, path = queue.popleft()  # Get the current node and path
        if node == goal:  # If current node is the goal, return the path
            return path
        visited.add(node)  # Mark the current node as visited
        for neighbor in g1.get(node, []):  # Iterate over neighbors
            if neighbor not in visited:  # If neighbor is not visited
                queue.append((neighbor, path + [neighbor]))  # Add neighbor to queue with updated path
                visited.add(neighbor)  # Mark neighbor as visited

    return []  # Return empty list if no path is found


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

# Find the path from node 0 to node 7
path = bfs(g1, 0, 7)
print(f"Path from node 0 to node 7: {path}")