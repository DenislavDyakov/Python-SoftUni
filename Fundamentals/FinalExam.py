#Problem 1
email = input()

command = input()

while command != "Valid":
    command = command.split()
    if command[0] == "Upper":
        index = int(command[1])
        email = email[:index] + email[index].upper() + email[index+1:]
        print(email)
    elif command[0] == "Lower":
        index = int(command[1])
        email = email[:index] + email[index].lower() + email[index+1:]
        print(email)
    elif command[0] == "Insert":
        index = int(command[1])
        char = command[2]    
        left_part = email[:index]
        right_part = email[index:]
        email = left_part + char + right_part
        print(email)
    elif command[0] == "Change":
        char = command[1]  
        value = int(command[2])
        if char in email:
            ascii_value = int(ord(char))
            total_value = ascii_value + value
            new_char = chr(total_value)
            email = email.replace(char, new_char)
            print(email)
        #else:
            #continue
            #command = input()
    elif command[0] == "Validation":
        if len(email) < 6:
            print(f"Email must be at least 6 characters long!")
        
        
        for char in email:
            if char.isdigit() == False and char.isalpha() == False and char != '@':
                print(f"Email must consist only of letters, digits and @!")
                #command = input()
                continue
        
        upper_case = 0
        for char in email:
            if char.isupper() == True:
                upper_case += 1
        if upper_case <= 0:
            print(f"Email must consist at least one uppercase letter!")
            
        lower_case = 0
        for char in email:
            if char.islower() == True:
                lower_case += 1
        if lower_case <= 0:
            print(f"Email must consist at least one lowercase letter!")
        
        digit = 0
        for char in email:
            if char.isdigit() == True:
                digit += 1
        if digit <= 0:
            print(f"Email must consist at least one digit!")
    

    command = input()
	
	
#Problem 2
import re 

pattern = r"(?P<boss_sep>\|)(?P<boss>[A-Z]{4,})(?P=boss_sep):(?<!\s)(?P<title_sep>\#)(?P<title>[A-Za-z]+\s[A-Za-z]+)(?P=title_sep)"

number_lines = int(input())

while number_lines != 0:
    text = input()
    check_validity = re.findall(pattern, text)
    if check_validity:
        boss = check_validity[0][1]
        title = check_validity[0][3]

        length_name = len(boss)
        length_title = len(title)
        
        print(f"{boss}, The {title}")
        print(f">> Strength: {length_name}")
        print(f">> Armour: {length_title}")
    
    else:
        print(f"Access denied!")
        
    number_lines -= 1  
    
#Problem 3
command = input()

stock = {}
sold = {}

while command != "Complete":
    action, quantity, food = command.split()
    quantity = int(quantity)

    if action == "Receive":
        if quantity <= 0:
            command = input()
            continue
        elif food not in stock:
            stock[food] = quantity
        else:
            stock[food] += quantity
    
    elif action == "Sell":
        if food not in stock:
            print(f"You do not have any {food}.")
        elif stock[food] < quantity:
            if food not in sold:
                sold[food] = stock[food]
            else:
                sold[food] += stock[food]
            
            print(f"There aren't enough {food}. You sold the last {stock[food]} of them.")
            del stock[food]
        else:
            stock[food] -= quantity
            if food not in sold:
                sold[food] = quantity
            else:
                sold[food] += quantity
                
            print(f"You sold {quantity} {food}.")   
            if stock[food] == 0:
                del stock[food]
    
    command = input()

sorted_stock = sorted(stock.items(), key=lambda x: x[0])
for food, quantity in sorted_stock:
    print(f"{food}: {quantity}")

count_sold = 0
for food, quantity in sold.items():
    count_sold += quantity
    
print(f"All sold: {count_sold} goods")
