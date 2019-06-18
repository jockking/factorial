#Factorial test

def calculateFactorial(factorial):
    num = 1
    for x in range(factorial, 1, -1):
        num = num * x
    return num    


val = input("Enter your value: ") 
print ('Factorial of ' + str(val) + ' is: ' + str(calculateFactorial(int(val))))