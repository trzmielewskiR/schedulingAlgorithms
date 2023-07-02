#F3 | | C_max, 2nd machine is dominated

class Machine:
    def __init__(self):
        self.t = 0

    def process(self, task_time, acquire_time):
        self.t = max(self.t, acquire_time) + task_time
        return self.t


class Task:
    def __init__(self, task_id, p1, p2):
        self.id = task_id
        self.p1 = p1
        self.p2 = p2


A = []
B = []
p2_sum = 0

n = int(input())
P1 = Machine()
P2 = Machine()

for i in range(n):
    p1, p2, p3 = map(int, input().split())
    p2_sum += p2
    p1 += p2
    p2 += p3
    if p1 >= p2:
        B.append(Task(i + 1, p1, p2))
    else:
        A.append(Task(i + 1, p1, p2))

A.sort(key=lambda t: t.p1)
B.sort(key=lambda t: t.p2, reverse=True)

A.extend(B)

for task in A:
    first_end = P1.process(task.p1, 0)
    P2.process(task.p2, first_end)

print(P2.t - p2_sum)
