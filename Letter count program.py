#Welcome to the letter Counter App
print("welcome to the letter counter app")
#get user input
name=input("\nWhat is your name: ").title().strip()
print("hello " + name + "!")
print("\nI will count the number of times a specific letter occur in a message ")
message=input("Please enter a message: ")

letter=input("Wich letter would you want to count the occurance of: ")
#standarize to lower case so that all letter are counted
message=message.lower()
letter=letter.lower()
#result and display
Count_of_letter=message.count(letter)
print("\n"+ name + ",your message has " + str(Count_of_letter)+ " " + letter + "'s in it")
