from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os, os.path, sys, requests, io, hashlib
from datetime import datetime
l = locals()
# Game Mods

# Basic Item Edits
with open("Save Edits/Basic Items/CatFood.py","r") as file:
    exec(file.read(), globals(), l)
    catFood = l['catFood']
with open("Save Edits/Basic Items/XP.py","r") as file:
    exec(file.read(), globals(), l)
    xp = l['xp']
# Cat Edits
with open("Save Edits/Cats/Get Cat.py","r") as file:
    exec(file.read(), globals(), l)
    Cats = l['Cats']
with open("Save Edits/Cats/Get Specific Cats.py","r") as file:
    exec(file.read(), globals(), l)
    SpecifiCat = l['SpecifiCat']
with open("Save Edits/Cats/Remove Cats.py","r") as file:
    exec(file.read(), globals(), l)
    RemCats = l['RemCats']
with open("Save Edits/Cats/Remove Specific Cats.py","r") as file:
    exec(file.read(), globals(), l)
    RemSpecifiCat = l['RemSpecifiCat']
# Other Edits
with open("Save Edits/Other/New Inquiry Code.py","r") as file:
    exec(file.read(), globals(), l)
    NewIQ = l['NewIQ']
with open("Save Edits/Other/Patch Save File.py","r") as file:
    exec(file.read(), globals(), l)
    patchSaveFile = l['patchSaveFile']

catAmount = 0
Savepaths = []
gameVer = ""
version = '2.38.1'

Color = {
"Default": "\x1b[39m",
"Black": "\x1b[30m",
"Red": "\x1b[31m",
"Green": "\x1b[32m",
"Yellow": "\x1b[33m",
"Blue": "\x1b[34m",
"Magenta": "\x1b[35m",
"Cyan": "\x1b[36m",
"LightGray": "\x1b[37m",
"DarkGray": "\x1b[90m",
"LightRed": "\x1b[91m",
"LightGreen": "\x1b[92m",
"LightYellow": "\x1b[93m",
"LightBlue": "\x1b[94m",
"LightMagenta": "\x1b[95m",
"LightCyan": "\x1b[96m",
"White": "\x1b[97m",
}

def SelSave():
    global Savepaths, gameVer
    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.ExistingFiles)
    dlg.setNameFilters(["battle cats save ()",])
    dlg.selectNameFilter("battle cats save ()")

    if dlg.exec_() == QDialog.Accepted:
        fileToOpen = dlg.selectedFiles()
        for i in range(len(fileToOpen)):
            ColouredText(f"&Save: &\"{os.path.basename(fileToOpen[i])}\"&\n", "White", "Green")
        Savepaths = fileToOpen
    else:
        ColouredText("Please select your save\n");
        SelSave()
        return
    gameVer = input("What game version are you using? (e.g en, jp, kr), note: en currently has the most support with the editor, so features may not work in other versions\n")

def MakeRequest(url):
    headers = {
    "time-stamp": '{:f}'.format((datetime.utcnow() - datetime(1, 1, 1)).total_seconds() * 10000000)
    }
    return requests.get(url, headers=headers)

def Error(text:str = "Error, a position couldn't be found, please report this in #bug-reports on discord"):
    raise Exception(text)

def GetCatNumber(path:str):
    # If the save file is not a save file, don't modify/read it as one
    if path.endswith(".list") or path.endswith(".pack") or path.endswith(".so") or path.endswith(".csv"):
        raise Exception("Not a save file")
    stream = io.open(path, mode='rb')

    allData = stream.read()
    anchour = 0

    for i in range(7344,7375):
        try:
            if allData[i] == 2:
                anchour = allData[i - 1]
                break
        except:
            raise Exception("Error, this save file seems to be different/corrupted, if this is an actual bc save file, please report this to the discord")
    if anchour == 0:
        for i in range(7375,10800):
            try:
                if allData[i] == 2:
                    anchour = allData[i - 1]
                    break
            except:
                raise Exception("Error, this save file seems to be different/corrupted, if this is an actual bc save file, please report this to the discord")
    stream.close()
    return anchour

def UpgradeCats(path:str, catIDs:list, plusLevels:list, baseLevels:list, ignore:int = 0):
    if not all(isinstance(x, int) for x in catIDs) or not all(isinstance(x, int) for x in plusLevels) or not all(isinstance(x, int) for x in baseLevels):
        raise Exception('Expected integer list')
    occurrence = OccurrenceB(path)
    stream = io.open(path, mode='rb')

    x_bytes = stream.read()
    Position = 0
    pos = occurrence[1] + 1

    for i in range(len(catIDs)):
        Position = pos + (catIDs[i] * 4) + 3
        if ignore != 2:
            x_bytes[Position] = bytes(plusLevels[i])
            Position -= 1
        Position += 2
        if ignore != 1:
            x_bytes[Position] = bytes(baseLevels[i])

    stream.close()
    stream = io.open(path, mode='wb')
    stream.write(x_bytes)
    stream.close()

def LoadData(path:str):
    stream = io.open(path, mode='rb')

    allData = stream.read()

    return allData

