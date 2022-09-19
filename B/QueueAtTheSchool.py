"""
"""


class QueueAtSchool:
    def solve(self, t, queue):
        for _ in range(t):
            i = 0
            while i < (len(queue) - 1):
                if queue[i] == "B" and queue[i + 1] == "G":
                    queue[i], queue[i + 1] = queue[i + 1], queue[i]
                    i = i + 2
                else:
                    i += 1
        return "".join(queue)


if __name__ == "__main__":
    qs = QueueAtSchool()

    n, t = map(int, input().split(" "))

    queue = list(input())

    print(qs.solve(t, queue))
