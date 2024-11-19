from collections import deque
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()
    queue.append((0, 0)) 
    while queue:
        jug1, jug2 = queue.popleft()
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        print(f"Jug1: {jug1}L, Jug2: {jug2}L")
        if jug1 == target or jug2 == target:
            print("\nSolution found!")
            return True
        queue.append((jug1_capacity, jug2))
        queue.append((jug1, jug2_capacity))
        queue.append((0, jug2))
        queue.append((jug1, 0))
        pour = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - pour, jug2 + pour))
        pour = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + pour, jug2 - pour))
    print("\nNo solution exists.")
    return False
jug1_capacity = 4  
jug2_capacity = 3  
target = 2  
water_jug_bfs(jug1_capacity, jug2_capacity, target)
