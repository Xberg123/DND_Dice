import random

dice = input("Please select the dice you wish to roll: D4, D6, D8, D10, D12, D20?" )
roll = input("What are you rolling for? ")
session = True



if dice == "D4":
    result_D4 = random.randint(1,4)
    print("after rolling for ", roll, " you rolled a...", result_D4)
elif dice == "D6":
    result_D6 = random.randint(1, 6)
    print("after rolling for ", roll, " you rolled a...", result_D6)
elif dice == "D8":
    result_D8 = random.randint(1, 8)
    print("after rolling for ", roll, " you rolled a...", result_D8)
elif dice == "D10":
    result_D10 = random.randint(1, 10)
    print("after rolling for ", roll, " you rolled a...", result_D10)
elif dice == "D12":
    result_D12 = random.randint(1, 12)
    print("after rolling for ", roll, " you rolled a...", result_D12)
elif dice == "D20":
    result_D20 = random.randint(1, 20)
    print("after rolling for ", roll, " you rolled a...", result_D20)
else:
    print("Please choose from the dice provided or make sure to have capitalization")