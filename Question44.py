##### slice the tuple
a=tuple(input("Enter a String : "))
print('First half slice : '+str(a[:int(len(a)/2)]))
print('Second half slice : '+str(a[int(len(a)/2):]))
print('tuple of whole string : '+str(a[::1]))