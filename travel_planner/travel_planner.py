import json


with open('tourist_places.json') as f:
    places = json.load(f)


with open('restaurants.json') as f:
    restaurants = json.load(f)


budget_levels = {
    'low': 2000,
    'medium': 5000,
    'high': 10000
}


city = input('Enter city: ')
budget = input('Budget level (low/medium/high): ')
food_type = input('Preferred food: ')

print('\nRecommended Places:')
for place in places.get(city, []):
    print('-', place)

print('\nRecommended Restaurants:')
for restaurant in restaurants.get(food_type, []):
    print('-', restaurant)

print('\nEstimated Budget:', budget_levels[budget])
