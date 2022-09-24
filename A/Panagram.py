"""
"""

from collections import Counter


class Panagram:
    def solve(self, n, word):
        chars = set()

        for i in word:
            chars.add(i.lower())
        return "YES" if len(chars) == 26 else "NO"


if __name__ == "__main__":
    p = Panagram()
    n = int(input())
    word = input()
    print(p.solve(n, word))
