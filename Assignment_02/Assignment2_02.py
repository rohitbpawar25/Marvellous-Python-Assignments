# Write a program that accepts one number and displays the following pattern. 
# 5
"""
* * * * *  
* * * * *  
* * * * *  
* * * * * 

"""

def DisplayPattern(n):
    for i in range(n):
        print (" * " * n)
        
DisplayPattern(5)