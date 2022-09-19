"""
"""


class BeautifulYear:
    def solve(self, start):

        while True:
            start = str(int(start) + 1)
            if len(set(start)) == 4:
                return int(start)


if __name__ == "__main__":
    by = BeautifulYear()

    start = int(input())

    print(by.solve(start))
