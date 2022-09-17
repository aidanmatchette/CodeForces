"""
"""


class SoldierBananas:
    def solve(self, cost, banana, money):
        counter = 1

        total_cost = 0

        while counter <= banana:
            total_cost += cost * counter
            counter += 1
        return total_cost - money if total_cost - money > 0 else 0


if __name__ == "__main__":
    sb = SoldierBananas()
    cost, money, banana = map(int, input().split(" "))
    print(sb.solve(cost, banana, money))
