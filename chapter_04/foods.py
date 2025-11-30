my_foods = ['pizza', 'falafel', 'chocolate cake']
friend_foods = my_foods[:]
for food in my_foods:
    print(f"I like {food}.")


my_foods.append('soup')
my_foods.append('potatoes')

friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nHere are my first 3 favorite foods:")
for food in my_foods[:3]:
    print(food)
print("\nHere are my favorite foods from the middle of the list:")
for food in my_foods[1:4]:
    print(food)
print("\nHere are my last 3 favorite foods:")
for food in my_foods[-3:]:
    print(food)
