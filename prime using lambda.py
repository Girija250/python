def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if any(filter(lambda x: number % x == 0, range(2, int(number ** 0.5) + 1))):
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")
