"""
"""


class Magnets:
    def solve(self, mags):
        groups = 1

        for i in range(len(mags) - 1):
            if mags[i][1] == mags[i + 1][0]:
                groups += 1
        return groups


if __name__ == "__main__":
    m = Magnets()
    n = int(input())

    mags = list()

    for _ in range(n):
        mags.append(list(input()))

    print(m.solve(mags))
