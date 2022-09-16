"""
"""


class BitPlus:
    def solve(self, operations):
        add = "++"
        sub = "--"
        ans = 0

        for check in operations:
            if add in check:
                ans += 1
            elif sub in check:
                ans -= 1
        return ans


if __name__ == "__main__":

    i = 0
    n = int(input())
    operations = list()

    while i < n:
        operations.append(input())
        i += 1

    bp = BitPlus()

    print(bp.solve(operations))
