#genetic algorithm with spaced crossing
import random

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point]
    child2 = parent2[:crossover_point]

    for task in parent2:
        if task not in child1:
            child1.append(task)

    for task in parent1:
        if task not in child2:
            child2.append(task)

    return child1, child2

def mutate(individual):
    index1 = random.randint(0, len(individual) - 1)
    index2 = random.randint(0, len(individual) - 1)
    
    while index1 == index2: 
        index2 = random.randint(0, len(individual) - 1)
        
    individual[index1], individual[index2] = individual[index2], individual[index1]
    return individual

def calculate_total_processing_time(num_machines, num_jobs, processing_times, order):
    completion_times = [0] * num_machines

    for job_id in order:
        job_processing_times = processing_times[job_id - 1]
        for j in range(num_machines):
            if j == 0:
                completion_times[j] += job_processing_times[j]
            else:
                completion_times[j] = max(completion_times[j], completion_times[j - 1]) + job_processing_times[j]

    return completion_times[num_machines - 1]

def initialize_population(num_jobs, population_size):
    population = []
    for _ in range(population_size):
        order = random.sample(range(1, num_jobs + 1), num_jobs)
        population.append(order)
    return population


def genetic_algorithm(num_machines, num_jobs, processing_times, population_size=300, num_iterations=100):

    mutation_rate = 0.4;
    population = initialize_population(num_jobs, population_size)

    for _ in range(num_iterations):
        # scoring population
        fitness_scores = []
        for individual in population:
            fitness = calculate_total_processing_time(num_machines, num_jobs, processing_times, individual) #dziwnie to wyglada
            fitness_scores.append(fitness)

        new_population = []
        for _ in range(population_size // 2):
            # tournament selection
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(child1)
            new_population.append(child2)

        # mutation
        for i in range(population_size):
            if random.random() < mutation_rate:
                new_population[i] = mutate(new_population[i])

        population = new_population

    best_fitness = float('inf')
    best_individual = None
    for individual in population:
        fitness = calculate_total_processing_time(num_machines, num_jobs, processing_times, individual)
        if fitness < best_fitness:
            best_fitness = fitness
            best_individual = individual.copy()

    return best_individual

#input
num_machines, num_jobs = map(int, input().split())

processing_times = []
for _ in range(num_jobs):
    processing_times.append(list(map(int, input().split())))

result = genetic_algorithm(num_machines, num_jobs, processing_times)
print(calculate_total_processing_time(num_machines, num_jobs, processing_times, result))
print(*result)