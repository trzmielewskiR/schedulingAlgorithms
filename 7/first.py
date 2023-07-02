#P2||C_max but using dynamic programming

items = []
n = int(input())
for i in range(n):
    x = int(input())
    items.append(x)

BB = int(sum(items))
B = int(sum(items)/2)

matrix = [[False for x in range(B+1)] for j in range(n+1)]


for i in range(n+1):
    matrix[i][0] = True
for j in range(1, B+1):
    matrix[0][j] = False
for i in range(1, n+1):
    for j in range(1, B+1):
        matrix[i][j] = matrix[i-1][j]
        if items[i-1] <= j:
            matrix[i][j] = True if (matrix[i-1][j-items[i-1]]
                                 or matrix[i][j]) else False


j = B
for x in range(j, 0, -1):
    if x == B and matrix[n][x] == True:
        C = j
        break
    elif x < B and matrix[n][x] == True:
        C = x
        break

print(C, BB-C)
