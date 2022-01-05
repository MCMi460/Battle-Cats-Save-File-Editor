def Bundle(path:str):
    with io.open(path, mode='r+b') as stream:
        length = os.path.getsize(path)
        allData = stream.read()
        found = False

        # Search for bundle counter position
        for i in range(length - 32):
            if allData[i] == 0x31 and allData[i + 1] == 0 and allData[i + 2] == 0 and allData[i + 3] == 0 and allData[i + 4] == 0x32 and allData[i + 5] == 0 and allData[i + 6] == 0 and allData[i + 7] == 0 and allData[i + 8] == 0x33 and allData[i + 9] == 0 and allData[i + 10] == 0 and allData[i + 11] == 0:
                stream.seek(i - 4)
                # Set total counter for bundle menus seen to 65535, stopping the game from opening any more
                stream.write((0xff).to_bytes(1, "little"))
                stream.write((0xff).to_bytes(1, "little"))
                found = True
                break
        if not found:
            Error()
        print("Closed all bundle menus")
