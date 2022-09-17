"""
"""


class BigBear:
    def solve(self, ler, b):
        count = 0

        while ler <= b:
            ler *= 3
            b *= 2
            count += 1
        return count


if __name__ == "__main__":
    ler, b = map(int, input().split(" "))

    bg = BigBear()
    print(bg.solve(ler, b))
