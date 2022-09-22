"""
"""


class WannaBe:
    def solve(self, n, x, y):

        x = x[1:]
        y = y[1:]
        levels = set()
        levels.update(x)
        levels.update(y)

        return "I become the guy." if len(levels) == n else "Oh, my keyboard!"


if __name__ == "__main__":
    wb = WannaBe()
    n = int(input())
    x = list(map(int, input().split(" ")))
    y = list(map(int, input().split(" ")))
    print(wb.solve(n, x, y))
