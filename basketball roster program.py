#basketball roster program
print("Welcome too the basketball Roster program")
roster=[]
player=input("who is your point gaurd:").title()
roster.append(player)
player=input("who is your shooting gaurd:").title()
roster.append(player)
player=input("who is your small forward:").title()
roster.append(player)
player=input("who is your power forward:").title()
roster.append(player)
player=input("who is your center:").title()
roster.append(player)
#display roster
print("\n\tYour starting 5 for for the upcoming basketball")
print("\n\tPoint Gaurd:\t\t" + roster[0])
print("\n\tshooting faurd:\t\t" + roster[1])
print("\n\tSmall forward:\t\t" + roster[2])
print("\n\tPower forward:\t\t" + roster[3])
print("\n\tCenter:\t\t\t" + roster[4])

#remove an injured player
injured_player=roster.pop(2)
print("\n oh no, "+ injured_player +" is injured.")
roster_length=len(roster)
print("Your roster only has " +str(roster_length)+ " player.")
#add a new player
added_player=input("who will take "+ injured_player +" spot.").title()
roster.insert(2,added_player)
#updating starting five
print("\n\tPoint Gaurd:\t\t" + roster[0])
print("\n\tshooting faurd:\t\t" + roster[1])
print("\n\tSmall forward:\t\t" + roster[2])
print("\n\tPower forward:\t\t" + roster[3])
print("\n\tCenter:\t\t\t" + roster[4])

print("\n Good luck "+ roster[2] +" you will do great.")
roster_length=len(roster)
print("\n your roster now have " +str(roster_length)+" players.")

