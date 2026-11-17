# JEEPNEY SIMULATOR (interactive)
route = ["Petron","Doctors","DLL"]
passengers = []
SEATS = 12
FARE = 13
total = 0 

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers),"of", SEATS,"seats")
    print("1 Sakay sa left \n2 Sakay sa right \n3 Priority seat \n4 Para po!")
    print("5 Baba sa pinto \n6 Baba sa harap")
    print("7 Seat check \n8 Balikan \n9 Total fare today")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == SEATS:
            print("Puno na po!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + FARE
            print(name, "boarded at the left.")

    elif choice == "2":
        if len(passengers) == SEATS:
            print("Puno na po!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + FARE
            print(name, "boarded at the right.")

    elif choice == "3":
        if len(passengers) == SEATS:
            print("Puno na po!")
        else:
            name = input("Name: ")
            passengers.insert(0, name)
            total = total + FARE
            print(name, "took the priority seat.")

    elif choice == "4":
        name = input("Who is getting off? ")
        if name in passengers:
            passengers.remove(name)
            print(name,"got off. Ingat po!")
        else:
            print(name, "is not on this jeep.")

    elif choice == "5":
        if len(passengers) == 0:
            print("The jeep is empty.")
        else:
            left = passengers.pop()
            print(left, "got off at the door.")

    elif choice == "6":
        if len(passengers) == 0:
            print("The jeep is empty.")
        else:
            front = passengers.pop(0)
            print(front, "got off at the front.")

    elif choice == "7":
        for i in range(len(passengers)):
            print("Seat", i + 1, passengers[i])

    elif choice == "8":
        route.reverse()
        print("Route:", route)

    elif choice == "9":
        print("Total fare today:", total)

    else:
        print("Invalid choice.")
        break