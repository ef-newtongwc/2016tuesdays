# This dictionary lists the value of every tile in Scrabble. The keys are the individual letters,
# and the (Python) values are the (tile) value in the game.

value_of_tile = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
                 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
                 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
                 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

rawStart = raw_input("type a word: ")
word = rawStart.upper()
total = 0

for letter in word:
    value = value_of_tile[letter]
    print "%s is worth %d" % (letter, value_of_tile[letter])
    eachTile = value_of_tile[letter]
    total = total + eachTile

print "  "
print "The total value of your word is: "
print total

    #totalValue = sum(eachTile)
