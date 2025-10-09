for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)
for number in numbers:
    print(number)
    
squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# 4-3. Counting to Twenty:

for number in range(1, 21):
    print(number)
    
#4-4. One Million:

numbers =  list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

multiples = [multiple*3 for multiple in range(1, 11)]

for multiple in multiples:
    print(multiple)

cubes = [cube**3 for cube in range(1,11)]

for cube in cubes:
    print(cube)

#slicing in lists
players = ['charles', 'martina', 'florence', 'eli']
print(players[0:3])


#4-10. Slices:
print("The first three players are:\n")
for player in players[0:3]:
    print(player)
    
print("Three players from the middle of the list are:")
for player in players[1:5]:
    print(f"\t{player}")
    
    
    
    