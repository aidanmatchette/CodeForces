"""
"""


class WrongSubtraction:
    def solve(self, n, k):
        for _ in range(k):
            if n % 10 == 0:
                n //= 10
            else:
                n -= 1
        return n


if __name__ == "__main__":
    ws = WrongSubtraction()
    n, k = map(int, input().split(" "))
    print(ws.solve(n, k))
