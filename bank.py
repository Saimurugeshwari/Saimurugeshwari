#Get user input
greet=input("greeting:")
new_greet=greet.lower().strip()
#create condition useing case-insensitive and print
if "hello" in new_greet:
    print("$0")
#if answer starts with 'h',print $20
elif 'h'==new_greet[0]:
    print("$20")
#otherwise
else:
    print("$100")