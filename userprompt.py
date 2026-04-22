while True:
    name=input("Input Name: \n")
    with open ("GuestBook.txt", "a") as GuestBook:
        GuestBook.write (f"{name}\n")

