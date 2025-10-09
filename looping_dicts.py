user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last':  'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in favorite_languages:
    print(name)
    
friends = ['phil', 'sarah']
for name in favorite_languages:
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, i see you love {language}!")
        
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")      