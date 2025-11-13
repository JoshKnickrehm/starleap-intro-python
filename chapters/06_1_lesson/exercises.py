print("********** Ch 6 Exercise 1 **********")




print("********** Ch 6 Exercise 2 **********")



print("********** Ch 6 Exercise 3 **********")
print("********** Ch 6 Exercise 4 **********")

def is_power(b, c):
    if c == 1:
        print('It is a power of 2')
        return True
        
    elif c == b:
        print('It is a power of 2') 
        return True
        
    elif c > b:
        print(int(c))
        return is_power(b, c/b)
    else:
        print('it is not a power of 2')
        return False

# while True:
#     big_number = int(input('Give me a number '))
#     result = is_power(2, big_number)
#     print (result)
print("********** Ch 6 Exercise 5 **********")

def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b,a % b)
    
print(GCD(15,25))