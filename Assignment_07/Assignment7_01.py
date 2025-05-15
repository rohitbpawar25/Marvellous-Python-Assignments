# Write two lambda functions: One to calculate the square of a number Another to calculate the cube of a number

Square = lambda Num1 : Num1 ** 2
Cube = lambda Num1 : Num1 ** 3

Input = int(input("Enter a number :"))

print("Square is :",Square(Input))
print("Cube is :",Cube(Input))