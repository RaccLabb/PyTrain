i = 1
weeklySteps = 0
while i <= 7:
    weeklySteps += int(input(f"Anna päivän {i} askeleet: "))
    i += 1
print(f"Viikon aikana kertyi askeleita yhteensä {weeklySteps}.")