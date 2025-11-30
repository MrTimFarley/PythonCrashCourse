motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'vespa']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
motorcycles.append('lambretta')
motorcycles.insert(0, 'yamaha')
del motorcycles[2]

print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
working_copy = motorcycles.pop()
print(motorcycles)
print(f"\nThe last motorcycle I owned was a {working_copy.title()}.")
