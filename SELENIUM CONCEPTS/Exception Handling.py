try:
    file=open("D:\\demo21.txt","r")
    # file = open("C:\\Users\\shashi\\Desktop\\abc.txt", "r")
    print(file.read())
    print("Have a nice day")

except FileNotFoundError as err:
    print(err)
finally:
    print("Final statements got printed finally")



try:
    num1=input("enetr a number ")
    num2 = input("enetr a number ")
    res = num1/num2
    print(res)
except TypeError as err:
    print("please provide only digits",err)
except ValueError as err:
    print("please enter only valid value",r)
except ZeroDivisionError as err:
    print("Please don't enter 0")
except Exception as err:
    print("Something went wrong")
finally:
    print("Finally Have a nice day")




