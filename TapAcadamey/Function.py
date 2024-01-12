lst = [10, 13, 18, 15, 20]

'''def fun(x):
    if x%2==0:
        return True
    else:
        return False
    
eve_lst = list(filter(fun,lst))
print(eve_lst)'''

even_list = list(filter(lambda x : x % 2 == 0,lst))
print(even_list)
    
    