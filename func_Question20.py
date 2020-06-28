############ calcuate the intersection of two list
arr1=input('enter element of 1st array separated by space : ').split()
arr2=input('enter element of 2st array separated by space : ').split()
x=lambda a: a in arr1
intersection=list(filter(x,arr2))
print('The intersection of two given array is : {}'.format(intersection))