# 1||sigma w_j c_j

base_list = []
n = int(input())
for x in range(n):
    x = input().split()
    input_result = (int(x[0]), int(x[1]))
    base_list.append(input_result)

for result in base_list:
    pass
    #print('czas wykonania: {}, czas zakonczenia: {}, ratio:  {}'.format(result[0], result[1], (result[0]/result[1])))

ratio_list = [(result[0]/result[1]) for result in base_list]
counter = 0
dictWithValues = {}
for values in base_list:
    counter += 1
    dictWithValues[counter] = values[0]/values[1]

dictionarySorted = sorted(dictWithValues.items(), key = lambda x:x[1])
#print(dictWithValues)
#print(dictionarySorted)
#print(ratio_list)

result = 0
all_time = 0
for number in dictionarySorted:
    #print(number[0])
    element = base_list[number[0]-1]
    all_time += element[0]
    result += (element[1] * all_time)

print(result)