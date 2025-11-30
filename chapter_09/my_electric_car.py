from car import Car
from car import ElectricCar
from car import Battery

my_leaf = ElectricCar('nissan', 'leaf', 2024, 'sedan')
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
