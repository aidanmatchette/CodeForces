"""
"""


class Word:
    def solve(self, word):
        upper = 0
        length = len(word)

        for char in word:
            if char == char.upper():
                upper += 1

        if upper > length / 2:
            return word.upper()

        else:
            return word.lower()


if __name__ == "__main__":
    w = Word()
    word = str(input())

    print(w.solve(word))
