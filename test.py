from collections import OrderedDict

t ={'autor': 'Albert Einstein'}, {'autor': 'J.K. Rowling'}, {'autor': 'Albert Einstein'}, {'autor': 'Jane Austen'}, {'autor': 'Marilyn Monroe'}, {'autor': 'Albert Einstein'}, {'autor': 'André Gide'}, {'autor': 'Thomas A. Edison'}, {'autor': 'Eleanor Roosevelt'}, {'autor': 'Steve Martin'}

print(t)
print(type(t))

x =  list(OrderedDict.fromkeys(t))

print(x)
