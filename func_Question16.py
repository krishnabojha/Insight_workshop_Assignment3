############### calculate square and cube
user_list=[]
input_list=input('Enter number of list separated by space : ').split()
for i in input_list:
    user_list.append(int(i))
    
square=lambda x:x*x
cube=lambda x:x*x*x
square=list(map(square,user_list))
cube=list(map(cube,user_list))
print('Original list : {}'.format(user_list))
print('List of square number : {}'.format(square))
print('List of cube number :{}'.format(cube))