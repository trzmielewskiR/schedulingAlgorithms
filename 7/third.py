# 1 | | sigma w_j U_j but using dynamic programming

items = []
n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    items.append([x,y,z])


sortedItems = sorted(items, key=lambda x: x[2])

A = [[0 for x in range(sortedItems[n-1][2]+1)] for j in range(n+1)]


for j in range(n+1):
    for t in range(sortedItems[n-1][2]+1):
        if j == 0:
            A[j][t] = 0
        elif t == 0:
            A[j][t] = sum([item[1] for item in sortedItems[:j]])
        elif t <= sortedItems[j-1][2]:
            if t >= sortedItems[j-1][0]:
                A[j][t] = min(A[j-1][t-sortedItems[j-1][0]], A[j-1][t] + sortedItems[j-1][1])
            else:
                A[j][t] = A[j-1][t] + sortedItems[j-1][1]
        else:
            A[j][t] = A[j][sortedItems[j-1][2]]
bag = A[n-1][sortedItems[n-1][2]]

sumAfterWeights = 0

for item in sortedItems:
    sumAfterWeights += item[1]


L = []
t = sortedItems[n-1][2]
for j in range(n, 0, -1):
    t = min(t, sortedItems[j-1][2])
    if A[j][t] == A[j-1][t] + sortedItems[j-1][1]:
        L.append(sortedItems[j-1])
    else:
        t = t - sortedItems[j-1][0]


L=sorted(L)
results = []

for item in items:
    if item not in L:
        results.append(item)

suma = sum(task[1] for task in results)
print(suma)
for item in items:
    if item not in L:
        index = items.index(item)
        print(index+1)