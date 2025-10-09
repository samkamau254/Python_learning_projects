person_1 = {}

person_1['first_name'] = 'sam'
person_1['last_name'] = 'kamau'
person_1['age'] = 22
person_1['city'] = 'nairobi'

print(person_1)

favorite_numbers = {
    'sam': 28,
    'david': 100,
    'sarah': 55,
    'terry': 33,
    'spencer':35,
    }

number_1 = favorite_numbers['sam']
number_2 = favorite_numbers['david']
number_3 = favorite_numbers['sarah']
number_4 = favorite_numbers['terry']
number_5 = favorite_numbers['spencer']

print(f"The favorite number of Sam is {number_1}.")
print(f"The favorite number of David is {number_2}.")
print(f"The favorite number of Sarah is {number_3}.")
print(f"The favorite number of Terry is {number_4}.")
print(f"The favorite number of Spencer is {number_5}.")


glossary = {
    'print': 'used to output value',
    'tuple': 'used to hold items that cannot change',
    'lists': 'holds items that can be changed',
    }

print(f"Print:", glossary.get('print'))
print(f"\nTuple:", glossary.get('tuple'))
print(f"\nlists:", glossary.get('lists'))