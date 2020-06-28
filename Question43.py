############ Remove element of the tuple
user_input=tuple(input('Enter string of tuple separated by space : ').split())
print('Current Tuple : '+str(user_input))
user_input=list(user_input)
a=input('Which element do you want to remove : ')
user_input.remove(a)
print('Updated tuple : '+str(tuple(user_input)))