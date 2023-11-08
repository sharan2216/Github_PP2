try:
    num1=int(input("enter a number 1 :"))
    num2=int(input("enter a number 2 :"))
    result = num1/num2
    print(result)

except TypeError as err1:
    print("Type error occured",err1)
except ZeroDivisionError as err2:
    print("error occured is",err2)
except ValueError as err3:
    print("VaueError occured",err3)
except Exception as err4:
    print("Something went wrong")
else:
    print("All went  right ...all is well")
finally:
    print("This is a Final statement Have a Nice Day")