def GetCurrentCats(path:str):
    occurrence = OccurrenceB(path)

    stream = io.open(path, mode='rb')

    catsL = []

    allData = stream.read()

    for i in range(len(catAmount)):
        startPos = occurrence[0] + 4
        if allData[startPos + (i * 4)] == 1:
            catsL.append(i)

    return catsL

def Options():
    fileToOpen = Savepaths
    path = fileToOpen[0]
    print(f"{Color['Red']}Backup your save before using this editor!\nIf you get an error along the lines of \"Your save is active somewhere else\"then select option 20-->2, and select a save that doesn't have that error and never has had the error\n")
    print(f"{Color['Green']}Thanks to: Lethal's editor for being a tool for me to use when figuring out how to patch save files, uploading the save data onto the servers how to and edit cf/xp\nAnd thanks to beeven and csehydrogen's open source work, which I used to implement the save patching algorithm\n")

    Features = [
        "Select a new save", "Cat Food", "XP", "Tickets / Platinum Shards", "Leadership", "NP", "Treasures", "Battle Items", "Catseyes", "Cat Fruits / Seeds", "Talent Orbs", "Gamatoto", "Ototo", "Gacha Seed", "Equip Slots", "Gain / Remove Cats", "Cat / Stat Upgrades", "Cat Evolves", "Cat Talents",
        "Clear Levels / Outbreaks / Timed Score", "Inquiry Code / Elsewhere Fix / Unban", "Close the rank up bundle / offer menu", "Game Modding menu", "Calculate checksum of save file",
    ]
    ColouredText("Warning: if you are using a non en save, many features won't work, or they might corrupt your save data, so make sure you back up your saves!\n", "White", "Red");

    toOutput = "&What would you like to do?&\n0.& Select a new save\n&"
    for i in range(1,len(Features)):
        toOutput = toOutput + f"&{i}.& {Features[i]}" + "\n"
    ColouredText(toOutput)

    CatNumber = []
    CatNumber.append(GetCatNumber(path))
    CatNumber.append(0x02)
    catAmount = int(CatNumber[0])
    Choice = ""
    while Choice == "":
        Choice = input()
    Choice = int(Choice)

    for i in range(len(fileToOpen)):
        path = fileToOpen[i]

        if Choice == 0:
            SelSave()
            Options()
            return
        elif Choice == 1:
            catFood(path)
        elif Choice == 2:
            xp(path)
        elif Choice == 3:
            pass
        elif Choice == 4:
            pass
        elif Choice == 5:
            pass
        elif Choice == 6:
            pass
        elif Choice == 7:
            pass
        elif Choice == 8:
            pass
        elif Choice == 9:
            pass
        elif Choice == 10:
            pass
        elif Choice == 11:
            pass
        elif Choice == 12:
            pass
        elif Choice == 13:
            pass
        elif Choice == 14:
            pass
        elif Choice == 15:
            GetCats(path)
        elif Choice == 16:
            pass
        elif Choice == 17:
            pass
        elif Choice == 18:
            pass
        elif Choice == 19:
            pass
        elif Choice == 20:
            NewIQ(path)
        elif Choice == 21:
            pass
        elif Choice == 22:
            pass
        elif Choice == 23:
            pass
        else:
            print("Please input a number that is recognised")
        patchSaveFile(gameVer, path)
    input("Press enter to continue\n")
    Options()

def GetCats(path:str):
    Features = [
        "Go back",
        "Get all cats",
        "Get specific cats",
        "Remove all cats",
        "Remove specific cats",
    ]

    toOutput = "&What would you like to edit?&\n0.& Go back\n&"
    for i in range(1,len(Features)):
        toOutput = toOutput + f"&{i}.& {Features[i]}" + "\n"
    ColouredText(toOutput)
    choice = int(input())

    if choice == 0:
        Options()
    elif choice == 1:
        Cats(path)
    elif choice == 2:
        SpecifiCat(path)
    elif choice == 3:
        RemCats(path)
    elif choice == 4:
        RemSpecifiCat(path)
    else:
        print(f"Please enter a number between 0 and {len(Features)}")

def OccurrenceB(path:str):
    stream = io.open(path, mode='rb')

    allData = stream.read()

    occurrence = []
    stream.close()
    anchour = GetCatNumber(path)

    for i in range(4000,len(allData) - 1):
        if allData[i] == anchour:
            if allData[i + 1] == 2 and allData[i + 2] == 0 and allData[i + 3] == 0:
                occurrence.append(i)
    stream.close()

    return occurrence

def ColouredText(input:str, Base:str = "White", New:str = "Yellow"):
    split = input.split('&')
    if split == input:
        print(Color['Red'],end='')
        print("\nNo & characters in inputed string!")
    print(Color[New],end='')
    i = 0
    while i < len(split):
        print(Color[New],end='')
        print(split[i],end='')
        print(Color[Base],end='')
        if i == len(split) - 1:
            break
        print(split[i + 1],end='')
        i += 2
    print(Color[Base])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        SelSave()
        Options()
    except Exception as e:
        print("An error has occurred\nPlease report this in #bug-reports:")
        print(e)
        input("Press enter to exit")
        quit()
