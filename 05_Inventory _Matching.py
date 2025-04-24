# Inventory: product -> (available_quantity, unit_price)
inventory = {
    "apple": (10, 2.0),
    "banana": (6, 1.0),
    "mango": (5, 3.0)
}

# Order: product -> quantity requested
order = {
    "apple": 4,
    "banana": 5,
    "mango": 3
}

# Customer budget
budget = 12.0

def check_order(inventory, order, budget):
    # Prepare a list of items: (unit_price, product, qty_needed, qty_available)
    items = []
    for product in order:
        if product in inventory:
            available, price = inventory[product]
            needed = order[product]
            items.append((price, product, needed, available))

    # Sort items by price (lowest first)
    items.sort()

    total_cost = 0
    fulfilled = {}

    for price, product, needed, available in items:
        qty_to_buy = min(needed, available)
        cost = qty_to_buy * price

        if total_cost + cost <= budget:
            total_cost += cost
            fulfilled[product] = qty_to_buy
        else:
            # Try to buy partial quantity
            remaining = budget - total_cost
            partial_qty = int(remaining // price)
            if partial_qty > 0:
                total_cost += partial_qty * price
                fulfilled[product] = partial_qty
            break

    # Determine status
    if all(fulfilled.get(p, 0) == order[p] for p in order):
        status = "✅ Order is fully fulfillable within budget."
    elif fulfilled:
        status = "⚠️ Order is partially fulfillable within budget."
    else:
        status = "❌ Order is not fulfillable within budget."

    print(status)
    print("Items fulfilled:", fulfilled)
    print("Total cost: $", round(total_cost, 2))

# Run the program
check_order(inventory, order, budget)
