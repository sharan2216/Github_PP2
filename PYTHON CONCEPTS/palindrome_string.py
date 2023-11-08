def palin_str(str):
    temp=str[::-1]
    if str.__eq__(temp):
        print("palindrome")
    else:
        print("not a palindrome")


str=input("enter a string: ")
palin_str(str)