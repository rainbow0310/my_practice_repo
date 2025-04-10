# Jamie Barbara
# Cite any sources you used to help with the homework including TAs and classmates

def string3(string):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """
    last_two = string[-2:] #gets the last two characters of the string
    concatenated = last_two + last_two + last_two #adds the last two characters as one word three times
    return concatenated #returns the final word with the three two last characters


def has123(nums):
    """
    Given an list of ints, return True if the sequence of numbers
    1, 2, 3 appears in the list somewhere. 1,2,3 must occur in order.
    """
    for i in range(len(nums)-2): #iterates through nums until it reaches 2 before the end since we're looking for three numbers
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3: #checks if 1,2,3 is in the list in order by using index and starting at index i
            return True #if all 3 numbers are in the list retrun true
    return False # if loop goes through the whole list and does not find the sequence of numbers then returns false

def hascode(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """
    count = 0 
    for i in range(len(string)-3): #iterating through the string umtil it reaches 3 indices before since the substring will be 4 characters long
         if string[i]== "c" and string[i+1] == "o" and string[i+3] == "e": #checking for characters in order while skipping (i+2) or "d"
            count +=1 #add to count if this specific order of letters is in there
            #print(count) this was a check
    return count



def samecatdog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
   *** This can be simplfied using a Python string method ***
    """
    count_1 = 0 
    count_2 = 0
    for i in range(len(string)-2): #iterating through the string umtil it reaches 2 indices before since the substring will be 3 characters long
         if string[i:i+3]== "cat": #checking for "cat"
            count_1 +=1 #add to count if this specific order of letters is in there
         if string[i:i+3]== "dog": #checking for "dog"
            count_2 +=1 #add to count if this specific order of letters is in there
    if count_1 == count_2: #check if the number of cats is the same as dogs
        return True
    else:
        return False


def centered_avg(nums):
    """
    Return the "centered" average of a list of ints, which we'll say is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
    """
    max_value = max(nums) #gets the max value of nums
    min_value = min(nums) #gets the min value of nums
    nums.remove(max_value) #removes one of the max values
    nums.remove(min_value) #removes one of the min values
    average_nums = sum(nums)//len(nums) #gets the floor average through the sum and then dividing by how many numbers there are (the length)
    return average_nums #returns the floor average


# Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct")

assert has123([1, 1, 2, 3, 1]) is True, '[1, 1, 2, 3, 1] has 123'
print("correct")
assert has123([1, 1, 2, 4, 1, 3]) is False, '[1, 1, 2, 3, 1] does not have sequence 123'
print("correct")
assert has123([1, 1, 2, 1, 2, 3]) is True, '[1, 1, 2, 1, 2, 3] has 123'
print("correct")

assert hascode("aaacodebbb") == 1, 'aaacodebbb has code'
print("correct")
assert hascode("aaacodebbb") == 1, 'codexxcode has code'
print("correct")
assert hascode("cozexxcope") == 2, 'cozexxcope has code'
print("correct")

assert samecatdog("catdog") is True, 'catdog appear same number of times'
print("correct")
assert samecatdog("catcat") is False, 'catcat does not appear same number of times'
print("correct")
assert samecatdog("1cat1cadodog") is True, '1cat1cadodog appear the same number of times'
print("correct")

assert centered_avg([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("correct")
assert centered_avg([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("correct")
assert centered_avg([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("correct")


# Problems found on https://codingbat.com/python