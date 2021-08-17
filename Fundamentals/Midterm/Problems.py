#Problem 1
journey_cost = float(input())
number_months = int(input())


money_saved = 0
month = 0
money_souvenirs = 0
money_needed = 0

while month < number_months:
  month += 1
  if month % 2 != 0 and money_saved != 0:
    money_saved = money_saved - (money_saved * 0.16)
  elif month % 4 == 0:
    money_saved = money_saved * 1.25
  money_saved = money_saved + (journey_cost * 0.25)

if money_saved > journey_cost:
  money_souvenirs = money_saved - journey_cost
  money_souvenirs = "{:.2f}".format(money_souvenirs)
  print(f"Bravo! You can go to Disneyland and you will have {money_souvenirs}lv. for souvenirs.")
else:
  money_needed = journey_cost - money_saved
  money_needed = "{:.2f}".format(money_needed)
  print(f"Sorry. You need {money_needed}lv. more.")
  

#Problem 2
items = input().split('|')
budget = float(input())
 
profit = 0.00
 
old_buy_item = 0.00
new_buy_item = 0.00
old_items_price = []
new_items_price = []
 
for item in items:
    args = item.split('->')
    type = args[0]
    price = float(args[1])
 
    if type == 'Clothes' and price <= 50 \
            or type == 'Shoes' and  price <= 35 \
            or type == 'Accessories' and price <= 20.50:
        if budget < price:
            continue
        budget -= price
        old_buy_item += price
        old_items_price.append(price)
 
 
for el in old_items_price:
    el *= 1.4
    new_items_price.append(float(el))
    print(f'{el:.2f}', end=" ")
 
profit = sum(new_items_price) - sum(old_items_price)
print(sep="\n")
print(f"Profit: {profit:.2f}")
 
if budget + sum(new_items_price) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
    
#Problem 3
products = [x for x in input().split("|")]
command = input().split('%')

while command[0] != "Shop!":
    if command[0] == "Important":
        product = command[1]
        if product in products:
            idx = products.index(product)
            products.pop(idx)
            products.insert(0, product)
        else:
            products.insert(0, product)
    elif command[0] == "Add":
        product = command[1]
        if product not in products:
            products.append(product)
        else:
            print("The product is already in the list.")
    elif command[0] == "Swap":
        first_product = command[1]
        second_product = command[2]
        if first_product in products and second_product in products:
            idx_1 = products.index(first_product)
            idx_2 = products.index(second_product)
            products[idx_1], products[idx_2] = products[idx_2], products[idx_1]
        elif first_product in products and second_product not in products:
            print(f"Product {second_product} missing!")
        else:
            print(f"Product {first_product} missing!")
    elif command[0] =="Remove":
        product = command[1]
        if product in products:
            products.remove(product)
        else:
            print(f"Product {product} isn't in the list.")
            
    command = input().split('%')

for product in products:
    print(str(products.index(product)+1) + '. ' +  product) 
