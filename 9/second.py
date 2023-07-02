#F2 | | C_max

amount = int(input())
tasks = []
A = []
B = []

for i in range(amount):
    time1, time2 = input().split()
    tasks.append((i, [int(time1), int(time2)]))
    if int(time1) <= int(time2):
        A.append(i)
    else:
        B.append(i)

def sortA(e):
    index, times = tasks[e]
    return times[0]

def sortB(e):
    index, times = tasks[e]
    return -times[1]

A.sort(key=sortA)
B.sort(key=sortB)
queueA = A + B
queueB = []
tasksAB = [queueA, queueB]

timeLeft = 0
taskOn = [-1, -1]
taskOnStartTime = [0, 0]
result = rulesFor = [[x, 0, 0] for x in range(amount)]

while len(tasksAB[0]) > 0 or len(tasksAB[1]) > 0:
    for i in range(2):
        if taskOn[i] != -1:
            index, times = tasks[tasksAB[i][0]]
            taskTime = timeLeft - taskOnStartTime[i]
            if times[i] <= taskTime:
                taskIndex = tasksAB[i].pop(0)
                taskOn[i] = -1
                result[taskIndex][i + 1] = timeLeft
                if i == 0:
                    tasksAB[1].append(taskIndex)
    for i in range(2):
        if len(tasksAB[i]) > 0 and taskOn[i] == -1:
            index, times = tasks[tasksAB[i][0]]
            taskOn[i] = index
            taskOnStartTime[i] = timeLeft
    timeLeft += 1

def resultSort(e):
    return e[2]

result.sort(key=resultSort)
for res in result:
    print(str(res[0] + 1) + ' ' + str(res[1]) + ' ' + str(res[2]))
