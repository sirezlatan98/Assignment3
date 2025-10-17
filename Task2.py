#WAP to use math module to find suare root, natural logarithm and sine
import math
def math_fun(number):
    print("Square root:",math.sqrt(number))
    print("Logarithm:",math.log(number))
    print("Sine:",math.sin(number))

number=int(input("Enter the number: "))
math_fun(number)
