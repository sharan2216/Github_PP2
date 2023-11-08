rev = 0
def palindrome_num(n):

    while n>0:
        rem=n%10
        n=n/10
        rev=(rev*10)+rem

    return rev
if(n==rev):
    print("Palindrome")
else:
    print("Not a palindrome")


n = input("enter a number :")
palindrome_num(n)