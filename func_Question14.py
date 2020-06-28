############ sort list of dictionary
dictionary=[{'country':'Nepal', 'capital':'kathmandu'},{'country':'bhutan', 'capital':'thimpu'},{'country':'maldeves', 'capital':'male'}]
print("Original list of dictionaries : \n{}".format(dictionary))
dictionary.sort( key = lambda x: x['capital'])
print("\nSorting the List of dictionaries : \n{}".format(dictionary))
