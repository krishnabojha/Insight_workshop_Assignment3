### Exchanging the character of first and last index
a=input("Enter a String : ")
a=list(a)
temp=a[0]
a[0]=a[len(a)-1]
a[len(a)-1]=temp
del temp
print('Output : '+''.join(a))