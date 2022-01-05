def SoL(path:str):
    with io.open(path, mode='r+b') as stream:
        allData = stream.read()
        # Stars unlocked/unlock next chapter
        unlock = 0
        # Times beaten/graphical fix
        levels = 0
        # Levels beaten/unlock next chapter/levels
        levsBeaten = 0

        # Search for SoL positions
        for i in range(len(allData)):
            if allData[i] == 5 and allData[i + 1] == 0x2c and allData[i + 2] == 1 and allData[i + 3] == 4 and allData[i + 4] == 0x0c:
                levsBeaten = i + 6005
                levels = i + 12005
            elif allData[i] == 0x2C and allData[i + 1] == 0x01 and allData[i + 2] == 0 and allData[i - 1] == 0 and allData[i + 3] == 0 and allData[i - 2] == 0 and allData[i - 3] == 0:
                unlock = i
                break
        if levels == 0 or unlock == 0:
            Error()
        ColouredText("&What subchapter do you want to edit?, enter an id starting at &1& = &Legend Begins&, &2& = &Passion land& etc, you can enter multiple ids seperated by spaces, e.g &1 5 4 7&, or you can enter 2 ids seperated by a &-& to edit a range of" +
        " chapters, e.g &1&-&7&, or you can enter &all& to edit all subchapters at once")
        c_input = input()
        totalChapters = 49
        chaptersToEdit = []
        if "-" in c_input:
            start = int(c_input.split("-")[0])
            end = int(c_input.split("-")[1])
            i = start
            while i <= end:
                chaptersToEdit.append(i)
                i += 1
        elif c_input.lower() == "all":
            start = 1
            end = totalChapters
            for i in range(start,end):
                chaptersToEdit.append(i)
        else:
            ids = [ int(x) for x in c_input.split(' ') ]
            [ chaptersToEdit.append(x) for x in ids ]
        ColouredText("&Do you want to set all of the stars/crowns at the same time (&1&), or individually (&2&)?")
        sameOrIndividual = input()
        stars = 0
        # Same
        if sameOrIndividual == "1":
            ColouredText("&How many stars/crowns do you want to complete for each chapter (&1&-&4&)")
            stars = int(input())
        for i in range(len(chaptersToEdit)):
            # Individual
            if sameOrIndividual == "2":
                ColouredText(f"&How many stars/crowns do you want to complete for chapter &{chaptersToEdit[i]}&? (&1&-&4&)")
                stars = int(input())
            # Levels beaten, required for next chapter to unlock
            id = chaptersToEdit[i] - 1
            stream.seek(levsBeaten + (id * 4))
            for j in range(stars):
                stream.write((8).to_bytes(1, "little"))
            # Stars/crowns unlocked and required for next chapter to unlock
            stream.seek(unlock - 6152 + ((id + 1) * 4))
            stream.write((3).to_bytes(1, "little"))
            # Times stage has been beaten, required to avoid graphical issues
            stream.seek(levels + (id * 97) - id)
            startpos = levels + (id * 97) - id
            for j in range(stars):
                for k in range(8):
                    stream.write((1).to_bytes(1, "little"))
                    stream.seek(7,1)
                stream.seek(startpos + (j * 2) + 2)
