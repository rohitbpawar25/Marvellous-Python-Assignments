# Even or Odd Number Check Write a program to check whether the entered number is even or odd.

def Chkodd(Num1):
    if Num1 % 2 == 0:
        return (": is an Even")
    else:
        return (": is an odd")

def main():
    Input = int(input("Enter Number :"))
    result = Chkodd(Input)
    print(Input,result)

if __name__ == "__main__":
    main()