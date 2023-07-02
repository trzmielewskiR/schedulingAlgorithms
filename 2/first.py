# 1 | r_j | C_max
n = int(input()) 
tasks = []
counter = 1

for i in range(n):
    c, d = map(int, input().split())
    tasks.append((c, d, counter))
    counter+=1

tasks.sort()

finish_times = []
current_time = 0
for task in tasks:
    start_time = max(current_time, task[0])  
    finish_time = start_time + task[1]  
    finish_times.append([finish_time, task[2]])
    current_time = finish_time  

#print(tasks)

finish_times.sort(key= lambda x: x[1])

for time in finish_times:
    print(time[0])


professor_finish_time = max(finish_times)
print(professor_finish_time[0])