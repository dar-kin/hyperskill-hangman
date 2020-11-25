

income = int(input())
percent = 0
calculated_tax = 0
if income <= 15_527:
    pass
elif income <= 42_707:
    percent = 15
    calculated_tax = income * 0.15
elif income <= 132_406:
    percent = 25
    calculated_tax = income * 0.25
else:
    percent = 28
    calculated_tax = income * 0.28
print(f"The tax for {income} is {percent}%. "
      f"That is {round(calculated_tax)} dollars!")
