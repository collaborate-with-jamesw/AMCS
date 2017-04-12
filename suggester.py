from suggestion_loader import get_random_suggestion

def print_suggestion(suggestion_dict):
    print((
        '{name}, it is a {category} place '
        'on {street} in {city}.'
    ).format(
        name=suggestion_dict['name'],
        category=suggestion_dict['category'],
        street=suggestion_dict['street'],
        city=suggestion_dict['city']
    ))

print('I suggest this restaurant:')
suggestion = get_random_suggestion()
print_suggestion(suggestion)
