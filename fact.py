# Program to find the factorial of a number

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i
    print("hg")
print("Factorial of", num, "is", factorial)