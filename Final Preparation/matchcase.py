num=int(input("Enter number :"))
match num:
    case 0:
        print("zero..")
    case 1:
        print("One")
    case 2:
        print("two")
    case _:
        print("Negative")