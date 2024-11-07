actualNumber = int(input("Numero inicial: "))
stop = False
while stop != True:
    with open("lists.txt", "a") as file:
        actualList = [actualNumber]
        notOne = True
        while actualList[-1] != 1:
            if actualList[-1] % 2 == 0:
                actualList.append(actualList[-1] / 2)
            else:
                actualList.append((actualList[-1] * 3) + 1)
        file.write(str(actualList) + "\n")
        actualNumber += 1