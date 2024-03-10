def factorial_finder(n):
    """Factorial Finding Maths Stuff Returns The Factorial"""
    factorial = 1
    for i in range(1, n+1):
        factorial = i*factorial
    return factorial

# Made it so you can enter your own number
while True:
    factor = input("Enter a positive number to calculate factorial: ")

    try: 
        factor = int(factor)
        print(f"The factorial of {factor} is {factorial_finder(factor)}")
        break
    except ValueError:
        print("\nEither your number is too big, or you didn't enter a number at all.\n")