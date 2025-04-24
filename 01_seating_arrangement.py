from itertools import permutations

def is_valid(arrangement, preferences):
    n = len(arrangement)
    for i in range(n):
        guest = arrangement[i]
        left = arrangement[(i - 1) % n]
        right = arrangement[(i + 1) % n]
        if set(preferences[guest]) != set([left, right]):
            return False
    return True

def find_seating(preferences):
    guests = list(preferences.keys())
    first = guests[0]
    for perm in permutations(guests[1:]):
        circle = [first] + list(perm)
        if is_valid(circle, preferences):
            return circle
    return None

# Example input
guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

result = find_seating(guests)

if result:
    print("Valid seating arrangement:")
    print(" -> ".join(result))
else:
    print("No valid seating arrangement possible.")
