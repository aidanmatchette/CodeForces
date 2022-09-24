"""
"""


class InsomniaCure:
    def solve(self, k, la, m, n, d):
        count = 0
        for i in range(1, d + 1):
            if i % k == 0 or i % la == 0 or i % m == 0 or i % n == 0:
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
