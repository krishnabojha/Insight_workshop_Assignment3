##### removing character except first and last two character
a=input('Enter your String:')
if len(a)==2:
    print('Output : '+(a+a))
elif len(a)<2:
    print('Output : Empty String ')
else:
    print('Output:'+(a[:2]+a[len(a)-2:]))