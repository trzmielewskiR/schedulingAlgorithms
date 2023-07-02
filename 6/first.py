# P| | sigma C_j

def timeSumForOneMachine(listOfOrders):
    result = 0
    lastArgumentTime = 0
    for order in listOfOrders:
        lastArgumentSum = (order[1] + lastArgumentTime)
        result = result + lastArgumentSum
        lastArgumentTime = lastArgumentSum
    return result


orders = []
scheduledOrders = []
m, n = map(int, input().split())
for i in range(n):
    x = int(input())
    orders.append([i+1, x])

SPT = sorted(orders, key = lambda x: x[1])

for machine in range(m):
    scheduledOrders.append([])


counter = 0
for order in SPT:
    machineNumber = counter % m
    counter += 1
    scheduledOrders[machineNumber].append(order)


results = list(map(timeSumForOneMachine, scheduledOrders))
#print(results)
result = sum(results)
print(result)