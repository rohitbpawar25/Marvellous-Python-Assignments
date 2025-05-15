# Write a function that accepts a list of integers and returns a list of prime numbers using filter().

PrimeNum = lambda num : num > 1 and all(num % i for i in range(2, num))

def main():
    Data = []
    Input = int(input("Enter Number of Data you want to Add :"))

    for i in range (Input):
        Values = int(input("Enter Data :"))
        Data.append(Values)
    print("Data in List :",Data)

    FData = list(filter(PrimeNum,Data))
    print("prime Numbers Are :",FData)

if __name__ == "__main__":
    main()