# Accept 10 numbers from the user and write them into a file named numbers.txt, each on a new line.

def Add_Num(No):
    fobj = open("numbers.txt", "w")
    for num in No:
        fobj.write(f"{num}\n")
    fobj.close()  

def main():
    Data = []
    for i in range(10):
        num = int(input(f"Enter Number {i+1}: "))
        Data.append(num)
    Add_Num(Data)

if __name__ == "__main__":
    main()
