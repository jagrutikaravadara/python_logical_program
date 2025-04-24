def transaction_manager():
    balance = 0
    transactions = []

    print("Welcome to the Transaction Manager!")
    print("Enter transactions one by one.")
    print("Use +amount for credit and -amount for debit (e.g., +1000, -250).")
    print("Type 'done' to finish.\n")

    while True:
        entry = input("Enter transaction: ").strip()
        if entry.lower() == 'done':
            break
        try:
            amount = float(entry)
            balance += amount
            transaction_type = "Credit" if amount > 0 else "Debit"
            transactions.append((transaction_type, abs(amount), balance))
            print(f"{transaction_type} of ₹{abs(amount):.2f} | New Balance: ₹{balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number like +100 or -50.")

    # Final Summary
    print("\n--- Transaction Summary ---")
    for i, (t_type, amt, bal) in enumerate(transactions, 1):
        print(f"{i}. {t_type}: ₹{amt:.2f} | Balance after: ₹{bal:.2f}")
    print(f"\nFinal Balance: ₹{balance:.2f}")

# Run the program
transaction_manager()

