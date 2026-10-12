grocery_inventory = {"Milk":("Dairy",3.50,8),
                    "Eggs":("Dairy",5.50,30),
                    "Bread":("Bakery",2.99,15),
                    "Apples":("Produce",1.50,50)}
egg_price = grocery_inventory["Eggs"][1]
print(egg_price)
if egg_price>5.00:
    print("Eggs are too expensive, reducing the price by $1")
    new_egg_price=egg_price-1.00
    grocery_inventory["Eggs"][1]=new_egg_price