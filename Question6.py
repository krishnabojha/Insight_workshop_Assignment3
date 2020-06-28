############# remove if not and poor comes one after another
count_not=0
count_poor=0
count=0
b=input('Enter your sentence : ') 
a=b.replace('!','')
a=a.replace('.','')
a=a.split(' ')
for j in a:
    if(j=='not'):
        count_not+=1
    if(j=='poor'):
        count_poor+=1
        break
if(count_not==count_poor):
    del count_not,count_poor
    not_index=a.index('not')
    itr=(a.index('poor')-not_index)+1
    while count<(itr):
        a.remove(a[not_index])
        count+=1
    a.append('good!')
    print("Output : '{}'".format(' '.join(a)))
else:
    print(b)