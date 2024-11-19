def is_safe(node, color, graph, colors):

    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def map_coloring_util(graph, color_options, colors, node):
    if node == len(graph):
        return True
    for color in color_options:
        if is_safe(node, color, graph, colors):
            colors[node] = color
            if map_coloring_util(graph, color_options, colors, node + 1):
                return True
            colors[node] = None

    return False
def map_coloring(graph, color_options):
    colors = [None] * len(graph)

    if map_coloring_util(graph, color_options, colors, 0):
        return colors
    else:
        return None

# Example Usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    # Example graph: A map with 4 regions (nodes 0, 1, 2, 3)
    graph = {
        0: [1, 2],    # Region 0 is adjacent to regions 1 and 2
        1: [0, 2, 3], # Region 1 is adjacent to regions 0, 2, and 3
        2: [0, 1, 3], # Region 2 is adjacent to regions 0, 1, and 3
        3: [1, 2]     # Region 3 is adjacent to regions 1 and 2
    }

    # Color options as R, G, B
    color_options = ["R", "G", "B"]

    # Solve the problem
    result = map_coloring(graph, color_options)
    if result:
        print("Solution found:")
        for region, color in enumerate(result):
            print(f"Region {region}: {color}")
    else:
        print("No solution exists!")
