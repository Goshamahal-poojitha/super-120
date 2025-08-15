def dfs(i, j, visited, grid, n, m):
    visited[i][j] = 1
    for r, c in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        nRow = i + r
        nCol = j + c
        if 0 <= nRow < n and 0 <= nCol < m and grid[nRow][nCol] == "1" and visited[nRow][nCol] == 0:
            dfs(nRow, nCol, visited, grid, n, m)

def numsIlands(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[0] * m for _ in range(n)]
    c = 0
    for i in range(n):
        for j in range(m):  # Bug fix: loop over range(m), not range(n)
            if grid[i][j] == '1' and visited[i][j] == 0:
                dfs(i, j, visited, grid, n, m)
                c += 1
    return c

# --- User Input Section ---
n = int(input("Enter the number of rows: "))
grid = []

print("Enter the grid rows with space-separated values (e.g., 1 0 1):")
for _ in range(n):
    row = input().split()
    grid.append(row)


print("Number of islands:", numsIlands(grid))
# Output the result
#Enter the number of rows: 4
#Enter the grid rows with space-separated values (e.g., 1 0 1):
#1 1 0 1
#1 0 0 1
#0 0 0 0 
#0 0 1 0 
#Number of islands: 3