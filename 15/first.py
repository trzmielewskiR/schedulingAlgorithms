def solver(V, m, c, a):
    A = [[0.0] * m for _ in range(m)]

    for x in range(m - 1):
        left = a[x]
        right = a[x + 1] + c[x + 1]
        A[x][x] = left
        A[x][x + 1] = -right

    A[-1] = [1.0] * m
    #print(A)

    B = [0.0] * m
    B[-1] = V
    #print(B)

    solution = gauss_elimination(A, B)
    return solution


def gauss_elimination(A, B):
    n = len(A)

    for i in range(n):
        pivot = A[i][i]

        for j in range(i, n):
            A[i][j] /= pivot
        B[i] /= pivot

        for k in range(i + 1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            B[k] -= factor * B[i]

    solution = [0.0] * n
    solution[-1] = B[-1]

    for i in range(n - 2, -1, -1):
        total = B[i]
        for j in range(i + 1, n):
            total -= A[i][j] * solution[j]
        solution[i] = total

    return solution


C = []
A = []
V = int(input())
numberOfProcessors = int(input())
for i in range(numberOfProcessors):
    c, a = map(float, input().split())
    C.append(c)
    A.append(a)

sorted_pairs = sorted(zip(C,A))
A_sorted, C_sorted = zip(*sorted_pairs)
A_sorted = list(A_sorted)  
C_sorted = list(C_sorted)  

tasks = solver(V, numberOfProcessors, A_sorted, C_sorted)
#print(tasks)

results = []
zeroProcessortime = 0
for number, task in enumerate(tasks):
    zeroProcessortime = zeroProcessortime + task * A_sorted[number]
    add = task * C_sorted[number]
    results.append(zeroProcessortime + add)

maxTime = max(results)
print("{:.3f}".format(maxTime))


output_correct = sorted(tasks, key=lambda x: C.index(A_sorted[tasks.index(x)]))
for task in output_correct:
    print("{:.3f}".format(task))