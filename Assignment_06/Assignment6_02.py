# Print Sum of Even Numbers Between 1 and 100. Use a loop to find and print the sum of all even numbers from 1 to 100.

def EvenNum():
    
    Num = 0
    for i in range(2,101,2):
        Num += i
    print("Sum Of Even Number 1 to 100 : ",Num)
        
EvenNum()
