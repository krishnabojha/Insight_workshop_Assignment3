####### sorting list of 2D tuple

a = list(tuple(map(int,input().split())) for r in range(int(input('enter no of list element : ')))) 
print("Input : "+str(a)) 
a=sorted(a,key= lambda i:i[-1])
print('Output : '+str(a))