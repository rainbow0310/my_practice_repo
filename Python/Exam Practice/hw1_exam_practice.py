# Jamie Barbara
# Cite any sources you used to help with the homework including TAs and classmates

def string3(string):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """
    last_two = string[-2:]
    word = last_two + last_two + last_two
    #print (word)
    return word


def has123(nums):
    """
    Given an list of ints, return True if the sequence of numbers
    1, 2, 3 appears in the list somewhere. 1,2,3 must occur in order.
    """
    for i in range(len(nums)-2):                                            #iterate through string but make sure to subtract 1 less then amount you are looking for
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False
    

def hascode(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """
    count = 0
    for i in range(len(string)-3):
        if string[i] == 'c' and string[i+1] == 'o' and string[i+3] == 'e':              #make sure to use the word in parenthesis and not the method name
            count +=1
            #print (count)
    return count


def samecatdog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
   *** This can be simplfied using a Python string method ***
    """
    count1 = 0
    count2 = 0
    for i in range(len(string)-2):         #subtract 1 from the word you are trying to find, cat is 3 so len(string)-2
        if string[i:i+3] == "cat":      #on the exam just write it out incrementally, or remember that the end goes up to that amoount not including
            count1 +=1 
        elif string[i:i+3] == "dog":
            count2 +=1
    if count1 == count2:
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
    min_value = min(nums)
    max_value = max(nums)
    nums.remove(min_value)
    nums.remove(max_value)
    return sum(nums) // len(nums)

# YOUR NAME HERE
# Cite any sources you used to help with the homework including 
# TAs and classmates

def middle_three(str):
    """
    Given a string with an odd length greater than or equal to 3, 
    return the middle three characters.
    If the string length is less than 3 or even, return an empty string.
    
    Example:
    middle_three("abcdefg") returns "cde"
    middle_three("12345") returns "234"
    middle_three("hi") returns ""
    """
    if len(str) % 2 != 0 and len(str) > 3:
        i = len(str) // 2
        # print(str)
        # print(str[i])
        word = str[i-1] + str[i] + str[i+1]
        return word
    else:
        return ""
  

def filter_long_words(words, length):
    """
    Given a list of strings, return a new list containing only the words
    that have a length greater than the specified `length` parameter.
    Important: Use list comprehensions.

    Example:
    filter_long_words(["apple", "bat", "car", "dolphin"], 3) returns ["apple", "dolphin"]
    filter_long_words(["a", "ab", "abc", "abcd"], 2) returns ["abc", "abcd"]
    """
    new_lst = []
    for fruit in words:
        if len(fruit) > length:
            new_lst.append(fruit)
    #print(new_lst)
    return new_lst                      #remember to actually return something, also remember that return is after the for loop so on the same indent

  

def unique_characters(word):
    """
    Implement a function that accepts a string and returns a set of 
    unique characters in the string.
    Important: this must be done in at most two lines of code.
    
    Example:
    unique_characters("hello") returns {"h", "e", "l", "o"}
    unique_characters("abc") returns {"a", "b", "c"}
    """
    return set(word)
  

def merge_dictionaries(dict1, dict2):
    """
    Given two dictionaries, merge them into one dictionary. 
    If the same key exists in both dictionaries,
    the value from `dict2` should overwrite the value from `dict1`.

    Example:
    merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4}) returns {"a": 1, "b": 3, "c": 4}
    merge_dictionaries({}, {"x": 10}) returns {"x": 10}
    """
    new_dict = {}  # Initialize an empty dictionary

    # Add all key-value pairs from dict1
    for key in dict1:
        new_dict[key] = dict1[key]

    # Add all key-value pairs from dict2 (overwriting if key exists)
    for key in dict2:
        new_dict[key] = dict2[key]

    return new_dict

    # new_dictionary = {}
    # new_dictionary.update(dict1)    
    # new_dictionary.update(dict2)    
    # return new_dictionary

#     def merge_dictionaries(dict1, dict2, indices):
#     """
#     Merge dict1 with only specific key-value pairs from dict2.
#     The keys to be added are determined by their position (index) in dict2.

#     Example:
#     merge_dictionaries({"a": 1, "b": 2}, {"x": 10, "y": 20, "z": 30, "w": 40, "v": 50}, [2, 4])
#     returns {"a": 1, "b": 2, "z": 30, "v": 50}
#     """
#     new_dict = dict1.copy()  # Copy dict1 into new_dict

#     dict2_keys = list(dict2.keys())  # Convert keys of dict2 into a list

