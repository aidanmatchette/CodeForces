"""
"""


class Drinks:
    def solve(self, n, amount):
        res = 0
        for num in amount:
            res += num
        return res / n


if __name__ == "__main__":
    d = Drinks()
    n = int(input())
    amount = list(map(int, input().split(" ")))
    print(d.solve(n, amount))
