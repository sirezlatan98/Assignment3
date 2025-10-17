#wap to define a function to find the factorial of a number using a loop or recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
number=int(input("Enter the number: "))
print(f"factorial of {number} is {factorial(number)}")
