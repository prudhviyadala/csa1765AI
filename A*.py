import heapq

class Node:
    def __init__(self, name, g, h, parent=None):
        self.name = name  # Node name
        self.g = g  # Actual cost from start to this node
        self.h = h  # Heuristic cost to goal
        self.f = g + h  # f = g + h
        self.parent = parent  # Parent node in the path
    
    def __lt__(self, other):
        return self.f < other.f

def a_star(start, goal, graph, heuristic):
    open_list = []  # Min-heap priority queue
    closed_list = set()  # Set of explored nodes
    
    # Create start node and add it to open list
    start_node = Node(start, 0, heuristic[start])
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)  # Node with the lowest f value
        
        # If we reached the goal, reconstruct the path
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path
        
        closed_list.add(current_node.name)
        
        # Expand neighbors
        for neighbor, cost in graph[current_node.name]:
            if neighbor in closed_list:
                continue  # Skip already explored nodes
            
            g = current_node.g + cost  # Calculate g value for the neighbor
            h = heuristic.get(neighbor, 0)  # Get heuristic value for the neighbor
            
            # Check if the neighbor is already in the open list
            neighbor_node = Node(neighbor, g, h, current_node)
            if not any(neighbor_node.name == node.name and neighbor_node.f >= node.f for node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Example Usage
if __name__ == "__main__":
    # Define the graph as an adjacency list (neighbor, cost)
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    
    # Define the heuristic (straight-line distance to the goal 'D')
    heuristic = {
        'A': 7,  # Heuristic values for each node
        'B': 6,
        'C': 2,
        'D': 0  # Goal node heuristic is 0
    }
    
    # Run A* from 'A' to 'D'
    start = 'A'
    goal = 'D'
    path = a_star(start, goal, graph, heuristic)
    
    if path:
        print(f"Shortest path from {start} to {goal}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}")
