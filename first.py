print("siya_singh")

import random

computer_number = random.randint(1,5)

for attemt in range(1,4):

    user_guess = int(input("guess number(between 1-5=>)"))

    if user_guess == computer_number:

        print("congrats")

        break

    else:

        print("try again")

else:

    print("attempts finish try next time")