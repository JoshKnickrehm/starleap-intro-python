minutes = 400
hours = minutes // 60
remainder = minutes % 60

def time():
    print(hours, end="")
    print(" ", end="")
    print("hour ", end="")
    print(remainder, end="")
    print(" ", end="")
    print("minutes ")

time()

if hours >= 4:
    print("a long time")
elif hours <= 2:
    print("not that long")
else:
    print("kinda long")