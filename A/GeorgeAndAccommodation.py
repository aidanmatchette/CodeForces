"""
"""


class GeorgeAccommodation:
    def solve(self, rooms):
        count = 0
        for room in rooms:
            if int(room[1]) - int(room[0]) >= 2:
                count += 1
        return count


if __name__ == "__main__":
    ga = GeorgeAccommodation()
    n = int(input())
    rooms = list()

    for _ in range(n):
        rooms.append(input().split(" "))

    print(ga.solve(rooms))
