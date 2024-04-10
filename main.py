"""
PowerOfTen
"""


def power_of_ten():
    number = int(input("Enter a max 3 digit number:"))
    if number < 0:
        print("number cannot be negative")
    elif number < 10:
        print(f"{number} = {number} * 1")
    elif number < 100:
        print(f"{number} = {number // 10} * 10 + {number % 10} * 1")
    elif number < 999:
        print(f"{number} = {number // 100} * 100 + {number // 10 % 10} * 10 + {number % 10} * 1")
    else:
        print("number has more than 3 digits")


"""
Cash Box
"""


def cashbox():
    change = -1

    while change < 0:
        sum = int(input("To pay:"))
        if sum < 0:
            print("Negative payment is invalid.")
            continue
        received = int(input("Received:"))

        if received < 0:
            print("Negative received amount is invalid.")
            continue

        change = received - sum
        if change >= 0:
            print("Your change is: " + str(change))
        else:
            print("You did not pay enough.")


if __name__ == '__main__':
    print("Run functions")
    cashbox()
    power_of_ten()
