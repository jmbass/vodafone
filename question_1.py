print('''
1. Comment about the possible output values of the following code in Python and how you would
overcome the drawbacks when using different Python versions
''')

def use_result_somewhere(x):
    # do something with result
    print(result)

result = 7/5

print('''
As suggested by the question, the main issue with these lines of code is that different Python versions will interpret 
the '/' operator differently.

Python 2.x will interpret the '/' operator as an integer division if the inputs are integers.

Python 3.x will interpret the '/' operator as a floating point division.

That said, the result variable will be equal to {} for Python 2.x interpreters and will be {} for
Python 3.x interpreters.
'''.format(7//5, result))

print('''
I believe that the best way to handle the potentials exceptions that this difference might cause is to directly deploy
all the Python source code into a Python Virtual Environment. 

This test will be delivered as a project in a virtual environment and, to activate it, all that's needed is to run in the root folder of 
this project:

$ source .venv/bin/activate

And the virtual environment will be activated. This will isolate the execution environment not only to a specific Python version 
but also to ensure only the needed dependencies will be used.

If you are using Windows (non-UNIX), you might want to create a new Virtual Environment as they are not cross-OS compatible.

''')

print('''
Alternatively, if Python 2.x is needed because of legacy issues, the following import will allow you to use division as
it is standard on Python 3.x

from __future__ import division

''')





