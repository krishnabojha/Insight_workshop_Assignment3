#########count the number of character
a=input('Enter your favourite String :')
a=list(a)
b=set(a)
dictionary=dict.fromkeys(b,0)
for i in b:
    for j in a:
        if(i==j):
            dictionary[i]=dictionary[i]+1
print('Your string have:')
print(dictionary)