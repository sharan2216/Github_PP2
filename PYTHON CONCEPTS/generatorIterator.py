# #Generator
# def sqr(n):
#     for i in range(1,n+1):
#         yield i*i
#
# a=sqr(5)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# Iterator
def iterate():
    list_b=iter([1,2,3,4,5])
    # list_b = iter(['A', 'B', 'C', 'D'])
    print(next(list_b))
    print(next(list_b))
    print(next(list_b))
    print(next(list_b))
    print(next(list_b))

iterate()
