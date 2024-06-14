import random
number = random.randint(1, 100)

print('Welcome to a game where you need to guess a number!')


def is_valid(s):
    return 0 < int(s) < 101 and int(s) % 10 < 10


def game():
    counter = 0
    while True:
        choice = int(input('Enter a number from 1 to 100: '))
        if is_valid(choice):
            if choice < number:
                print('Your number is smaller than the one I guessed, try again')
                counter += 1
            elif choice > number:
                print('Your number is greater than the one I guessed, try again')
                counter += 1
            elif choice == number:
                print('You guessed it! Good job!')
                print('Number of tries: ', counter)
                continue_game = input('Wanna continue? (Yes/No) ')
                if continue_game.lower() == 'yes':
                    print(game())
                if continue_game.lower() == 'no':
                    return 'Thanks for playing the game! See ya...'


        else:
            print('Please enter an existing number from 1 to 100?')


print(game())



