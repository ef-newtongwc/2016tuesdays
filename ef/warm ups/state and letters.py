states = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Delaware',
        'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana',
        'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana',
        'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada',
        'New York', 'Ohio', 'Oklahoma','Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
        'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming'
]

guess = raw_input('Type a Letter:')
guessInLower = guess.lower()
guessInUpper = guess.upper()
print guessInUpper
print "states that start with that letter are: "
for state in states:
    if state[0] == guessInUpper:
        print(state)

print " "

print "states with that letter are: "
for state in states:
    #if guessInLower in state:
     #   print(state)
    #if guessInUpper in state:
     #   print(state)
        #count = state.count('guess')
        #print count
