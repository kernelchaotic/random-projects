import random

again = True

side_Count = input("How many sides does this die have? (Use integers.)\n")

while again:
    print(random.randint(1, int(side_Count)))
    another_roll = input("Want to roll again? (yes/no)")
    if another_roll.lower() == "yes":
        continue
    else:
        break