#     for index in indices:
#         if index < len(dict2_keys):  # Ensure index is within bounds
#             key = dict2_keys[index]  # Get key at specified index
#             new_dict[key] = dict2[key]  # Add key-value pair to new_dict

#     return new_dict

# # Example usage:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"x": 10, "y": 20, "z": 30, "w": 40, "v": 50}

# print(merge_dictionaries(dict1, dict2, [2, 4]))  
# # Output: {'a': 1, 'b': 2, 'z': 30, 'v': 50}

# def merge_dictionaries(dict1, dict2, keys_to_add):
#     """
#     Merge dict1 with only specific key-value pairs from dict2.
#     """
#     return {**dict1, **{key: dict2[key] for key in keys_to_add if key in dict2}}

# # Example usage:
# print(merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4, "d": 5}, ["b", "d"]))
# # Output: {'a': 1, 'b': 3, 'd': 5}

def character_frequency(strings):
    """
    The classic character frequency algorithm: given a list of strings, 
    return a dictionary with a key for each character and the value being 
    the number of times that character appears across all strings.

    Example:
    character_frequency(["abc", "ab", "c"]) returns {"a": 2, "b": 2, "c": 2}
    character_frequency(["hello", "world"]) returns {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
    """
    count=0
    new_dict={}
    for word in strings:
        for chars in word:
            if chars in new_dict:                 
                new_dict[chars] += 1       #can't do count here, must be the dictionary spot 
            else:
                new_dict[chars] = 1
    #print(new_dict)
    return new_dict

def group_by_length(strings):
    """
    Write a function that takes a list of strings and groups them by their 
    lengths. Return a dictionary where keys are the lengths and values 
    are lists of words with that length.

    Example:
    group_by_length(["a", "bb", "ccc", "dd", "eee"]) returns {1: ["a"], 2: ["bb", "dd"], 3: ["ccc", "eee"]}
    group_by_length(["apple", "bat", "cat", "dolphin"]) returns {5: ["apple"], 3: ["bat", "cat"], 7: ["dolphin"]}
    """
    new_dict = {}
    for i in strings:
        len_word = len(i)                   #this has to be len of i or whatever is in strings not the actual string
        if len_word in new_dict:
            new_dict[len_word].append(i)    #append whatever is in strings NOT strings
        else:   
            new_dict[len_word] = [i]
    #print (new_dict)
    return new_dict
  
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

#Test functions
assert middle_three("abcdefg") == "cde", 'middle_three("abcdefg") expected "cde"'
print("correct")
assert middle_three("12345") == "234", 'middle_three("12345") expected "234"'
print("correct")
assert middle_three("hi") == "", 'middle_three("hi") expected ""'
print("correct")

assert filter_long_words(["apple", "bat", "car", "dolphin"], 3) == ["apple", "dolphin"], 'Expected ["apple", "dolphin"]'
print("correct")
assert filter_long_words(["a", "ab", "abc", "abcd"], 2) == ["abc", "abcd"], 'Expected ["abc", "abcd"]'
print("correct")

assert unique_characters("hello") == {"h", "e", "l", "o"}, 'unique_characters("hello") expected {"h", "e", "l", "o"}'
print("correct")
assert unique_characters("abc") == {"a", "b", "c"}, 'unique_characters("abc") expected {"a", "b", "c"}'
print("correct")

assert merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}, 'Expected {"a": 1, "b": 3, "c": 4}'
print("correct")
assert merge_dictionaries({}, {"x": 10}) == {"x": 10}, 'Expected {"x": 10}'
print("correct")

assert character_frequency(["abc", "ab", "c"]) == {"a": 2, "b": 2, "c": 2}, 'Expected {"a": 2, "b": 2, "c": 2}'
print("correct")
assert character_frequency(["hello", "world"]) == {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}, 'Expected {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}'
print("correct")

assert group_by_length(["a", "bb", "ccc", "dd", "eee"]) == {1: ["a"], 2: ["bb", "dd"], 3: ["ccc", "eee"]}, 'Expected {1: ["a"], 2: ["bb", "dd"], 3: ["ccc", "eee"]}'
print("correct")
assert group_by_length(["apple", "bat", "cat", "dolphin"]) == {5: ["apple"], 3: ["bat", "cat"], 7: ["dolphin"]}, 'Expected {5: ["apple"], 3: ["bat", "cat"], 7: ["dolphin"]}'
print("correct")

# Problems found on https://codingbat.com/python
