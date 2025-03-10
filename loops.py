import random

number = random.randint(1,25)                   # Generate random number
number_of_guesses = 0                           # Instantiate guess counter

while number_of_guesses < 5:
    print('Guess a number between 1 and 25: ')  # Tell user to guess number
    guess = input()                             # Produce the user input field
    guess = int(guess)                          # Convert guess to integer
    number_of_guesses += 1                      # Increment guess count by 1

    if guess == number:                         # Break while loop if guess is correct
        break
    elif number_of_guesses == 5:                # Break while loop if guess limit reached
        break
    else:                                       # Tell user to try again
        print('Nope! Try again.')

# Message to display if correct
if guess == number:
    print('Correct! You guessed the number in ' + str(number_of_guesses) + ' tries!')
# Message to display after 5 unsuccessful guesses
else:
    print('You did not guess the number. The number was ' + str(number) + '.')




x = 0
while x<5 :
    print("x is not yet 5 x = "+ str(x))
    x = x + 1
    print('x ='+str(x))


    from time import sleep

### YOUR CODE HERE ###
n = 10

while n>=0:
    print(n)
    sleep(1)
    n = n-1
    
    if(n==5):
        print("Place your reservation soon! 5 minutes remaining.")
    elif(n==2):
        print("Place your reservation soon! 2 minutes remaining.")
    elif(n==0):
        print("User timed out.")

a = 0
for a in range(3):
    print(a)        