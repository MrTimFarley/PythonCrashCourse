available_toppings = ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['pepperoni', 'canadian bacon', 'sausage']

for requested_topping in requested_toppings:
    if requested_topping not in available_toppings:
        print(f"Adding {requested_topping}.")
        available_toppings.append(requested_topping)
    else:
        print(f"Okay, we have {requested_topping}.")
    print(f"Available toppings are: {available_toppings}")
    
print("\nFinished making your pizza!")