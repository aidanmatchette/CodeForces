"""
"""


class UltraFast:
    def solve(self, num1, num2):
        res = ""
        for i in range(len(num1)):
            if num1[i] != num2[i]:
                res += "1"
            else:
                res += "0"
        return int(res)


if __name__ == "__main__":
    uf = UltraFast()
    num1 = list(input())
    num2 = list(input())
    print(uf.solve(num1, num2))
