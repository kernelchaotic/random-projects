
print("Let's calculate how much time you have left alive, assuming you live until 90!")
age = input("What is your current age?")

days = 90 * 365 - int(age) * 365
weeks = 90 * 52 - int(age) * 52
months = 90 * 12 - int(age) * 12

print("You have " + str(days) + " days, " + str(weeks) + " weeks, and " + str(months) + " months left.")
print("Make them count.")