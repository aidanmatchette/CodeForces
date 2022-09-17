"""
"""


class BoyOrGirl:
    def solve(self, name):
        chars = set()

        for char in name:
            if char in chars:
                continue
            chars.add(char)

        if len(chars) % 2 == 0:
            return "CHAT WITH HER!"
        else:
            return "IGNORE HIM!"


if __name__ == "__main__":
    bg = BoyOrGirl()

    name = input()

    print(bg.solve(name))
