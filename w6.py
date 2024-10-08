from collections import deque


def min_steps_to_destination(grid, k):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    m, n = len(grid), len(grid[0])
    queue = deque([(0, 0, 0, 0)])
    visited = set()
    visited.add((0, 0, 0))

    while queue:
        x, y, steps, obstacles_removed = queue.popleft()
        if x == m - 1 and y == n - 1:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_obstacles_removed = obstacles_removed + grid[nx][ny]
                if new_obstacles_removed <= k and (nx, ny, new_obstacles_removed) not in visited:
                    visited.add((nx, ny, new_obstacles_removed))
                    print(dx, dy)
                    queue.append((nx, ny, steps + 1, new_obstacles_removed))
    return -1


grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
k = 1
print(f"The min. no. of steps to walk from the upper left corner to the lower right corner is = ",
      min_steps_to_destination(grid, k))
