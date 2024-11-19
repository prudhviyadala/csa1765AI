from collections import deque

def bfs(graph, start):
 
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Queue for BFS
    result = []  # To store the order of visited nodes

    while queue:
        node = queue.popleft()  # Dequeue a node from the front of the queue

        if node not in visited:
            visited.add(node)  # Mark the node as visited
            result.append(node)  # Add the node to the result
            # Enqueue all unvisited neighbors
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
bfs_result = bfs(graph, start_node)

print("BFS Traversal Order:", bfs_result)
