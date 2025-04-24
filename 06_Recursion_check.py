

def countdown(n):
    if n < 1:
        return
    print(n)
    countdown(n - 1)

# Call the function starting from 1000
countdown(1000)
