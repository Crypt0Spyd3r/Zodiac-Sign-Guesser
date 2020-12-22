
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
mob = str(input("Enter the month were you born in: "))

if mob == "January":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Capricorn")
elif mob == "February":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Aquarius")
elif mob == "March":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Pisces")
elif mob == "April":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Aries")
elif mob == "May":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Taurus")
elif mob == "June":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Gemini")
elif mob == "July":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Cancer")
elif mob == "August":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Leo")
elif mob == "September":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Virgo")
elif mob == "October":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Libra")
elif mob == "November":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Scorpio")
elif mob == "December":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Sagittarius")
else:
	print("You are an alien from mars!")

