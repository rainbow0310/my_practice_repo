print("Hello World!")

# this is a single line comment

'''
this lets you write multiple lines of a comment 
'''
# line 1
# line 2
# line 3 control forward slash lets you highlight and comment out everything at once

#vairables
x = 10 #dont have to say data type or include semicolon
x="hello" #can switch data types 
x=[1,2,3]
print(x)

x=100
y=10
result=int(x/y)
result=int(result)
print(result) #will come out as a float unless int is added in front

x=105
result = x//y #x divided by y but takes the floor so rounds down and prints integer even if not converted, called floor division
print(result)

min_val=min(1,10,50)
print(min_val) #dont name a vaariable min because it confuses python
#when writing variable names make it all lowercase with _ in between
raised=pow(2,3) # 2 to the power of 3
print(raised)
raised=2**3 # this is also 2 to the power of 3
print(raised)

x=-1
y=0
if x<0 : #use colon and no parenthesis
    print("x is negative") # NEED the indentation since there is no holder to tell python what to do
elif x>0 : # this is else if
    print("x is positive")
else:
    print("x is 0")

#compud conditional statements
start = 10
end = 100

if x>=start and x<= end :
    print("x is within range")

if x>=start or x<=end: 
    print("x is not within range")
