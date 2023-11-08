num=int(input("enter a number : "))

def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
if num<0:
    print(f"negative number cant be calculated")
elif num==0:
    print("factorial of 0 is 1")
else:
    result=fact(num)
    print(result)

fact(int(num))

# 2nd way:---

def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)

num=int(input("enter a number : "))
print(fact(int(num)))