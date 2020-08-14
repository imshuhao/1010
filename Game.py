class GameMap:

    def __init__(self, size: int = 10):
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.point = 0
        self.size = size

    def __empty_row(self, n: int):
        self.grid[n] = [0 for _ in range(self.size)]

    def __empty_col(self, n: int):
        for row in self.grid:
            row[n] = 0

    def check_all(self):
        for row in self.grid:
            if all(row):
                self.point += self.size
                row = [0 for _ in range(self.size)]
        for i in range(self.size):
            pass
