ThirtyDays = ["April", "June", "September", "November"]
ThirtyOneDays = ["January", "March", "May", "July", "August", "October", "December"]

print "This is the Days-In-A-Month program! Enter a month and i will tell you how many days there are."
user_input = raw_input("type a month: ")

if user_input == "Febuary":
    print "this month has 28 or 29 days!"

for month in ThirtyDays:
    if user_input == month:
        print "this month has 30 days!"

for month in ThirtyOneDays:
    if user_input == month:
        print "this month has 31 days!"
else:
    print("try again")

