"""
"""


class CalculatingFunction:
    def solve(self, n):
        res = 0

        for i in range(1, n + 1):
            if i % 2 == 0:
                res += i
            else:
                res -= i
        return res


if __name__ == "__main__":
    cf = CalculatingFunction()
    n = int(input())

    print(cf.solve(n))
