# if and elif conditional statement

name = input("Input your name ---> ")
age = int(input("Input your age ---> "))

print("Hi,", name,"that age is considered as ")
if age >= 1 and age <= 5:
	print("Infant")
elif age >= 6 and age <= 12:
 	print("Kid")
elif age >= 13 and age <= 19:
 	print("Teenager")
elif age >= 20 and age <= 29:
	print("Early Adulthood")
elif age >= 30 and age <= 48:
	print("Adult")
elif age >= 49 and age <= 59:
	print("Advance Adult")
elif age >= 60 and age <= 150:
	print("Senior")
else: 
	print("Invalid")