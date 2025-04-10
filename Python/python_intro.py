print("hello world!")
# fast easy comment
'or use single quotes'
'''
use this to make a few lines
of comments.
'''

# Variables
x = 100
y = 5.5
x = 'hello'
x=[1,2,3]

x=100
y=10
result = x/y
print(result)
result = int(result)
print(result)
result = x//y
print(result)

min_val = min(1,10)
print(min_val)
raised = pow(2,4)
print(raised)

x = -1
y = 0

if x < 0:
    print("less than")
if x < 0 and y == 0:
    print("yes")
else:
    print("no")

if x < 0 or y == 0:
    print("yes")
else:
    print("no")

if x < 0:
    print("less")
elif x > 0:
    print("more")
else:
    print("equals")

counter = 0
while counter < 10:
    print(counter)
    counter += 1

for i in range(5):
    print(i)

list = [1,2,3,4,5]
for i in range(len(list)):
    print(list[i])

for val in list:
    print(val)

for i,val in enumerate(list):
    print(i,val)

nums = [10,20,30,40,50]
for i in range(len(nums)):
    print(i, nums[i])

for val in nums:
    print(val)

for i, val in enumerate(nums):
    print(i,val)

dogs = ["Boomer", "Rocky", "Daisy"]
for i in range(len(dogs)):
    print(i, dogs[i])

for val in dogs:
    print(val)

for i, val in enumerate(dogs):
    print(i,val)

nums = [1,2,3,4,5]
sum = 0
for val in nums:
    sum += val
print(sum)

def hello_world():
    print("hello world")

hello_world()

def hello(name):
    print("Hello " + name)

def hello_default(name="Bob"):
    print("Hello " + name)

hello("John")
hello_default()
hello_default("Alice")





