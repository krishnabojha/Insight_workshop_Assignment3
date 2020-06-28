########## generating dictionary of key as a number and square of that as a value

a={}
n=int(input('(total number of key) n : '))
for i in range(1,n+1):
    a[i]=i*i
print('Output : '+str(a))