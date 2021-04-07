from sys import getsizeof

print('''
2. Given the following code, please rewrite generate_list and use_list functions using atleast one
different iterator
''')

def generate_list():
    res = []
    for i in range(5):
        res.append(i)
    return res

def use_list(input):
    for i in input:
        print(i)

print('''
If I understand the question correctly, we need to use a different iterator and not loop as we usually
do in an iterable object...
''')  

print("Ok, so let's use a generator and make it an iter object! They're better when it comes to memory efficiency.")
def generate_list_gen():
    return (i for i in range(5)) # returns a generator, which is much more memory-efficient! 

def use_list_gen(input):
    my_iterator = iter(input)
    while True:
        try:
            print(next(my_iterator))
        except StopIteration:
            # Iterator throws an exception if there is the next pointer points to nothing.
            break

# This input...
x = generate_list()
use_list(x)

print("Size of the generated list (no generator): {}".format(getsizeof(x)))
# Should be the same than this one than this one.

x = generate_list_gen()
use_list_gen(x)

print("Size of the generator: {}".format(getsizeof(x)))

print("This memory efficience is more visible with larger lists.")