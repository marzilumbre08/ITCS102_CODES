from getpass import getpass 

isLogin = False

while isLogin == False:
    username = input("Insert Username --> ")
    password = getpass("Insert Password --> ")

    if username == "User1" and password == "ohmaigul4y":
        print("Access granted.")
        isLogin = True

    else:
        print("Try again.")
        isLogin = False