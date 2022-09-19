"""
"""


class Translation:
    def solve(self, word1, word2):

        rev = ""
        for i in reversed(range(len(word1))):
            rev += word1[i]
        return "YES" if rev == word2 else "NO"


if __name__ == "__main__":
    word1 = input()
    word2 = input()

    t = Translation()

    print(t.solve(word1, word2))
