def Outbreaks(path:str):
    # Length of first outbreak chunk
    length = 237
    toSearch = bytearray([ 0 for x in range(length) ])
    choice = bytearray([ 0 for x in range(length) ])
    # Generate search terms
    for i in range(47):
        toSearch[(i * 5) + 1] = i + 1
        choice[i * 5] = 1
    toSearch[236] = 0x01
    choice[235] = 0x01
    pos = ThirtySix(path)[0]

    found = False
    StartPos = 0

    # Search for outbreak position
    pos2 = Search(path, toSearch, False, pos, choice)[0]
    with io.open(path, mode='r+b') as stream:
        allData = stream.read()
        if pos2 > 0:
            found = True
            StartPos = pos2
        if not found or StartPos < 100:
            Error()
        for j in range(len(allData)):
            stream.seek(StartPos + (j * 5))
            stream.write((1).to_bytes(1,"little"))
            # If it reaches the end of a chapter, skip forward to the next one and write some data
            if allData[StartPos + (j * 5) + 10] == 0x30:
                StartPos += 5
                stream.seek(StartPos + (j * 5))
                stream.write((1).to_bytes(1,"little"))
                if allData[StartPos + (j * 5) + 1] >= 0x07:
                    break
                StartPos += 8
            elif allData[StartPos + (j * 5) + 13] >= 0x40:
                break
    print("Successfully cleared all zombie stages")
