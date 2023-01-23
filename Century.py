name = input("What is your name? ")
age = int(input("What is your age? "))
#for easy updates. Pull from data?
year = 2023
Centennial = year - age + 100
print(name + ", you will be 100 years old in "+ str(Centennial))
if age >= 10 and age <= 18:
    print("You've got a long way to go!")
elif age >= 19 and age <= 25:
    print("Things are about to ramp up!")
elif age >= 26 and age <= 40:
    print("These are your most active years. Make the best of it!")
elif age >= 41 and age <= 60:
    print("Wo-oh, you're halfway there!")
elif age >= 61 and age <= 75:
    print("If you haven't, start enjoying your time my friend.")
elif age >= 76 and age <= 99:
    print("You're so close!")
elif age >= 100:
    print("why are you checking? You're already there.")

elif age <= 10:
    print("How are you reading this? Goo-goo ga ga, kiddo.")