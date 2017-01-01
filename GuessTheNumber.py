import random

won = False
wtp = True
while wtp:
    value = random.randint(1, 20)
    print("Hi ! I m thinking of a number, can you guess it?")
    for tri in range(3):
        guess = int(input("Enter a no: "))
        if guess == value:
            won = True
            print("Congrats! You won.")
            break
        elif tri < 2:
            print("Sorry! try again")
            print(3 - tri - 1, "tries left")
        if won == False and tri == 2:
            print("Sorry ! you lost")
            print("Number was:", value)
            choice = str(input("would you like to play again y/n "))
            if choice == "n":
                print("Good bye")
                wtp = False
