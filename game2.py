from random import randrange
answer = randrange(100)
while True:
    player_guess = int(input("Guess a number: "))
    if (answer == player_guess):
        print("You win!")
        break
    if ( answer < player_guess ):
        print("It's smaller")
    else:
        print("It's bigger")