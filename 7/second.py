#knapsack problem but using dynamic programming

items = []
n, B = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    items.append([x,y])


matrix = [[0 for x in range(B+1)] for j in range(n+1)]

for i in range(n+1):
    for j in range(B+1):
        if i==0 or j==0:
            matrix[i][j] = 0
        elif items[i-1][0] > j:
            matrix[i][j] = matrix[i-1][j]
        else:
            matrix[i][j] = max(matrix[i-1][j], (matrix[i-1][j-items[i-1][0]]) + items[i-1][1])

print(matrix[n][B])

chosen_items = []
j = B
for i in range(n, 0, -1):
    if matrix[i][j] != matrix[i-1][j]:
        chosen_items.append(i)
        j = j - items[i-1][0]

'''
for i in range(n, 0, -1):
    if selected[i][current_capacity]:
        chosen_items.append(i)
        current_capacity -= items[i-1][0]
'''

chosen_items.reverse()

for number in chosen_items:
    print(number)
