name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
mob = str(input("Enter the month were you born in: "))

if mob == "January" or "january":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Capricorn")
elif mob == "February" or "february":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Aquarius")
elif mob == "March" or "march":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Pisces")
elif mob == "April" or "april":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Aries")
elif mob == "May" or "may":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Taurus")
elif mob == "June" or "june":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Gemini")
elif mob == "July" or "july":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Cancer")
elif mob == "August" or "august":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Leo")
elif mob == "September" or "september":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Virgo")
elif mob == "October" or "october":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Libra")
elif mob == "November" or "november":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Scorpio")
elif mob == "December" or "december":
	print("Because " + name + " is " + str(age) + " years old, he/she is a Sagittarius")
else:
	print("You are an alien from mars!")
