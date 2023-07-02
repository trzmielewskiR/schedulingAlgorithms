#Fm | | C_max
inputArray = input().split(' ')
m = int(inputArray[0])
n = int(inputArray[1])

tasks = []
for _ in range(n):
    inputArray = input().split(' ')
    newArray = [int(x) for x in inputArray]
    tasks.append(newArray)

machineQueue = [[] for _ in range(m)]
machineQueue[0] = list(range(n))
machineTask = [(-1, 0) for _ in range(m)]

readyTaskCount = 0
timeLeft = 0

while readyTaskCount < (n * m):
    for i in range(m):
        task, startTime = machineTask[i]
        if task == -1 and machineQueue[i]:
            index = machineQueue[i].pop(0)
            machineTask[i] = (index, timeLeft)
    timeLeft += 1
    for i in range(m):
        task, startTime = machineTask[i]
        if task != -1:
            taskRunTime = timeLeft - startTime
            if taskRunTime == tasks[task][i]:
                machineTask[i] = (-1, 0)
                readyTaskCount += 1
                if i < m - 1:
                    machineQueue[i + 1].append(task)
                else:
                    print(timeLeft)
