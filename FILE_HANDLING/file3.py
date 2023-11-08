# try:
#     file=open("D:\\demo21.txt","r")
#     print(file.read())
#     print("Have a nice day")
# except FileNotFoundError as err:
#     print("FileNotFounderror---error occured ")
#
# print("This is the last statement")

try:
    num1=int(input("enter 1st number"))
    num2=int(input("enter 2nd number"))
    res=num1/num2

except TypeError as err:
    print("type error occurred")
except ZeroDivisionError as err2:
    print("ZeroDivisionError")
except ValueError as err3:
    print("Value error occured ")
except Exception as err:
    print("something went wrong")
else:
    print("All went right...all is well!!")
finally:
    print("Have a nice day")


