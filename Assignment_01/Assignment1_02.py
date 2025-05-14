# write a program that contains a function named ChkNum(), which accepts one number as a parameter. If the number is even, the function should display "Even number", otherwise "Odd number"



def ChkNum(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

ChkNum(11)  
ChkNum(8) 


'''
def ChkNum(number):
   if number % 2 == 0:
    return "Even number"
   else:
     return "Odd number"
    
def main():
    print("Enter a number: ")
    value = int(input())
    result = ChkNum(value)
    print(" Answer : ", result)

if __name__ == "__main__":
    main()

'''