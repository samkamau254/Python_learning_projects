#If you could invite anyone, living or deceased, to dinner,
#who would you invite? Make a list that includes at least three people you’d
#like to invite to dinner. Then use your list to print a message to each person,
#inviting them to dinner.

Guests = ['sam', 'craig', 'david']
message = (f'''
Hello {Guests[0].title()}, i would like to invite you for a dinner party.\n
Hello {Guests[1].title()}, i would like to invite you for a dinner party.\n
Hello {Guests[2].title()}, i would like to invite you for a dinner party.'''
)
print(message)

print("sam can't make it to the dinner party.")

#3-5.Changing Guest List
Guests[0] = 'peter'
print(Guests)

message = (f'''
Hello {Guests[0].title()}, i would like to invite you for a dinner party.\n
Hello {Guests[1].title()}, i would like to invite you for a dinner party.\n
Hello {Guests[2].title()}, i would like to invite you for a dinner party.'''
)
print(message)

print(f''' Hello {Guests[0].title(), Guests[1].title(), Guests[2].title()} we would be expecting more guests and i have found a bigger table''')

#3-6. More Guests

Guests.insert(0, 'faith')
Guests.insert(1, 'loki')
Guests.append('alex')

message = (f'''
Hello {Guests[0].title()}, i would like to invite you for a dinner party.\n
Hello {Guests[1].title()}, i would like to invite you for a dinner party.\n
Hello {Guests[2].title()}, i would like to invite you for a dinner party.\n
Hello {Guests[3].title()}, i would like to invite you for a dinner party.\n
Hello {Guests[4].title()}, i would like to invite you for a dinner party.'''
)
print(message)

#3-7. Shrinking Guest List
print(Guests)

popped_guest_0 = Guests.pop(0)
print(f"Hello {popped_guest_0}, the dinner table won't arrive in time for the dinner and i have only space for two, sorry you can't attend the dinner.")
print(Guests)

popped_guest_1 = Guests.pop(1)
print(f"Hello {popped_guest_1}, the dinner table won't arrive in time for the dinner and i have only space for two, sorry you can't attend the dinner.")
print(Guests)

popped_guest_2 = Guests.pop(2)
print(f"Hello {popped_guest_2}, the dinner table won't arrive in time for the dinner and i have only space for two, sorry you can't attend the dinner.")
print(Guests)

popped_guest_0 = Guests.pop(0)
print(f"Hello {popped_guest_0}, the dinner table won't arrive in time for the dinner and i have only space for two, sorry you can't attend the dinner.")
print(Guests)

del Guests[0]
print(Guests)

del Guests[0]
print(Guests)

Guests = ['sam', 'craig', 'david']
print(Guests)
print(f"The number of Guests invited for the party is {len(Guests)}")