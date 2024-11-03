# #EX1
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# # If it’s more than 10 characters, print a message which states “string too long”.
# # If it’s 10 characters, print a message which states “perfect string” and continue the exercise.
string = (input("Please give me a string of exactly 10 characters:"))
if len(string) < 10:
    print ("string not long enough")
elif len(string) > 10:
    print ("string too long")
elif len(string)== 10:
    print ("perfect string")

# #EX2
# # Then, print the first and last characters of the given text.
# # The user enters "HelloWorld"
# # Then you have to print 
# # H
# # d
greeting = 'HelloWorld'
print (greeting[0])
print (greeting[-1])

# #EX3
# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "HelloWorld"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# HelloWorld
x = ""
h = 'HelloWorld'
for char in h:
    x += char
    print(x)