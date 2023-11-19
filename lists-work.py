friends = ['adam', 'celene', 'kayla', 'lynne', 'whitney']
message = f"{friends[0].title()} is a good friend."
print(message)
print(friends)
#use the index to print one friend
print(friends[0])
#capitalize friends name
print(friends[0].title())
#print a message to each friend using a for loop
friends = ['adam', 'celene', 'kayla', 'lynne', 'whitney']
for friend in friends:
    print(f"{friend.title()}, is a great friend!")
trucks = ['ram', 'chevy', 'yota', 'hemi']
for truck in trucks:
    print(f"I would like to own a {truck.title()}.")