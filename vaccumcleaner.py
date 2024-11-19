def vacuum_cleaner(grid, start):
    rows, cols = len(grid), len(grid[0])
    x, y = start
    actions = []
    cleaned = 0
    def print_grid():
        for row in grid:
            print(" ".join(str(cell) for cell in row))
        print()
    print("Initial Grid:")
    print_grid()
    while True:
        if grid[x][y] == 1:
            grid[x][y] = 0
            actions.append(f"Cleaned at ({x}, {y})")
            cleaned += 1
            print(f"Cleaned dirt at ({x}, {y})")
            print_grid()
        if all(cell == 0 for row in grid for cell in row):
            print("All tiles are clean!")
            break
        if y + 1 < cols: 
            y += 1
            actions.append("Move Right")
        elif x + 1 < rows: 
            x += 1
            y = 0
            actions.append("Move Down")
        else:  
            break
    print("Final Grid:")
    print_grid()
    print(f"Total Cleaned: {cleaned} tiles")
    return actions, grid
environment = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 0, 1]
]
start_position = (0, 0)
actions, final_grid = vacuum_cleaner(environment, start_position)
print("\nActions Taken:")
for action in actions:
    print(action)
