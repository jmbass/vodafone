print('''
4. Is there any issue with the following code that may alter the expected behaviour?
''')

def append_to_list(value, list_=[]):
    list_.append(value)
    return list_

l1 = append_to_list(3)
l2 = append_to_list(1, [2])
l3 = append_to_list(5)


print(l1)
print(l2)
print(l3)


print('''

It really depends on what do you mean by expected behaviour. Maybe you want to cache calls of this function when no list is passed
as an argument?

I reckon this is about functions in Python being objects that are evaluated on their definition and default arguments being persisted
when they're mutable. Default parameters are some sort of 'object attributes' and, because of this, their state may be updated 
in each call - as any other object.

In other words, I believe that the 'unexpected behaviour' you are expecting me to point out has to do with the fact that list_ is 
a mutable object defined as a default argument and, therefore, this list will not be empty the next time the function is called -
it'll have the previous entries appended on the previous calls.

Of course, this will not happen if the default argument is overwritten. Then, the list will be initialized as the one passed as
an argument of this function.

A proof of concept.

Let foo be a function such as:

def foo(a=[]):
    a.append(5)
    return a

Let's print the call to this function several times with:

print(foo())

''')

def foo(my_list=[]):
    my_list.append(5)
    return my_list

print(foo())
print(foo())
print(foo())
print(foo())
print(foo())

print('''
The list is growing on each call and I'm not passing a parameter.

But if now I do...

print(foo([2]))
''')

print(foo([2]))

print('Now the list is initialized and is not the default mutable one.')