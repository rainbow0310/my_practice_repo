

#Write a for loop to print all numbers from 1 to 20 that are divisible by 3
for x in range(1,21):
    if x % 3 == 0:
        print (x, end = " ")

#Write a while loop that calculates the sum of all even numbers between 1 and 50 (inclusive). Print the result
count=1
sum_even=0
while count<=50:
    if count%2==0:
        sum_even+=count
    count+=1
print(sum_even)

#Use a for loop to print the numbers greater than 5
numbers = [5, 8, 2, 15, 10, 3, 7]
for i in numbers:
    if i > 5:
        print(i, end = " ")

"""
Write a function called swap that takes a list of elements and swaps the first and last elements. For
example, if the input to the function is [0,3,8,4,5] the swapped list would be [5,3,8,4,0]. You do not need
to return the list. Test the function like this:
"""

def swap(elements):
    first = lst[0]
    last = lst[len(lst)-1]
    lst[0] = last
    lst[len(lst)-1] = first

lst=[0,3,8,4,5]
swap(lst)
print(lst)

# Challenge: given lst, store a running sum of that list in lst2
lst=[1,2,3,4,5]
lst2=[]
lst2.append(lst[0])
for i in range(1,len(lst)):
    lst2.append(lst2[i-1]+lst[i])
print(lst2, end = "*")