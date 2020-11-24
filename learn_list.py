# This is my own personal Python exampls to help me to remember how to write the codes.

import random, copy

# Lists stored in variables are not actually stored in the variable, they are referenced in memmory. The references have ID's that python uses internally.
# So when a list is changed a new list is created in memmory using the same refernce ID.

# lists - itemised with a comma, can contain ['Strings', integers, other lists].
# Lists are held in square brackets and can consist of different data types example = ['turkey' 30, [9, 8, 7]]. 
my_dinner_recipe = ['potatoes', 'whole chicken', 'carrots', 'brockley', 'stuffing']
food_shopping = ['orange juice', 'oats', 'bananas', 'yogurt', 'maple syrup', 'blueberries']
nums = [12, 28, 2.4, -19, -1, 43, 44, 0, 5, 8, 33, 89, 22, 19]


# each item in a list has and index and each index can be referenced, accessed and changed.
my_dinner_recipe[1] # this will be 'whole chicken'
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

# Lists are mutable meaning the items in a list can be removed and changed, items can be added to the list.
# Lists can be concatenated and replicated using + and * operators.
# The assignemnt Operator [+, -, *, /, %] can be used to add inters to  list variables, 
# concatenate list variables to strings, replicate lists variables and concatenate list with another list.
example = ['a', 'b', 'c', 'd'] + [1, 3, 4, 8, 40]
print(example) # this will be ['a', 'b', 'c', 'd', 1, 3, 4, 8, 40]
examp = [1, 3, 4, 8, 40] * 3
print(examp) # this will be [1, 3, 4, 8, 40, 1, 3, 4, 8, 40, 1, 3, 4, 8, 40]
dinner_shop = my_dinner_recipe + food_shopping
print(dinner_shop) # ['potatoes', 'whole chicken', 'carrots', 'avacado', 'gravey', 'orange juice', 'oats', 'bananas', 'yogurt', 'maple syrup', 'blueberries']

# Replacing and Deleteing items in a list. 
my_dinner_recipe[3] = 'avacado' # this will replace brockley with avacado.
my_dinner_recipe[-1] = 'gravey' # this will replace stuffing with gravey.
del food_shopping[3] # this will delete 'yogurt' from the food_shopping list.

# Manipulating list items with Methods: [index('example'), appen('example'), insert(1, 'example'), remove(), sort(), reverse()]. These Methods can only be used for list data type.
food_shopping.index('oats') # this will give the index number of oats. If a list has duplicate items index() will give the first item in that list.
food_shopping.append('cinnamon') # this will add cinnamon to the end of the list.
# the insert() Method lets you add an item at any index, takes two arguments, the position and the value. 
food_shopping.insert(2, 'mango chunks') # this will add 'mango chunks' to the index position 2 in the list.
food_shopping.remove('bananas') # this will remove 'bananas' from the list. If the item has duplicates the first item will be removed.
# The sort() Method sorts out strings [a-z] and integers [0-10] in Ascending order. You can use sort(reverse=True) for Descending order.
nums.sort() # Outputs [-19, -1, 0, 2.4, 5, 8, 12, 19, 22, 28, 33, 43, 44, 89]
nums.sort(reverse=True) # Outputs [89, 44, 43, 33, 28, 22, 19, 12, 8, 5, 2.4, 0, -1, -19]
my_dinner_recipe.sort() # Outputs ['avacado', 'carrots', 'gravey', 'potatoes', 'whole chicken']
# sort() does not supprt lists with mixed data types. Uppercase letters are come before lower case letters. Use sort(key=str.lower) to have lowercase nefore upper case.
food_shopping.reverse() # this will reverse the order. ['cinnamon', 'blueberries', 'maple syrup', 'mango chunks', 'oats', 'orange juice']

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
# The random.shuffle function will reorder the list in a random order.
random.shuffle(my_dinner_recipe) # Output random order of the list.

# List has its own fuction list('example'), this returns example with each letter as string in a list format.
print(list('example')) # returns ['e', 'x', 'a', 'm', 'p', 'l', 'e']

# Lists stored in variables are not actually stored in the variable, they are referenced in memmory. The references have ID's that python uses internally.
# So when a list is changed a new list is created in memmory using the same refernce ID.
# If you wish to make an exact copy of a list instead of a reference then you can use the copy() and deepcopy() functions. 
# The deepcopy is used to copy lists that contain other lists.
print(id(food_shopping)) # Outputs 4473145152
new_fd_shopping = copy.copy(food_shopping)
print(new_fd_shopping) # Outputs ['cinnamon', 'blueberries', 'maple syrup', 'mango chunks', 'oats', 'orange juice']
print(id(new_fd_shopping)) # Outputs 4344831296 - which is different