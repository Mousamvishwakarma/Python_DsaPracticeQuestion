
import random

max_num = int(input("Enter your  my_number: "))
random_num = random.randint(1, max_num)

guess = input("Guess a number: ")

while True:
    if guess == "quit":
        print("User quit the game.")
        break
    elif int(guess) == random_num:
        print("You are right! Congrats Sir")
        break
    elif int(guess) < random_num:
        guess = input("Hint: Your guess is too small. Try again: ")
    else:
        guess = input("Hint: Your guess is too large. Try again: ")




# max_number = int(input( "enter your number  "))
# random_num = random.ranadint(1,max_number)
# guess = input(" guess you number")
# while True:
#     if guess == "quit":
#         print("you quit game")
#         brack

#     elif int(guess) == random_num:
#         print("guess a right number congs!")
#         brack

#     elif int(guess) < random_num:
#         guess = input(" you guess to small number: try again ")
#     else:
#         guess = input("your guess is too large number : try again")