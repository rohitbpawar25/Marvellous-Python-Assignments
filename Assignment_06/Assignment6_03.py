# Accept a number from the user and print its multiplication table up to 10.

def MulNum():

    Num = int(input("Enter a Number :"))
    for i in range(1,11):
        print(F"{Num} x {i} = {Num * i}")
    
MulNum()