###### calculate Fibonacci
from functools import reduce
num=int(input('Enter number : '))
fib = lambda n: reduce(lambda x, _: x+[sum(x[-2:])], range(n-2), [0, 1])
print('The Fibonacci numbers upto {} is : {}'.format(num,fib(num)))