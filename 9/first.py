# O2 | | C_max

amount = int(input())
tasks = []

for i in range(amount):
    time1, time2 = map(int, input().split())
    tasks.append((i, [time1, time2]))

tasks_sorted_by_second_desc = sorted(tasks, key=lambda x: -x[1][1])
tasks_sorted_by_first_desc = sorted(tasks, key=lambda x: -x[1][0])
tasks = [tasks_sorted_by_second_desc, tasks_sorted_by_first_desc]

time_left = 0
task_on = [-1, -1]
task_on_start_time = [0, 0]
task_on_local_index = [-1, -1]

while len(tasks[0]) > 0 or len(tasks[1]) > 0:
    for i in range(2):
        if task_on[i] != -1:
            index, times = tasks[i][task_on_local_index[i]]
            task_time = time_left - task_on_start_time[i]
            if times[i] <= task_time:
                tasks[i].pop(task_on_local_index[i])
                task_on[i] = -1
                task_on_local_index[i] = -1
    for i in range(2):
        if len(tasks[i]) > 0 and task_on[i] == -1:
            for j in range(len(tasks[i])):
                index, times = tasks[i][j]
                second_machine = (i + 1) % 2
                if index != task_on[second_machine]:
                    task_on[i] = index
                    task_on_local_index[i] = j
                    task_on_start_time[i] = time_left
                    break
    time_left += 1

print(time_left - 1)
