#Create a datetime obj and store current date and time

import datetime
time=datetime.datetime.now()
month=str(time.month)
day=str(time.day)
hour=str(time.hour)
minute=str(time.minute)
#welcome mesaage 
foods=["Meat","Cheese"]
print("Welcome to grocery list app")
print("Current date and time :" + month + "/" + day + "\t" + hour+":"+minute)
print("You currently have "+ foods[0] + "and" + foods[1] + "in your List")


#get user input
food=input("\n type of food to add to your grocery list: ")
foods.append(food.title())
food=input("\n type of food to add to your grocery list: ")
foods.append(food.title())
food=input("\n type of food to add to your grocery list: ")
foods.append(food.title())

#print and sort the list
print("\n here is your grocery list")
print(foods)
foods.sort()
print("here is your grocery list sorted:")
print(foods)
#stimulate shopping
print("\n stimulating grocery shopping....")
print("\n Current grocery list:" +str(len(foods)))
print(foods)
buy_food=input("what food did you just buy: ")
foods.remove(buy_food.title())
print("removing" + buy_food+ " from the list...")
buy_food=input("what food did you just buy: ")
foods.remove(buy_food.title())
print("removing" + buy_food+ " from the list...")
buy_food=input("what food did you just buy: ")
foods.remove(buy_food.title())
print("removing" + buy_food+ " from the list...")
#the store is out of an item
print("\n Curremt grocery list:"+ str(len(foods))+"items")
print(foods)
no_item=foods.pop()
print("\n the store is out of "+ no_item +".")
new_food=input("What food would you like insted").title()
foods.insert(0,new_food)
print("\n here is what remians on your grocery list")
print(foods)


      
