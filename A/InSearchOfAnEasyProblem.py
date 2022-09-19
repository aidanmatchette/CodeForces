"""
"""


class EasyProblem:
    def solve(self, responses):
        return "HARD" if "1" in responses else "EASY"


if __name__ == "__main__":
    n = int(input())

    responses = list(input().split(" "))

    ep = EasyProblem()

    print(ep.solve(responses))
