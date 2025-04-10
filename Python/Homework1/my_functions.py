#Jamie Barbara
def returnInteger(nums): #takes in list nums
    """
    returns the sum of a list of numbers. 
    It will return the sum as an int no matter 
    the type of number used in the list
    """
    return(int(sum(nums))) #returns integer sum of list nums

def introduction(name, age, major, fun_fact): #takes in strings and an int
    """
    returns a string that allows a person to introduce themselves through given variables
    """
    return ("Hi! My name is " + name + " and I am a " + str(age) + " year old " + major +
    " major. A fun fact about me is that " + fun_fact)  #prints an introductory statement with information given

print(returnInteger([1,2,3,4,5]))
print(returnInteger([10,10,10,10,10]))
print(returnInteger([5, 800.5, 17,6.8888945]))

print(introduction("Jamie Barbara", 21, "Accounting", "I love dogs!"))
print(introduction("Jane Doe", 21, "Poli Sci", "my favorite book is 'A Tale of Two Cities.'"))
print(introduction("Clifford Red", 25, "Mechanical Engineering", "I am a big red dog!"))
