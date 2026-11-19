#رمز ساز امن + بازی تصادفی

import random
import string

while True:

    print("\n----- Menu -----")
    print("1. Sakhte Ramz")
    print("2. Bazi Hadse Adad")
    print("3. Khoroj")

    choice = int(input("Entekhab kon: "))

    if choice == 1:

        n = int(input("Tool ramz ra vared kon: "))

        chars = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(n):
            password += random.choice(chars)

        print("Ramz shoma:", password)

    elif choice == 2:

        number = random.randint(1, 100)

        for i in range(7):

            guess = int(input("Adad ra hads bezan: "))

            if guess == number:
                print("Afarin! Dorost hads zadi")
                break

            elif guess < number:
                print("Ye adad bozorgtar bezan")

            else:
                print("Ye adad koochaktar bezan")

        else:
            print("Forsat tamoom shod!")
            print("Adad sahih:", number)

    elif choice == 3:
        print("Khoda hafez!")
        break

    else:
        print("Entekhab eshtebah ast")