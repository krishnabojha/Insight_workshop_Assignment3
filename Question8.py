############## remove a character of given index
a=input('Enter a String : ')
if(len(a)!=0):
    b=int(input('Which index character you want to remove : '))
    a=list(a)
    a.remove(a[b])
    print("Output  : "+''.join(a))
else:
    print('Warning!!!, you must enter String')