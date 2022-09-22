"""
"""


class Horseshoe:
    def solve(self, shoes):
        curr = set(shoes)

        return len(shoes) - len(curr)


if __name__ == "__main__":
    h = Horseshoe()

    shoes = list(map(int, input().split(" ")))

    print(h.solve(shoes))
