"""
If n is even, then the answer i n/2, otherwise the answer is (n -1) /2
"""


class CalculatingFunction:
    def solve(self, n):

        if n % 2 == 0:
            return n // 2
        else:
            return -1 * (n + 1) // 2


if __name__ == "__main__":
    cf = CalculatingFunction()
    n = int(input())

    print(cf.solve(n))
