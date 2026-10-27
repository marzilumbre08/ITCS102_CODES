# z = 1
# for x in range(5):
#    for y in range(x + 1):
#        print(z, end=" ")
#        z = z + 1
#    print()

size = int(input("Enter size ---> "))
z = 1
for x in range(size):
    for y in range(x + size):
        print(z, end=" ")
        z = z + 1
    print()