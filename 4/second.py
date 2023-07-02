# 1 | | sigma U_j
n = int(input())
orders = []

for i in range(n):
    p, d = map(int, input().split())
    orders.append([i+1, p, d])
#print('orders: ', orders)

sortedByExecutionTime = sorted(orders, key=lambda x: x[2])


lateOrders = []

time = 0

for order in sortedByExecutionTime:
    lateOrders.append(order)
    oldTime = time
    time += order[1]
    sortedLateOrders = sorted(lateOrders, key=lambda x: x[1])
    if time > order[2]:
        biggestExecutionTime = sortedLateOrders.pop()
        lateOrders.remove(biggestExecutionTime)
        time = time - biggestExecutionTime[1]


result = len(lateOrders)
print(result)
