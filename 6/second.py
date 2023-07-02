# Q| | sigma C_j
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
wages = list(map(int, input().split()))

for i in range(n):
    x = int(input())
    orders.append([i+1, x])

SPT = sorted(orders, key = lambda x: x[1], reverse=True)

for machine in range(m):
    scheduledOrders.append([])


wagesStandard = wages.copy()
counter = 0
for order in SPT:
    minimalWage = min(wages)
    minimalWageIndex = wages.index(minimalWage)
    scheduledOrders[minimalWageIndex].insert(0, [order[0], order[1]*wagesStandard[minimalWageIndex]])
    minimalWage = minimalWage + wagesStandard[minimalWageIndex]
    wages[minimalWageIndex] = minimalWage


results = list(map(timeSumForOneMachine, scheduledOrders))
#print(results)
result = sum(results)
print(result)