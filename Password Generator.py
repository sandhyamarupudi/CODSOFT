# importing the random module
import random

# a function that will generate a password on length (n) and return it.
def Passwordgenerator(n):
    # defining the list of choices of characters.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

    '''
    The random.sample() method returns a list, so we need to convert it into a string before returning it.
    '''

    chosenLetters = random.sample(characters, n)
    # finally converting the list into string
    passwordgen = "".join(chosenLetters)

    return passwordgen


if __name__ == "__main__":
    while True:
        usersChoice = input(
            "Please enter 'yes' if you want to generate a password else type 'no' to exit: ")
        if usersChoice == 'no':
            print('Thankyou for using password generator')
            break
        else:
            n = int(input("Enter the length of the password: "))
            password = Passwordgenerator(n)
            print("A randomly selected password is:", password)
            print()

