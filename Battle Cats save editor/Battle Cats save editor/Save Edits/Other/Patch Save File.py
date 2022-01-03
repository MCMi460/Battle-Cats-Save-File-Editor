def patchSaveFile(choice:str,path:str):
    if path.endswith(".list") or path.endswith(".pack") or path.endswith(".so") or path.endswith(".csv"):
        raise Exception("Not a save file")

    stream = io.open(path, mode='rb')
    allData = stream.read()
    stream.close()

    toBeUsed = []
    for i in range(len(allData) - 32):
        toBeUsed.append(allData[i])
    bytes = "battlecats".encode(encoding='ASCII')
    if choice != "jp":
        bytes = ("battlecats" + choice).encode(encoding='ASCII')
    test = 32 - len(bytes)

    Usable = bytes + bytearray(toBeUsed)


    Data = hashlib.md5(Usable).digest()

    hex = str(Data)
    print("Data patched")

    EncyptedHex = str(Data)

    hex = hex.lower()

    stuffs = hex.encode(encoding='ASCII')

    allData = bytearray(allData)
    allData = allData[:len(allData) - 32]
    allData.extend(stuffs)
    stream = io.open(path, mode='wb')
    stream.write(allData)
    stream.close()
    return choice
