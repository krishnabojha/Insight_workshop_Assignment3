########## Find the index of element 
user_tuple=tuple(input('Enter tuple element separated by space : ').split())
print('Your tuple : '+str(user_tuple))
a=input('Enter element to get index : ')
if a in user_tuple:
    print('Index of {} is {}'.format(a,user_tuple.index(a)))
else:
    print('{} is not in tuple.'.format(a))