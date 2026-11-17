anime_type = ["isekai","fantasy","adventure","scifi","romance","action","horror"]
anime_title = []

while True:
    ans = input("Do you know any anime --> (yes/no) ")

    if ans.lower() == 'yes':
        print("What is its type -- ? select from the list ")
        for x in anime_type:
            print(x) # traversing a list

        a_type = input("Type --> ")

        title = input("What is the title of the anime --> ")
        anime_title.append(title)
        continue
    else:
        print("Thank you")
        print("So far, you have encoded the following: ")
        for x in anime_title:
            print(x) # traversing a list
        break