# This is my own personal Python exampls to help me to remember how to write the codes.


# Python comes with built in functions that you can use to build and test applications. [print(), len(), etc]
# To write a function requiers the use of the key word 'def' followed by the name of the function with parentheses()and a colon:
# Functions work with indentation so it must be properly indented otherwise it will not work properly.
# You can use all the tools, variables lists, tuple, conditional statements, user inputs etc. to create to create your function.
def simple_function(): # The topline defines the function.
    print('simple function test') # The statement underneath defines what the function will do. This section can be as long as you need it to be.
simple_function() # This is how the function is called when you wish to execute the function.

# Functions are designed to do something and return something. You can specify what the return value should be with the keyword 'return'.
def language():
    return  "I speak English" # The return keyword defines what the function will do when the the function is aclled.
print(language()) # Prints the return statement "I speak English"
# Python adds return None to the end of any function definition with no return statement. If you use return without a value, None is returned.

# Functions can take Parameters, def example(test): You can have as many Parameters as you need. 
# The Parameter means for the function to run it has to be given an argument. each Parameter given requires an argument.
def fave_food(food): # This function has one Parameter. 'food' is the variable name for the parameter. 
    print('My favourite food is ' + food) # 'food' is used as part of the print statement. 
# Whatever value is passed to the function will be stored in the food variable.
# The value passed to the function is called an Argument. This is represented by the 'food' in the print statement.
fave_food('kenke and fish') # This will print 'My favourite food is kenke and fish'.

# Each Parameter give to a function can have a default value. If a default value is given the function will not need an argument to run.
# When the function is called the default value given will be used if no arguments are provided.
def greetings(name='John Doe'):
    print(name)
greetings() # This will print "John Doe"
# When using default values with multiple parameters, the parameter with a default valu must always be at the end other errors will occur.
def greet(name, dob=''): # All parameters with Default values must come after Parameters without default values.
    pass # This keyword is used for an empty function not ready to be used.
# parameters can lists tuples or dictionaries. They all require a name per parameter. 
# When the function is called you can use a variable with a list or pass in the a list like this example([1, 2, 3])
def country(countries): # this function takes in a list and creates a new list
    visits = [] # Variable with an empty list.
    print('How many countries have you visited?')
    for i in countries: # loop through the countries
        visits.append(i) # Add each country to the visits variable.
        print(visits)
country(['Denmark', 'France', 'USA']) # This prints ['Denmark', 'France', 'USA']

# You can use *args as the parameter and this allows you to enter multiple arguments. The values will be stored in a Tuple name args which is immutable.
# Another option is **kwargs, this takes keyword arguments store them in a dictionary named kwargs. Two loop through kwargs use kwargs.
# The star is what creates the the conditions args is just a name so it can be *example if you want. This is the same for kwargs. Use two **example.
# Both args and kwargs can be used with other parameters. example(name, *args, **kwargs)
def food(*args):
    print(args)
food('chicken', 'avacado', 'carrots', 'gravey', 'potatoes') # The function outputs: ('chicken', 'avacado', 'carrots', 'gravey', 'potatoes')

def dinner(**kwargs):
    print(kwargs)
dinner(meat='chicken', veg='carrots', main='potatoes', side='avacado', gravey='gravey')
# The function outputs: {'meat': 'chicken', 'veg': 'carrots', 'main': 'potatoes', 'side': 'avacado', 'gravey': 'gravey'}

# Python supports the concept of anonymous functions, also called lambda function. 
# Anonymous functions doesn't need a name and lambda function are defined with the keyword lambda. A lambda can be saved to a variable.
# Lambdas are useful for functions that takes a function as parameter. They only allow a single expression and has return built in automatically. 
lam_test = lambda num: num * num
print(lam_test(20)) # Prints 400

names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
names.sort(key=lambda s: s.lower())
print(names) # This prints ['Adams', 'diMeola', 'Ma', 'Zandusky']

# To handle errors that may occur in a function. Use the keyword 'try and except' errors like user inputs or wrong arguments passed into the function etc.
def num(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(num(0)) # Prints Error: Invalid argument.
print(num(2)) # Prints 21.0