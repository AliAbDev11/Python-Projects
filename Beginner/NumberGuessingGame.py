import random

random_number = random.randint(0,10)
print('Welcome to Number Guessing game you should guess a number between 0 and 10')
number = None
attempts = 0
while number != random_number:
    number = int(input('You should write the correct number: '))
    attempts += 1
    if number > random_number:
        print('too high')
    elif number < random_number:
        print('too low')
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts!")