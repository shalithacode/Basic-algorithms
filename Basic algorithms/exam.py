#initial user inputs
x = int(input("Enter base : "))
n = int(input("Enter expression : "))

#function for base, expression calculation 
def power(base,exp):
    if(exp == 0):
        return 1
    elif(exp > 0):
        return base * pow(base, exp-1)

#to run the program user inputs =1
while (x != 1 and n != 1):
    print(power(x,n))                       #function call
    x = int(input("Enter base : "))
    n = int(input("Enter expression : "))

#If user inputs =1    
if (x == 1 and n == 1):
    print(power(x,n))
