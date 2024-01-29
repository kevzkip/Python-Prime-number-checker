def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

while True:
    # Ask the user for input
    num = input("Enter a number (or 'X' to quit): ")

    if num.lower() == 'X':
        break

    num = int(num)

    # Check if the number is prime and print the result
    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
