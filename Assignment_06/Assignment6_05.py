# Accept a number from the user and check whether it is prime or not.

def ChkNum():

    Num = int(input("Enter a Number :"))
    if Num <= 1 :
        print(Num,"Not Prime")
        return 
    for i in range(2,Num):
        if Num % i == 0:
            print(Num,"Not Prime")
            return
    print(Num,"is Prime")
    return

ChkNum()