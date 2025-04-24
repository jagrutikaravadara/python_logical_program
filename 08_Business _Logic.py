def calculate_bill(units):
    bill = 0
    print("Electricity Bill:\n")

    if units <= 100:
        bill = units * 5
        print(f"0-{units} units @ ₹5/unit = ₹{bill}")

    elif units <= 300:
        slab1 = 100 * 5
        slab2 = (units - 100) * 7
        bill = slab1 + slab2
        print("0-100 units @ ₹5/unit = ₹", slab1)
        print(f"101-{units} units @ ₹7/unit = ₹{slab2}")

    elif units <= 500:
        slab1 = 100 * 5
        slab2 = 200 * 7
        slab3 = (units - 300) * 10
        bill = slab1 + slab2 + slab3
        print("0-100 units @ ₹5/unit = ₹", slab1)
        print("101-300 units @ ₹7/unit = ₹", slab2)
        print(f"301-{units} units @ ₹10/unit = ₹{slab3}")

    else:
        slab1 = 100 * 5
        slab2 = 200 * 7
        slab3 = 200 * 10
        slab4 = (units - 500) * 15
        bill = slab1 + slab2 + slab3 + slab4
        print("0-100 units @ ₹5/unit = ₹", slab1)
        print("101-300 units @ ₹7/unit = ₹", slab2)
        print("301-500 units @ ₹10/unit = ₹", slab3)
        print(f"501-{units} units @ ₹15/unit = ₹{slab4}")

    print("\nTotal Amount Payable = ₹", bill)

# Get user input
usage = int(input("Enter electricity usage in kWh: "))
calculate_bill(usage)

     