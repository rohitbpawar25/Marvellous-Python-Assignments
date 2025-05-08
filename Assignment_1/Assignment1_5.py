# Write a program which displays numbers from 10 to 1 on the screen.

def Display(start,end):
    for num in range (start,end-1,-1):
        print(num)

print("Enter start number:")
start_num =int(input())
print("Enter end number :")
end_num = int(input())

Display(start_num,end_num)