def patchSaveFile(choice:str,path:str):
    if path.endswith(".list") or path.endswith(".pack") or path.endswith(".so") or path.endswith(".csv"):
        raise Exception("Not a save file")

    stream = io.open(path, mode='rb')
    allData = stream.read()
    stream.close()

    toBeUsed = bytearray()
    stream = io.open(path, mode='rb')
    for i in range(len(allData) - 32):
        toBeUsed.extend(stream.read(1))
    stream.close()
    bytes = "battlecats".encode(encoding='ASCII')
    if choice != "jp":
        bytes = ("battlecats" + choice).encode(encoding='ASCII')
    test = 32 - len(bytes)

    Usable = bytearray()
    Usable[:] = bytes
    Usable[:] = toBeUsed


    md5 = hashlib.md5()

    md5.update(Usable)
    Data = md5.hexdigest()

    hex = str(Data)
    print("Data patched")

    EncyptedHex = str(Data)

    hex = hex.lower()

    stuffs = hex.encode(encoding='ASCII')

    stream = io.open(path, mode='r+b')
    stream.seek(len(allData) - 32 + len(stuffs))
    stuffs = stuffs + stream.read()
    stream.seek(len(allData) - 32)
    stream.write(stuffs)
    stream.close()
    return choice
