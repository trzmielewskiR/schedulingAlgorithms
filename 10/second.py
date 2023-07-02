# F | perm | C_max with NEH algorithm

def neh_algorithm(num_machines, num_jobs, processing_times):
    order = []
    available_jobs = list(range(1, num_jobs + 1))
    job_total_times = [sum(processing_times[i]) for i in range(num_jobs)]

    available_jobs.sort(key=lambda x: -job_total_times[x - 1])

    order.append(available_jobs[0])

    for i in range(1, num_jobs):
        best_position = -1
        min_total_processing_time = float('inf')

        for j in range(i + 1):
            order.insert(j, available_jobs[i])
            total_processing_time = calculate_total_processing_time(num_machines, i + 1, processing_times, order)
            if total_processing_time < min_total_processing_time:
                min_total_processing_time = total_processing_time
                best_position = j
            order.pop(j)

        order.insert(best_position, available_jobs[i])

    return order


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


num_machines, num_jobs = map(int, input().split())

processing_times = []
for _ in range(num_jobs):
    processing_times.append(list(map(int, input().split())))

order = neh_algorithm(num_machines, num_jobs, processing_times)

total_processing_time = calculate_total_processing_time(num_machines, num_jobs, processing_times, order)

print(total_processing_time)
print(*order)