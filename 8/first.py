# 1 | | w_j U_J but using branch and bound

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight 


def branch_and_bound_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    n = len(items)
    max_value = 0
    best_solution = [0] * n
    
    def backtrack(i, current_weight, current_value, solution):
        nonlocal max_value, best_solution 
        
        if i == n:
            if current_value > max_value:
                max_value = current_value
                best_solution = solution[:]
            return
        
        if current_weight + items[i].weight <= capacity:
            solution[i] = 1
            backtrack(i + 1, current_weight + items[i].weight, current_value + items[i].value, solution)
        
        if (current_value + biggestPossibleSolution(i + 1, current_weight, items)) > max_value:
            solution[i] = 0
            backtrack(i + 1, current_weight, current_value, solution)
    
    def biggestPossibleSolution(k, current_weight, items):
        biggestPossibleSolution = 0
        potential_weight = current_weight
        
        while k < n and potential_weight + items[k].weight <= capacity:
            potential_weight += items[k].weight
            biggestPossibleSolution += items[k].value
            k += 1
        
        if k < n:
            biggestPossibleSolution += (capacity - potential_weight) * items[k].ratio
        
        return biggestPossibleSolution
    
    backtrack(0, 0, 0, [0] * n)
    
    return max_value, best_solution


items = []
numberOfOrders, capacity = map(int, input().split())
for i in range(numberOfOrders):
    weight, price = map(int, input().split())
    items.append(Item(weight, price))

max_value, best_solution = branch_and_bound_knapsack(items, capacity)

print(max_value)

