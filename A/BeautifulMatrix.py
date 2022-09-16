"""
"""


class BeautifulMatrix:
    def solve(self, matrix):
        moves = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == "1":
                    moves = abs(3 - (r + 1)) + abs(3 - (c + 1))
        return moves


if __name__ == "__main__":
    matrix = list()
    i = 5
    while i > 0:
        matrix.append(input().split(" "))
        i -= 1

    bm = BeautifulMatrix()
    print(bm.solve(matrix))
