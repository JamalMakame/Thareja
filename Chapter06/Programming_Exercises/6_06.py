# Write a python program to add 'ing' at the end of a given string(length should be at least 3)
# If the given string already ends with 'ing then add 'ly instead
# If the string length of the given string is less than 3, leave it unchanged
print('----- A program to add ing and ly at the end of a string -----')
print()

string = input('Enter a string : ')
if string.endswith('ing'):
    string += 'ly'
elif len(string) >=3:
    string += 'ing'
print(string)