from collections import deque
def is_valid_state(state):
    m_left, c_left, m_right, c_right = state
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    return True
def generate_successors(state, boat_side):
    m_left, c_left, m_right, c_right = state
    successors = []
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  
    for m, c in moves:
        if boat_side == "left":
            new_state = (m_left - m, c_left - c, m_right + m, c_right + c)
            if is_valid_state(new_state):
                successors.append((new_state, "right"))
        else:
            new_state = (m_left + m, c_left + c, m_right - m, c_right - c)
            if is_valid_state(new_state):
                successors.append((new_state, "left"))
    return successors
def bfs(initial_state, goal_state):
    queue = deque([(initial_state, "left", [])])  
    visited = set()
    while queue:
        current_state, boat_side, path = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]
        if (current_state, boat_side) in visited:
            continue
        visited.add((current_state, boat_side))
        for successor, new_boat_side in generate_successors(current_state, boat_side):
            queue.append((successor, new_boat_side, path + [current_state]))
    return None
initial_state = (3, 3, 0, 0) 
goal_state = (0, 0, 3, 3)  
solution = bfs(initial_state, goal_state)
if solution:
    print("Solution found!")
    for step, state in enumerate(solution):
        print(f"Step {step}: {state}")
else:
    print("No solution exists.")
