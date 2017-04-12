def print_suggestion(suggestion_dict):
    print(suggestion_dict['name'])
    print(suggestion_dict['category'])
    print(suggestion_dict['street'])
    print(suggestion_dict['city'])

DEFAULT_SUGGESTION = {
    'name': 'Mustang Donuts',
    'category': 'Doughnuts',
    'street': 'Hillcrest',
    'city': 'Dallas'
}

print('I suggest this restaurant:')
print_suggestion(DEFAULT_SUGGESTION)
