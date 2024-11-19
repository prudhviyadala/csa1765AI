
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
def dfs_recursive(graph, start, visited=None):
 
    if visited is None:
        visited = set()  # Initialize visited nodes

    # Mark the current node as visited
    visited.add(start)
    print(start, end=" ")

    # Visit all the neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# DFS using an explicit stack
def dfs_stack(graph, start):
 
    visited = set()  # Set to track visited nodes
    stack = [start]  # Stack for DFS

    while stack:
        node = stack.pop()  # Pop a node from the stack
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add all unvisited neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Example Usage
print("DFS (Recursive):")
dfs_recursive(graph, 'A')  # Start DFS from node 'A'

print("\nDFS (Using Stack):")
dfs_stack(graph, 'A')  # Start DFS from node 'A'
