# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Exercise: "Help the farmer" (using conditions and operators).

'''
The function shown below helps a farmer to decide what to do:
- during what season;
- during what time of the day;
- with the location of the cows;
- regarding mowing the grass
- with the slurry tank
- with a combination of all or several of the above situations
'''

print('\n')

def farm_action(
        weather, # (rainy, sunny, windy, neutral)
        time_of_day, # (day, night)
        cow_milking_status, # (Need milking = True, Don't need milking = False)
        location_of_the_cows, # (pasture, cowshed)
        season, # (winter, spring, summer, fall)
        slurry_tank, # (Full = True, Not full = False)
        grass_status) -> str: # (Long = True, Short = False)
    
    # Take cows to cowshed
    if location_of_the_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy'):
         action = 'Take cows to the cowshed.\n'

    # Milk cows      
    elif location_of_the_cows == 'cowshed' and cow_milking_status == True:
         action = 'Milk the cows.\n'

    elif location_of_the_cows == 'pasture' and cow_milking_status == True:
         action = 'Take cows to the cowshed.\n' + 'Milk the cows.\n' + 'Take cows back to the pasture.\n'

    # Fertilize pasture
    elif slurry_tank == True and location_of_the_cows == 'cowshed' and weather != 'sunny' and weather != 'windy':
         action = 'Fertilize the pasture.\n'
    
    elif slurry_tank == True and location_of_the_cows == 'pasture' and weather != 'sunny' and weather != 'windy':
         action = 'Take cows to the cowshed.\n' + 'Fertilize the pasture.\n' + 'Take cows back to the pasture.\n'

    # Mow grass 
    elif grass_status == True and season == 'spring' and weather == 'sunny' and location_of_the_cows != 'pasture':
         action = 'Mow the grass.\n'

    elif grass_status == True and season == 'spring' and weather == 'sunny' and location_of_the_cows != 'cowshed':
         action = 'Take cows to the cowshed.\n' + 'Mow the grass.\n' + 'Take cows back to the pasture.\n'
    
    else:
         action = 'Wait.\n'
    
    return action

print(farm_action('sunny','day', True, 'pasture', 'spring', False, True,))

'''
Below you can also select several scenario’s to check what the
output will be after uncommenting one of the lines / scenario’s and run this code.
'''

# print(farm_action('rainy', "night", False, 'pasture', 'spring', False, True))

# print(farm_action('rainy', "night", True, 'cowshed', 'spring', False, True))

# print(farm_action('neutral', 'night', False, 'cowshed', 'spring', True, True))

# print(farm_action('sunny', 'day', False, 'cowshed', 'spring', False, True))

# print(farm_action('sunny', 'day', False, 'cowshed', 'spring', False, False))

# print(farm_action('sunny','day', True, 'pasture', 'spring', False, True))

end = 'The output of the \'farm action\' function ends above this line.\n'

print(end)


