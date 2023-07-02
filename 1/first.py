# 1||C_max
tests = []
result = 0

n = input()
tests = input().split()
for number in tests:
    result = result + int(number)
print(result)