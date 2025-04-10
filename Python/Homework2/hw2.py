# Jamie Barbara
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
    if len(str)% 2 != 0 and len(str) >= 3:              #if the length of the string is odd and greater than or equal to 3
        i = int(len(str) / 2)                           #sets the index equal to the middle character of the string
        middle_word = str[i-1] + str[i] + str[i+1]      #makes a new string with the 3 middle letters
    else:
        return ""
    return middle_word 

            
  

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
    for fruit in words:                                 #iterates through the strings in the list words
        if len(fruit) > length:                         #if the length of the string is greater than the given length
            new_lst.append(fruit)                       #add the word to new_lst
    return new_lst
  

def unique_characters(word):
    """
    Implement a function that accepts a string and returns a set of 
    unique characters in the string.
    Important: this must be done in at most two lines of code.
    
    Example:
    unique_characters("hello") returns {"h", "e", "l", "o"}
    unique_characters("abc") returns {"a", "b", "c"}
    """
    return set(word)                                    #turns string into a set which has no duplicates and seperates the characters
  

def merge_dictionaries(dict1, dict2):
    """
    Given two dictionaries, merge them into one dictionary. 
    If the same key exists in both dictionaries,
    the value from `dict2` should overwrite the value from `dict1`.

    Example:
    merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4}) returns {"a": 1, "b": 3, "c": 4}
    merge_dictionaries({}, {"x": 10}) returns {"x": 10}
    """
    new_dictionary = {}
    new_dictionary.update(dict1)    #source: https://www.geeksforgeeks.org/append-a-value-to-a-dictionary-python/
    new_dictionary.update(dict2)    #update function merges all the elements of one dictionary to another, since the second dictionary is written after, it replaces duplicate values from the first one
    return new_dictionary
  

def character_frequency(strings):
    """
    The classic character frequency algorithm: given a list of strings, 
    return a dictionary with a key for each character and the value being 
    the number of times that character appears across all strings.

    Example:
    character_frequency(["abc", "ab", "c"]) returns {"a": 2, "b": 2, "c": 2}
    character_frequency(["hello", "world"]) returns {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
    """
    new_dict = {}
    for word in strings:                #iterates through each string
        for char in word:               #iterates through each character
            if char in new_dict:        #if the character is in the dictionary already
                new_dict[char]+=1       #add to the count in the dictionary for the character char
            elif char not in new_dict:  #if the character is not in the dictionary
                new_dict[char] = 1      #for that character start the count at 1
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
    for word in strings:                        #iterates through each string
        len_word = len(word)                    #stores length of the word
        if len_word in new_dict:                #if the length of the word is already in the dictionary
            new_dict[len_word].append(word)     #add the word to the existing spot where the length already exists; professor Malone helped with this one
        else:
            new_dict[len_word] = [word]         #create a new pair with the word and its length
    return new_dict

# Test functions
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