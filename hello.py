#Simple Print Function
print("Hello World")

#Increament

i = 3
i += 1
print (i)

#QuickSort
print('**** Quick Sort Algorithm ****\n')
def quicksort (arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))
print('\n')

#String Manipulation
print('**** String Manipulation ****\n')
s = 'hello'
d = 'PAAG'
print(s.capitalize()) # Capitalize a string; prints "Hello"
print(s.upper())      # Convert a string to uppercase; prints "HELLO"
print(d.lower())      # Convert a string to lowercase; prints "paag"
print(s.center(15))   # Center a string, padding with spaces; prints " hello "
print(s.rjust(25))    # Right-justify a string, padding with spaces; prints "  hello"
print(s.replace('l', '(ell)' ))  # Replace all instances of one substring with another;
                                 # prints "he(ell)(ell)o"
print('     hussnain'.strip()) #Removes white spaces
print('\n')

print('**** LOOPS ****\n')
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))

print('\n')

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)   # Prints [0, 1, 4, 9, 16]

print("\n")                               
#Slicing / Dicing
print("*** Lists & Slicing ***")
areas  = [0, 1, 2, 3, 4, 5]

upstairs = areas[0:3]
print(upstairs)
downstairs = areas[3:]
print(downstairs)

print("\n")
x = [10, 20, 30, 40, 50]
y = list(x)

print("List X is copied in y = ", y)

Li = [[1,2,30]]

