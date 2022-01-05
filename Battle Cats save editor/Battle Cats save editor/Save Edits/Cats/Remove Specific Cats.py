def RemSpecifiCat(path:str):
    occurrence = OccurrenceB(path)
    with io.open(path, mode='r+b') as stream:
        catIds = input("Cat list: https://battle-cats.fandom.com/wiki/Cat_Release_Order\nWhat is the cat ID?, input multiple ids separated by spaces to add multiple cats at a time\n").split('\n')
        for i in range(len(catIds)):
            catID = int(catIds[i])
            startPos = occurrence[0] + 4
            stream.seek(startPos + catID * 4)
            stream.write((0).to_bytes(1, "little"))
            ColouredText(f"&Removed cat: &{catID}\n")
