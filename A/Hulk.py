"""
"""


class Hulk:
    def solve(self, n):
        odd = "I love that "
        even = "I hate that "
        res = ""

        for i in range(n):
            if i % 2 == 0:
                res += even
            else:
                res += odd
        splt_res = res.split(' ')
        return " ".join(splt_res[:-2]) + " it"


if __name__ == "__main__":
    h = Hulk()
    n = int(input())
    print(h.solve(n))
