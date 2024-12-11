print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bills = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bills+=5
        print("Child tickets are $5.")
    elif age <= 18:
        bills +=7
        print("Youth tickets are $7.")
    else:
        bills +=12
        print("Youth tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "y":
        bills+=3
    print(f"Your bills are {bills}$.")
else:
    print("Sorry you have to grow taller before you can ride.")
