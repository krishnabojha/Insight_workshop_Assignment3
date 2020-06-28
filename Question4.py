########## swape first two character of two string

a,b=input("Enter two string separated by space : ").split()
print("Output : '{}'" .format((b[:2]+a[2:])+' '+(a[:2]+b[2:])))