##### counting ocurrance of the word in sentence
a=input('Enter your favourite Sentence :')
a=a.split()
b=set(a)
dictionary=dict.fromkeys(b,0)
for i in b:
    for j in a:
        if(i==j):
            dictionary[i]=dictionary[i]+1
print('Your string have:')
print(dictionary)