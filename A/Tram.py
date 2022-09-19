"""
"""


class Tram:
    def solve(self, passengers):
        max_pass = 0

        curr = 0

        for stop in passengers:
            leave, entry = stop
            curr -= leave
            curr += entry

            max_pass = max(max_pass, curr)
        return max_pass


if __name__ == "__main__":
    n = int(input())

    passengers = list()

    for _ in range(n):
        passengers.append(map(int, input().split(" ")))
    t = Tram()

    print(t.solve(passengers))
