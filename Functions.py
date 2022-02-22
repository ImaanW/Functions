#Functions are objects
# we create these functions by defining them with def statements, followed by the argument list
#memebership is by indentation and all the lines assocaited with code are indented
#def make_list(val, times):
    #res = str(val) * times
   ##here are the functions and instructions created by the developer(made up names)
# passing two variables val and times

#arguments are namesd // Defaults may be assigned
#Return statement is optional- you dont have to have it
  #any object may be returned
  #defualt is the empty objects None

#Variables are local(Private) if assigned - unless the key word global is used- when coding we always go local and private
#function names should be lower case


#Function Parameters
#Specified within the parentheses of the function declaration
# 1st define the function - make function
def make_list():
    result = range(6)
    return result

#2nd call/ invoke the function by using its name
list_a = make_list()
print(type(list_a))
print(list_a)

   #example two
def make_list2(value, times):
    result = str(value) * times
    return result
#here again calling the function - you can keep on calling the sme function and give it diff inputs
list_b = make_list2('spam ', 4)
print(list_b)

#Parameters are passed by assignment(copy)
def print_list(value, times):
    print(str(value) * times)
#call a function that does NOT retun a vlaue
print_list('spam',5)

#since they are references, changes alter the callers variables
#we can pass in mutable datatypes such as lists,dictionaries
#def change_list(inlist, val, times):


#function that will take in 3 peoples names and say hello
#def say_hello(indout):
 #   for name in names
  #      print('hello')


#assigning default values to parameters
#you can Assign the default values
#you can pass parameters by...
#by position\
#by defualt
#or by name

#Enforcing named parameters (pratice from slide)
#using *, first will force a user to supply NAMED arguments


#UNAPCKING AND VARIADIC FUNCTIONS
def my_fu(a,b,c):
    print (a,b,c)

mytup = 23,56,78
my_fu(*mytup)
#unpacking passes a sequences elemes as a single parameter

#varaidic functions have a variable number of parameters
#they can be collected into a tuple with a *prefix
#Scoopup all the parameters after the fist one turn them into a tuple

#KEYWORD PARAMETER
#double astrik ** turns into a dictiornary/ key value pairs But will come out undordered


#returning  onjects from a function
#returning - heres an output- stops the function, passing the object back to the caller,

#use return followed by the function

#VARIABLES IN FUNCTIONS
#byy default, variables used in a function are local
#avoid global

#LAMBDA FUNCTION
#CREATED to enables us to write (anonoymous) short hand functions - efficient
# cannot contain functions or loops
#CAN contain conditionals
compare = lambda a,b: -1 if a < b else (+1 if a > b else 0)
x = 42
y = 3
print("a>b", compare(x,y))
#here a and b are the conditionals
#this function is comparing
#LAMDDA FUNCTION oftern used with map() - take in a colection and filter() built-ins

lucky_numbers = [1,7,8,13,21]
luck_numbers_mutated = list(map(lambda x: x + 1, lucky_numbers))
print(luck_numbers_mutated)