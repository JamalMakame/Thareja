# Write a program using a function to calculate x to the power of y,
# where y can be either negative or positive.

print('--- A Program to Power of an integer ---')
print()

def power(x,y):
    ''' A function that returns the power of an integer'''
    return pow(x,y)

def main():
    ''' A function that take the radius then returns the surface area of a sphere.'''
    x= int(input('Enter the base value: '))
    y= int(input('Enter the Power Value: '))

    print()

    print(f'The answer: {power(x,y)}')


if __name__ == '__main__':
    main()

