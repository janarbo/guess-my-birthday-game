from random import randint

name = input("Hi!What's your name ?")

guess_number = 0

for guess_number in range(5):
    guess_number += 1

    month_number = randint(0, 13)
    year_number = randint(1923, 2005)

    print (guess_number,":", name, "were you born in", month_number, "/", year_number, "?")

    response = input("yes or no? ")
    if response == "yes":
        print("I knew it!")
        exit()
    else:
        print("Drat! Lemme try again!")

print("I have other things to do, good bye!")
