"""
"""

from collections import Counter


class NearlyLucky:
    def solve(self, num):

        digitMap = Counter(num)

        count = digitMap["4"] + digitMap["7"]

        if count == 4 or count == 7:
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    nl = NearlyLucky()

    num = input()

    print(nl.solve(num))
