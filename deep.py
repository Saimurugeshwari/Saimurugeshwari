#Gte user input
quest=input("what is the answer to the great question of life,the universe,and everthing? ")
if quest.strip().lower()=="42":
    print("yes")
elif quest.strip().lower()=="forty two":
    print("yes")
elif quest.strip().lower()=="forty-two":
    print("yes")
else:
    print("No")