def MaxTreasures(path:str):
    ColouredText(
        "&What chapter do you want to edit?(You can enter multiple numbers separated by spaces to edit multiple at once):&\n" +
        "&1.& EoC 1\n" +
        "&2.& EoC 2\n" +
        "&3.& EoC 3\n" +
        "&4.& ItF 1\n" +
        "&5.& ItF 2\n" +
        "&6.& ItF 3\n" +
        "&7.& CotC 1\n" +
        "&8.& CotC 2\n" +
        "&9.& CotC 3\n" +
        "&10.& All\n",
        "White", "Yellow")
    choice = input().split(' ')
    print("What level of treasures of you want?: 0=none, 1=inferior, 2=normal, 3=superior:")
    level = int(input())
    with io.open(path, mode='r+b') as stream:
        if level > 255:level = 255

        for k in range(len(choice)):
            choiceInt = int(choice[k])
            if choiceInt <= 3:
                choiceInt -= 1
            j = 0
            startPos = 2986
            endPos = 4942
            ChapterID = 0
            i = startPos
            while i <= endPos:
                j += 1
                # If it's not end of the chapter treasure data write data
                if j % 49 == 0:
                    ChapterID += 1
                else:
                    if ChapterID == choiceInt or choiceInt == 10:
                        stream.seek(i)
                        stream.write((level).to_bytes(1,"little"))
                i += 4
    print(f"All treasures level {level}")
