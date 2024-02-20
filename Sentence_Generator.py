def sentenceInput():
    passage1 = input("Enter Passage here: ")
    splitPassage1 = passage1.split(". ")
    storePassage = []

    for i in splitPassage1:
        storePassage.append(i)
    print(storePassage)

