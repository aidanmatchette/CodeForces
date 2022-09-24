"""
"""


class InsomniaCure:
    def solve(self, k, la, m, n, d):
        count = 0
        for i in range(1, d + 1):
            if d % k == 0 or d % la == 0 or d % n == 0:
                count += 1
        return count


if __name__ == "__main__":
    ic = InsomniaCure()
    k = int(input())
    la = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    print(ic.solve(k, la, m, n, d))
