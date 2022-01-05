def Elsewhere(path:str):
    print("Please select a working save that doesn't have 'Save is used elsewhere' and has never had it in the past\nPress enter to select that save")
    input()
    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.ExistingFiles)
    dlg.setNameFilters(["working battle cats save ()",])
    dlg.selectNameFilter("working battle cats save ()")
    path2 = ""

    if dlg.exec_() == QDialog.Accepted:
        fileToOpen = dlg.selectedFiles()
        path2 = fileToOpen[0]
    else:
        ColouredText("Please select your save\n");
        SelSave()
        return
    condtions1 = bytearray([ 0x2d, 0x00, 0x00, 0x00, 0x2e ])
    # Search for rough inquiry code position in second save
    pos1 = Search(path2, condtions1)[0]
    if pos1 == 0:
        Error()

    with io.open(path, mode='r+b') as stream:
        allData = stream.read()

        codeBytes = bytearray()
        codeBytes2 = bytearray()
        iqExtra = bytearray()
        lastKey = bytearray()
        found = []

    # Search for token position in second save
    condtions2 = bytearray([ 0x78, 0x63, 0x01 ])
    pos2 = Search(path2, condtions2, False, len(allData) - 800)[0]
    if pos2 == 0:
        Error()

    with io.open(path, mode='r+b') as stream:

        # Search for inquiry code position from rough position in second save
        for j in range(1900,2108):
            if allData[pos1 - j] == 9 and allData[pos1 - j + 1] == 0 and allData[pos1 - j + 2] == 0 and allData[pos1 - j + 3] == 0 and allData[pos1 - j - 1] == 0 and allData[pos1 - j + 23] == 0x2c:
                found.append(1)
                # Save it in an array
                stream.seek(pos1 - j + 4)
                iqExtra = stream.read(11)
                break
        # Check for token
        for i in range(pos2 + 9,pos2 + 100):
            if allData[i] >= 48 and allData[i + 1] >= 48 and allData[i + 2] >= 48 and allData[i + 3] >= 48:
                pos2 = i
                found.append(1)
                break
        # Save token to array
        stream.seek(pos2)
        lastKey = stream.read(45)

        if (len(found) < 2):
            Error()
        # Search for rough inquiry code in first save
        pos3 = Search(path, condtions1)[0]
        if pos3 == 0:
            Error()
        found.append(1)
    with io.open(path, mode='r+b') as stream:
        allData = stream.read()
    # Search for token position in first save
    pos4 = Search(path, condtions2, false, len(allData) - 800)[0]
    if pos4 == 0:
        Error()
    found.append(1)

    with io.open(path, mode='r+b') as stream:
        # Search for inquiry code position starting from rough position
        for j in range(1900,2108):
            if allData[pos3 - j] == 9 and allData[pos3 - j + 1] == 0 and allData[pos3 - j + 2] == 0 and allData[pos3 - j + 3] == 0 and allData[pos3 - j - 1] == 0 and allData[pos3 - j + 23] == 0x2c:
                found.append(1)
                stream.seek(pos3 - j + 4)
                # Set inquiry code in first save to inquiry code in second save
                stream.write(iqExtra)
                break
        for i in range(pos4 + 9,pos4 + 100):
            if allData[i] >= 48 and allData[i + 1] >= 48 and allData[i + 2] >= 48 and allData[i + 3] >= 48:
                pos4 = i
                break
        stream.seek(pos4)
        # Set token in first save to token in second save
        stream.write(lastKey)
        found.append(1)
        if len(found) < 4:
            Error()
        else:
            print("Success")
