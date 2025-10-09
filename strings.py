name = "sam kamau"
print(name.title())
print(name.upper())
print(name.lower())

#using variables in strings

first_name = "Sam"
second_name = "Kamau"
full_name = f"\n{first_name.lower()} {second_name.lower()}"

print(full_name)

print(f"\n\t{first_name}")

favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)

nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix("https://")

print(nostarch_url)