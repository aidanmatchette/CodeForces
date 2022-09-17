"""
"""


class WordCapitalization:
    def solve(self, word):
        if len(word) > 0:
            return word[0].upper() + word[1:]
        else:
            return word


if __name__ == "__main__":

    word = input()
    wc = WordCapitalization()
    print(wc.solve(word))
