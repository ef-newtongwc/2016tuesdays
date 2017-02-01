animalList = []
while True:
    Animal = raw_input("Enter a animal: ")
    print (Animal)
    animalList.append(Animal)
    print " The Animals are: "
    for Animal in animalList:
        print Animal
        animalLength = len(Animal)
        print animalLength

    #print "The animal with the longest length is: "
    #for animal in animalList:
    #    print animalLength
