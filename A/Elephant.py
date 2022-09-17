"""
"""


class Elephant:
    def solve(self, num):
        steps = [5, 4, 3, 2, 1]
        counter = 0

        while num > 0:

            for step in steps:
                if num >= step:
                    num -= step
                    counter += 1
                    break
        return counter


if __name__ == "__main__":
    num = int(input())

    e = Elephant()

    print(e.solve(num))
