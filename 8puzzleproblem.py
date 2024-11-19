import heapq
def manhattan_distance(state, goal):
    distance = 0
    goal_flat = [item for row in goal for item in row]  # Flatten the goal state
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Ignore the blank tile
                x, y = divmod(goal_flat.index(state[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

# Convert 2D board to a tuple
def board_to_tuple(board):
    return tuple(item for row in board for item in row)

# Convert tuple back to 2D board
def tuple_to_board(t):
    return [list(t[i:i+3]) for i in range(0, len(t), 3)]

# Find the position of the blank (0) tile
def find_blank(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return i, j

# Generate the valid neighbors for a board state
def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* Algorithm
def a_star(start, goal):
    goal_tuple = board_to_tuple(goal)
    start_tuple = board_to_tuple(start)
    
    # Priority queue for A*
    pq = []
    heapq.heappush(pq, (0, start_tuple, 0, None))  # (f, current_state, g, parent)
    
    visited = set()
    came_from = {}
    
    while pq:
        _, current, g, parent = heapq.heappop(pq)
        
        if current in visited:
            continue
        visited.add(current)
        came_from[current] = parent
        
        # Check if goal state is reached
        if current == goal_tuple:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Reverse the path to get the correct order
        
        # Generate neighbors and calculate f = g + h
        current_board = tuple_to_board(current)
        for neighbor in generate_neighbors(current_board):
            neighbor_tuple = board_to_tuple(neighbor)
            if neighbor_tuple not in visited:
                h = manhattan_distance(neighbor, goal)
                heapq.heappush(pq, (g + 1 + h, neighbor_tuple, g + 1, current))
    
    return None  # Return None if no solution is found

# Print the solution path
def print_solution(path):
    for step, state in enumerate(path):
        print(f"Step {step}:")
        board = tuple_to_board(state)
        for row in board:
            print(row)
        print()

# Example usage
start_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = a_star(start_state, goal_state)

if solution:
    print("Solution found!")
    print_solution(solution)
else:
    print("No solution exists.")
