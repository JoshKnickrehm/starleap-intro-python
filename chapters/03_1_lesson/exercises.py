
##### Template for Chapter 3.14, Exercises 1 - 3 ######


print("********** Ch 3 Exercise 1 **********")
def right_justify(input):
    length = len(input)
    print("length = ", length)
    target = 70
    spaces = target - length
    space_string = ' '*spaces
    print(space_string + input)
    
right_justify('monty')







print("********** Ch 3 Exercise 2 **********")


def do_thrice(f):
    f()
    f()
    f()
def print_spam():
    print('spam')


do_thrice(print_spam)

def hi():
    print('hi')

do_thrice(hi)


print("********** Ch 3 Exercise 3 **********")

def top_grid():
    print('+ - - - + - - - +')

def mid_grid():
    print('|       |       |')


def make_squares():
    top_grid()
    do_thrice(mid_grid)
    top_grid()

def make_grid():
    make_squares()
    do_thrice(mid_grid)    
    top_grid()

make_grid()

def end_corner():
    print('+')

def corner():
    print('+ ', end='')    

def middle():
    print('- ', end='')

def edge():
    print('|       ', end='')

def draw_grid():
    corner()
    do_thrice(middle)
    corner()
    do_thrice(middle)
    end_corner()
    do_thrice(edge)
    do_thrice(edge)
    do_thrice(edge)
    corner()
    do_thrice(middle)
    corner()
    do_thrice(middle)
    end_corner()
    

draw_grid()
