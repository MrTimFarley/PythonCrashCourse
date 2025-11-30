alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print(alien_0)

del alien_0['points']
print(alien_0)

print(f"Original x-position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment
print(f"New x-position: {alien_0['x_position']}")
