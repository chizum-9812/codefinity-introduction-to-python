grocery_inventory = {"Milk":("Dairy",3.50,8),
                    "Eggs":("Dairy",5.50,30),
                    "Bread":("Bakery",2.99,15),
                    "Apples":("Produce",1.50,50)}
egg_price = grocery_inventory["Eggs"][1]

if egg_price>5.00:
    print("Eggs are too expensive, reducing the price by $1.")
    new_egg_price=egg_price-1.00
    category,price,stock=grocery_inventory["Eggs"]
    grocery_inventory["Eggs"]=(category,new_egg_price,stock)

else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print ("Inventory after adding Tomatoes: ",grocery_inventory)

milk_stock=grocery_inventory["Milk"][2]
if milk_stock<10:
    new_milk_stock=milk_stock+20
    print ("Milk needs to be restocked. Increasing stock by 20 units.")
    category,price,stock=grocery_inventory["Milk"]
    grocery_inventory["Milk"]=(category,price,new_milk_stock)

else:
    print("Milk has sufficient stock.")

if grocery_inventory["Apples"][1]>2.00:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory: ",grocery_inventory)