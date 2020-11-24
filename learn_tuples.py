# This is my own personal Python exampls to help me to remember how to write the codes.
import random

# A Tuple is another form of a list, it has alot of the same features as lists howeve, tuple is immutabel. 
# The items in a tuple can not be changed, removed and no additional items can be added to a tuple.
# Tuple is written with (), the items are also separated with a comma. 
# A Tuple with only one item must have a comma at the end. example = ('chips',) - 
# this is so Python will not think its just an item in parentheses.

my_dinner_recipe = ('potatoes', 'whole chicken', 'carrots', 'brockley', 'stuffing')
food_shopping = ('orange juice', 'oats', 'bananas', 'yogurt', 'maple syrup', 'blueberries')
nums = (12, 28, 2.4, -19, -1, 43, 44, 0, 5, 8, 33, 89, 22, 19)

# each item in a list has and index and each index can be referenced, accessed and changed.
my_dinner_recipe[1] # this will be 'whole chicken'.

all_my_recipes = [[my_dinner_recipe, 'lunch recipes', 'breakfast'], [10, 1, 6]] # Lists containing other lists.

all_my_recipes[0] # this will be [my_dinner_recipe, 'lunch recipes', 'breakfast']
all_my_recipes[1][2] # this will be 6.

# indexes can be accessed using negative numbers, -1 references the last item in a list, -2 goes to second to last and so on.
my_dinner_recipe[-1] # this will be stuffing

# Slices are used get several items from a list. example[1:4] will give the items from index 1 to 3. 
# The last digit is always ignored, slices evaluates to a new list value.         
my_dinner_recipe[1:4] # this will be ['whole chicken', 'carrots', 'brockley'].
my_dinner_recipe[2:-1] # this will be ['carrots', 'brockley'] 

# Slices can also be written like this example[:3] or example[1:]
my_dinner_recipe[:3] # this will be ['potatoes', 'whole chicken', 'carrots']
my_dinner_recipe[1:] # this will be ['whole chicken', 'carrots', 'brockley']

# The len() can be used to obtain the amount of tems in a list
len(my_dinner_recipe) # this will be 4, counting always starts at 0. 

# Manipulating list items with Methods: [index('example'), appen('example'), insert(1, 'example'), remove(), sort(), reverse()]. These Methods can only be used for list data type.
food_shopping.index('oats') # this will give the index number of oats. If a list has duplicate items index() will give the first item in that list.

# The in and not Operators can be used to check for values in a list. These evaluates to a Bolean value.
'yogurt' in my_dinner_recipe # Outputs False
'chicken' not in food_shopping # Outputs True

# List items can be assigned to multiple varibles. The number of items in the list and number of variables must be the same.
starch, poultry, orange_veg, green_veg, mixed_veg = my_dinner_recipe
print(starch) # Ouputs the value stored in starch

# You can use loops to loop through lists to get a value. The enumerate() function returns the index and the value of the item in a list.
for index, food in enumerate(my_dinner_recipe):
    print('Index ' + str(index) + ' ' + food)
# Output = Index 0 avacado
# Index 1 carrots
# Index 2 gravey
# Index 3 potatoes
# Index 4 whole chicken

# The random.choice() function will randomly select and item from a list.
random.choice(my_dinner_recipe) # Output anyone item from this list.

# Tuple has its own fuction tuple([2, 4, 5, 10]), this returns list as a tuple.
print(tuple([2, 4, 5, 10])) # Outputs (2, 4, 5, 10)