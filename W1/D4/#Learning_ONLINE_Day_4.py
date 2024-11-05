#Learning_ONLINE_Day_4
#All you need to know about Functions
#Basic Functions, Parameters and Arguments

#parameters - used to define the function. (positional)
def say_hello(): #the brakcets hold parameters like 'name', or keep giving it parameters (as many as I want)
    print('helllooooo')

def say_hello(name, emoji): #We are able to use the variables inside the function and add an f'' to the print command. Then add the variable to the print command.
    print(f'helllooooo {name} {emoji}')

#Arguments - the actual valus we provide in a function and used to call the function. (positional)
say_hello('Mike',':-)')
say_hello('Sharon',':-)')
say_hello('Eliav',':-)')
say_hello('Boris',':-)')

#arguments can be used over and over.
#positional parameters and arguments matter because they are required to be in the proper position. You have to make sure the first parameter is 
#the first argument and the second parameter is the second argument. 

#Default Parameters and Keyword Arguments

#keyword arguments - allow us to not worry about the position. (some say its bad practice becuase its making the code harder to edit and more confusing)
say_hello(emoji=':-)',name='Mike')

#default parameters
def say_hello(name='Darth Vader', emoji=';-)'): 
    print(f'helllooooo {name} {emoji}')

say_hello()  #if you run default params without an argument it will print the arguments defined in the original function.

#Return keyword
def sum(num1, num2): #sum will add num1 and num2

#if you run 
sum(4,5) #nothing happens when you run it
print(sum(4,5)) #prints NONE when you run it

#Functions always have to return something
#so you need a function to have 'return' in it.
def sum(num1, num2):
    return num1+num2
print(sum(4,5)) #ooutput will be 9
#a function modifies something in our program or returns something.
#A function should do one thing really well and a function should return something.
#functions can be combinesd and run together.
total = sum(5,10)
print(sum(10,total))
#output is 25

#METHODS AND FUNCTIONS
#Built-in functions like:
list()
print()
max()
min()
input()

#and custom functions like:
def sum(num1, num2):
    return num1+num2
print(sum(4,5))

#METHODS US '.' NOTATION
'hello'.capitalize #autofill after putting in '.' after the string hellp, it provides a list of methods tha can be applied.
#methods have to be owned by something. In this case its the string 'hello'.

#Python Basics : Docstrings
def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)
test('!!!!!')
test() #the brackets will show a pop up that shares the info of the purpose of this function that is shown within the ''' line of code.

#many docstrings come standard in python, but we can also customize them
help(test)

#helps people to understand what you are coding.

