import itertools

def calculate_distance(path, dist_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += dist_matrix[path[i]][path[i + 1]]
    total_distance += dist_matrix[path[-1]][path[0]]  # Returning to the start city
    return total_distance

def traveling_salesman_bruteforce(dist_matrix):
    num_cities = len(dist_matrix)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_path = None
    for perm in itertools.permutations(cities):
        current_distance = calculate_distance(perm, dist_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = perm

    return best_path, min_distance
dist_matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 5],
    [20, 25, 30, 0, 15],
    [25, 30, 5, 15, 0]
]
best_path, min_distance = traveling_salesman_bruteforce(dist_matrix)
print(f"Best path: {best_path}")
print(f"Minimum distance: {min_distance}")
