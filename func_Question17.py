########### check the given string is start with the given character or not
user_string=input('Enter a string : ')
character='k'
x=lambda x: True if x.startswith(character) else False
print('Output : {}'.format(x(user_string)))