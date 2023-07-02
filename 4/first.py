#1 | | L_max

n = int(input())
orders = []


for i in range(n):
    p, d = map(int, input().split())
    orders.append([i+1, p, d])
#print('orders: ', orders)

delays = sorted(orders, key=lambda x: x[2])

done = []
time = 0
for argument in delays:
    time = time + argument[1]
    done.append([argument[0], time])

done = sorted(done, key = lambda x: x[0])
#print('done: ', done)
maximumLags = []
for x in range(n):
    difference = done[x][1] - orders[x][2]
    #print(difference)
    maximumLags.append(difference)

maximumLag = max(maximumLags)
#print('delays:', delays)
print(maximumLag)