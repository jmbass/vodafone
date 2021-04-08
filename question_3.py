print('''
3. An isogram is a word with no repeating letters. Please complete the function is_isogram, which
returns true ifthe word has no repeating letters. Could you do the same for a heterogram: a
sentence with no repeating letters?
''')

print("Sure! I'm afraid this is a rather known solution\n")

print("I'll assume that this is not caps sensitive. Also, I'll assume that an empty string is a valid isogram")

# set builds a collection of unique elements. If there's only unique elements in the word, then the length should be the same if it is an isogram.
def is_isogram(word : str):
    return len(set(word.lower())) == len(word) 

# same solution, let's just get rid of the spaces.
def is_heterogram(sentence : str):
    return len(set(sentence.replace(' ', ''))) == len(sentence.replace(' ', ''))

print("Let's write some test cases... If something wrong, an Assertion Exception should be thrown.\n")

assert is_isogram("Vodafone") == False # Repeats o's
assert is_isogram("murcielago") == True # My favorite isogram.
assert is_isogram("telcomM") == False # Should not be cap sensitive
assert is_isogram("IoT") == True

assert is_heterogram("Vodafone is the best!") == False # I mean, it's true but this is not a heterogram :)
assert is_heterogram("The big cat jumps") == True

print('If you can read me, nothing went wrong :)')