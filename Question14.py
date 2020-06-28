######### Displaying HTML tag 
a=input('Enter html Tag : ')
b=input('Enter html Word : ')
def add_tags(tag,word):
    return "<%s>%s</%s>" % (tag, word,tag)
print(add_tags(a,b))