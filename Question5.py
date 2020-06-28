############### adding ing and ly to string
a=input('Enter a String : ')
if len(a)>2:
    if a[(len(a)-3):]!='ing':
        a+='ing'
    else:
        a+='ly'
print('Output : '+a)