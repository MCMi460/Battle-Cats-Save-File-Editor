def CatUpgrades(path:str):
    occurrence = OccurrenceB(path)
    ColouredText("&What level do you want?:enter the &base& followed by a &+& then the &plus& level you want, e.g 50+80, 30+0, 10+30\nEnter the base followed by a plus with nothing else to leave the plus value as it is, e.g 50+, or 20+\nEnter " +
    "a plus followed by the plus value to leave the base values as they are e.g +20, +50")
    answer = input()
    leave = 0
    baselevel = 0
    plusLevel = 0
    try:
        baselevel = int(answer.split('+')[0]) - 1
    except:
        leave = 1
    try:
        plusLevel = int(answer.split('+')[1])
    except:
        leave = 2
    ids = list(range(0,catAmount + 1))
    plusLevels = [ plusLevel for x in range(catAmount + 1) ]
    baseLevels = [ baselevel for x in range(catAmount + 1) ]
    UpgradeCats(path, ids, plusLevels, baseLevels, leave)

    print(f"Upgraded all cats to level {answer}")
    # Close rank up bundle menu offer thing popping up 100s of times
    Bundle(path)
