"""
"""


class HelpfulMaths:
    def solve(self, eq):
        if "+" not in eq:
            return eq

        nums = list(map(int, eq.split("+")))
        nums.sort()
        return "+".join(str(num) for num in nums)


if __name__ == "__main__":

    eq = input()

    hm = HelpfulMaths()

    print(hm.solve(eq))
