# fixed x
for x in range(5):
    for y in range(5):
        if x + y == 4 or x==y:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# w/ input
n = int(input("how big do u want the x to be? "))
for x in range(n):
    for y in range(n):
        if x + y == n-1 or x==y:
            print("*", end="")
        else:
            print(" ", end="")
    print()