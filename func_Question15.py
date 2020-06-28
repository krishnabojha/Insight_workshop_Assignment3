########## filter list 
user_list=[]
input_list=input('Enter number of list separated by space : ').split()
for i in input_list:
    user_list.append(int(i))
    
even_int=lambda x:x%2==0
odd_int=lambda x:x%2!=0
even_int=list(filter(even_int,user_list))
odd_int=list(filter(odd_int,user_list))
print('Original list : {}'.format(user_list))
print('List of even number : {}'.format(even_int))
print('List of odd number : {}'.format(odd_int))