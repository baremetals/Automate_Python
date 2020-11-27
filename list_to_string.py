# This function takes a list countries, then converts the list into one string with commas at the end of each country in the string. 
# For the last two countries the word 'and' is used instead of the comma. The function works for lists of any size. 

places_visited = ['Ghana', 'France', 'Sweden', 'Germany']
def country(countries):
    last_country_length = len(countries[-1]) + 2 # The 2 is added because of the extra comma and space that will be added later on during the loop. 
    places = '' 
    print('How many countries have you visited?')
    for i in countries:
        places += i + ', '
    string_length = len(places)
    the_difference = string_length - last_country_length
    the_last_country = places[the_difference:-2] # the -2 is used to remove the extra comma and space that was added during the loop.
    final_countries = places[:the_difference] + 'and ' + the_last_country
    print('I have visited ' + final_countries)            
country(places_visited)


