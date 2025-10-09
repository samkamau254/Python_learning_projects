alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


#working with dictionaries
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2
    
else:
    #This must be a fast alien.
    x_increment = 3
    
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()

print(f"Sarah's favorite language is {language}.")

#Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('point', 'No point value assigned.')
print(point_value)
