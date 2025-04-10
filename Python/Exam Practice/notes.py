#list slicing
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
suffix = letters[-3:] # slice starts 3 from right end
prefix = letters[:-4] # slice ends 4 from right end
print(suffix)
print(prefix)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
fwd2 = letters[::2] # every 2nd letter
bwd2 = letters[::-2] # every 2nd letter in reverse
print(fwd2)
print(bwd2)

# extend adds a list to the end
letters.extend(['f', 'h',
'i'])

# insert adds an item at a specific index
letters.insert(1, 'b')
letters.insert(6, 'g')

supplies = ['book', 'pen', 'stapler', 'mug', 'tape']
print(supplies)
# remove deletes a specific item by its value
supplies.remove('stapler')
print(supplies)

# pop deletes an item at a specific index
supplies.pop(1)
print(supplies)
# pop deletes the item at the list end
supplies.pop()
print(supplies)

# clear deletes all the items
supplies.clear()

names = ['Joe', 'Mary', 'Jane', 'Joe', 'Steve', 'Joe']
# Find and count using index and count
print('Mary is at index:', names.index('Mary'))
print('Joes in the list:', names.count('Joe'))
# Mary is at index: 1
# Joes in the list: 3

names = ['Tim', 'Mary', 'Jane', 'Joe', 'Steve', 'Eve']
print(names)
# reverse will reverse the order of the list
names.reverse()
print(names)
# sort puts items in their natural (alphabetical) order
names.sort()
print(names)
# ['Tim', 'Mary', 'Jane', 'Joe', 'Steve', 'Eve']
# reverse: ['Eve', 'Steve', 'Joe', 'Jane', 'Mary', 'Tim']
# ['Eve', 'Jane', 'Joe', 'Mary', 'Steve', 'Tim']

names = ['Jack', 'Mary', 'Jim', 'Bob', 'Eve', 'Hank']
copy1 = names.copy()
copy2 = list(names)
copy3 = names[:]
print(names)
print(copy1)
print(copy2)
print(copy3)
# ['Jack', 'Mary', 'Jim', 'Bob', 'Eve', 'Hank']
# ['Jack', 'Mary', 'Jim', 'Bob', 'Eve', 'Hank']
# ['Jack', 'Mary', 'Jim', 'Bob', 'Eve', 'Hank']
# ['Jack', 'Mary', 'Jim', 'Bob', 'Eve', 'Hank']

values = [34, 27, 95, 18, 36, 21, 64, 50, 77]
even_values = [x for x in values if x % 2 == 0]
print(even_values)
#[34, 18, 36, 64, 50]

#2d list 
table = [[0] * 12 for i in range(10)]
print(table)

# Print the list
for row in range(len(table)):
    for col in range(len(table[row])):
        print(table[row][col], end=' ') 
        print()

 #access tuples using a for loop

 #input function, always returns a string
name = input('Enter your name: ')
print('Hi,', name)
age = int(input('What is your age? '))

#Multiple arguments print on the same line with a single space between:
answer = 42
print("The answer is", answer)
#The answer is 42
print('May', 'the', 'Force', 'be', 'with', 'you')
#May the Force be with you

#open a file
with open('movies.txt') as file:
 text = file.read()
print(text)
#The read method without arguments returns the entire text of the file as a string.


with open('top_ten_movies.txt', 'r') as file:
 for line in file:
    print(line, end='')
#Since the for loop is operating on the file object, it must be part of the with statement body. Each line of the file is stored in a list we can iterate

file_name =input("enter file name ")
with open(file_name) as file:
        count=1
        for line in file:
            print(str(count) + ". "+ line.strip())
            count +=1
