# Print Triangle Pattern using Nested Loops

'''
*
* *
* * *
* * * *
* * * * *
'''

def Pattern(rows):

    for i in range(1, rows + 1):
        for j in range(i):
            print("*",end=" ")
        print()

Pattern(5)