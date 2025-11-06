print("********** Ch 6 Exercise 1 **********")




print("********** Ch 6 Exercise 2 **********")



print("********** Ch 6 Exercise 3 **********")

print("********** Ch 6 Exercise 4 **********")

def is_power(b, c):
    if c == 1:
        return True
    elif c == b:
        return True
    elif c > b:
        print(int(c))
        return is_power(b, c/b)
    else:
        return False

while True:
    big_number = int(input('Give me a number'))
    result = is_power(2, big_number)
    print (result)







print("Ch 6 Exercise 4: Not implemented") # Delete this line when you write your code!



print("********** Ch 6 Exercise 5 **********")

# Do your work for Exercise 5 here.

print("Ch 6 Exercise 5: Not implemented") # Delete this line when you write your code!
