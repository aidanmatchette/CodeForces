"""
"""


class Presents:
    def solve(self, gifts):
        res = [0 for _ in range(len(gifts))]

        for i in range(len(gifts)):
            res[int(gifts[i]) - 1] = i + 1
        return " ".join(str(item) for item in res)


if __name__ == "__main__":
    p = Presents()
    n = int(input())
    gifts = list(input().split(" "))
    print(p.solve(gifts))
