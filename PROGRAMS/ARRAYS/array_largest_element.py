def largest(arr):
    print("array is :",arr)
    max=arr[0]
    n=len(arr)
    for i in range(1,n):
        print(arr[i])
        if arr[i]>max:
            max=arr[i]

    print("max value in an array is :",max)


arr=[1,2,3,4,5]
largest(arr)