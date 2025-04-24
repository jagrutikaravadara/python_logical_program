import heapq

def max_tasks(tasks):
    # Sort tasks by deadline (earliest first)
    tasks.sort(key=lambda t: t['deadline'])# lambda function use
    
    total_time = 0
    max_heap = []  # Store durations as negative values to use as max-heap

    for task in tasks:
        duration = task['duration']
        deadline = task['deadline']
        
        if total_time + duration <= deadline:
            heapq.heappush(max_heap, -duration)
            total_time += duration
        elif max_heap and -max_heap[0] > duration:
            # Replace longer task with shorter one to save time
            total_time += duration + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -duration)

    return len(max_heap)

# Example input
tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

print("Max tasks that can be completed:", max_tasks(tasks))
