########## unpack the tuple 
a,b,c,d=input('Enter 4 numbers separated by space : ').split()
tuple_value=int(a),int(b),int(c),int(d)
print('Tuple of input : '+str(tuple_value))
a1,a2,a3,a4=tuple_value
### Unpacking the tuple
print("sum : "+str(a1+a2+a3+a4))
print('Unpacked output : ')
print(a1,a2,a3,a4)