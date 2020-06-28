###### Removing the odd index character from string
a=input('Enter a String : ')
b=''
for i in range(len(a)):
    if(i%2==0):
        b+=a[i]
print('Output : '+b)