try:
    val = int(input("enter a number:"))
except ZeroDivisionError:
    print("zero division input")
except ValueError:
    print("invalid input")