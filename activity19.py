isStudent = True

while isStudent == True:
    x = bool(input("Are you a student? (True/False) --> "))

    if x == True:
        print("Continuing Loop")
        continue
    else:
        break