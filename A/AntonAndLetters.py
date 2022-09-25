"""
"""


class AntonLetters:
    def solve(self, chars):
        distinct = set()
        for char in chars:
            if char.isalpha():
                distinct.add(char)

        return len(distinct)


if __name__ == "__main__":
    al = AntonLetters()
    chars = input()
    print(al.solve(chars))

