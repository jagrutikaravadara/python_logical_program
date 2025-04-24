import heapq

def dijkstra(graph, start, end):
    q, seen = [(0, start, [])], set()
    while q:
        dist, node, path = heapq.heappop(q)
        if node in seen: continue
        seen.add(node)
        path += [node]
        if node == end: return dist, path
        for nei, d in graph.get(node, {}).items():
            if nei not in seen:
                heapq.heappush(q, (dist + d, nei, path))
    return float('inf'), []

# Example input
cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}
start, end = 'A', 'D'

# Run and print result
dist, path = dijkstra(cities, start, end)
print(f"Path: {' -> '.join(path)}\nDistance: {dist}")
    