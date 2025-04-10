#name = input("Enter your name ")

try:
    num=int(input("Enter a number "))
    print("you entered", num)
    double = num*2
    print("doubled", double)
except:                                 #only enters exception if there is an error thrown
    print("number was not entered")

answer= 42
print('The answer is', answer)          #will print a space where the comma is

#print will make new lines for printing as default unlesss you do: , end = ' ') //you can put whatever you want for the end

with open("movies.txt") as file:        #must be saved in the root file (Platform Based Computing)
    for line in file:                   #iterate through file
        print(line.strip())             #strip takes out the new line that would be added if it was just print(line)

# with open("heights.txt") as file:
#     for line in file:
#             info = line.strip().split()  #strip removes the new line and then split it
#             #^info will be a list with the first word being one string and then the second word being the last name and third string being the number
#             #by default the split will split based on the space
#             info[2] = int(info[2]) #makes the 3rd index of the string into int
#             print(info)

"""
prompt user for file and then print it out with numbers
"""
#my try
file_name =input("enter file name ")
#count = 1
# with open(file_name) as file:
#     for line in file:
#          info = line.strip().split()
#          count += 1
#          print(count , ". " , info)

#solution
file_name =input("enter file name ")
with open(file_name) as file:
        count=1
        for line in file:
            print(str(count) + ". "+ line.strip())
            count +=1

