#شبیه ساز خودپرداز

balance = 1000000

while True:

    print("\n----- ATM Menu -----")
    print("1. Mojoodi")
    print("2. Bardasht")
    print("3. Variz")
    print("4. Khoroj")

    choice = int(input("Entekhab kon: "))

    if choice == 1:
        print("Mojoodi shoma:", balance)

    elif choice == 2:

        amount = int(input("Mablagh bardasht: "))

        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Bardasht anjam shod")
            print("Mojoodi jadid:", balance)

        else:
            print("Mojoodi kafi nist ya mablagh eshtebah ast")

    elif choice == 3:

        amount = int(input("Mablagh variz: "))

        if amount > 0:
            balance = balance + amount
            print("Variz anjam shod")
            print("Mojoodi jadid:", balance)

        else:
            print("Mablagh eshtebah ast")

    elif choice == 4:
        print("Khoda hafez!")
        break

    else:
        print("Entekhab eshtebah ast")