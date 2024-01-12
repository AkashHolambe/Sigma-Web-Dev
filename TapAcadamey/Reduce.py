from functools import reduce
lst =[1, 2, 3, 4, 5]

'''
def fun (x,y):
    return x+y
res = reduce(fun,lst)
print(res)'''

res= reduce(lambda x,y : x+y,lst)
print(res)
