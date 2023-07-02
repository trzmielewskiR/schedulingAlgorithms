# P | | C_max

orders = []

def minimumLoad(loads):
    minLoad = min(loads)
    for proc, load in enumerate(loads):
        if load == minLoad:
            return proc


# m, n = map(int, input().split())
# for i in range(n):
#     x = int(input())
#     orders.append([i+1, x])

# orders_sorted = sorted(orders, reverse = True, key= lambda x: x[1])

m, n = map(int, input().split())
for i in range(n):
    x = int(input())
    orders.append(x)

orders_sorted = sorted(orders, reverse=True)

loads = []
scheduled_orders = []

for processor in range(m):
    loads.append(0)
    scheduled_orders.append([])

for order in orders_sorted:
    minimumLoadProcessor = minimumLoad(loads)
    scheduled_orders[minimumLoadProcessor].append(order)
    loads[minimumLoadProcessor] += order


print(max(loads))