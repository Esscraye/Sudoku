class Solver:
    def __init__(self, M=9):
        self.M = M

    def check(self, grid, row, col, num):
        for x in range(self.M):
            if grid[row][x] == num:
                return False

        for x in range(self.M):
            if grid[x][col] == num:
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True

    def backtracking(self, grid, row, col):
        if row == self.M - 1 and col == self.M:
            return True
        if col == self.M:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return self.backtracking(grid, row, col + 1)

        for num in range(1, self.M + 1, 1):
            if self.check(grid, row, col, num):
                grid[row][col] = num
                if self.backtracking(grid, row, col + 1):
                    return True
            grid[row][col] = 0
        return False

    def solve(self, grid):
        if self.backtracking(grid, 0, 0):
            print(grid)
        else:
            print("Solution does not exist :(")
