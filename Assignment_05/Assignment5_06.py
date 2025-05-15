# Q6. Celsius to Fahrenheit Converter Write a program to accept temperature in Celsius and convert it to Fahrenheit using the formula: F = (C × 9/5) + 32

def Temp(Num1):
    F = (Num1 * 9/5) + 32
    return F

def main():

    Input = int(input("Enter temperature in Celsius :"))
    result = Temp(Input)
    print("Temperature in Fahrenheit :",result)

if __name__ == "__main__":
    main()