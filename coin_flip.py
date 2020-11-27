import random

number_of_streaks = 0
results = []
tails = 0
heads = 0
for experimentNumber in range(20):
    coin_flip = random.randint(0, 1)
    if (coin_flip == 0):
        results.append('T')
        tails += 1  
    else:
        results.append('H')
        heads += 1
    if (results[:3] == 'H'):
        number_of_streaks += 1

    # for streak in results:
# for streak in results:
#     if ("H" ):
#         number_of_streaks += 1
print(results)
print(number_of_streaks)
