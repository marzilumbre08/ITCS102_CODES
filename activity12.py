import getpass

username = 'len'
password = 'noonegivesaf128'

u = input("Enter Username:")
p = getpass.getpass("Enter Password:")

if username == u and password == p:
	print("Congrats, you got in successfully!")
else:
	print("Try again next time LOL!")