def NewIQ(path:str):
    stream = io.open(path, mode='r+b')
    length = os.path.getsize(path)
    allData = stream.read()

    iq = input("What inquiry code do you want - this code must be set to an account code that actually lets you play without the save is used elsewhere bug\n")
    iq_bytes = bytes(iq, "ascii")
    found = False

    for i in range(length):
        if allData[i] == 0x2D and allData[i + 1] == 0x0 and allData[i + 2] == 0x0 and allData[i + 3] == 0x0 and allData[i + 4] == 0x2E:
            for j in range(1900,2108):
                if allData[i - j] == 0x09:
                    stream.seek(i - j + 4)
                    stream.write(iq_bytes)
                    found = True
    if not found:
        Error()
    print(f"Success\nYour new account code is now: {iq} This should remove that \"save is being used elsewhere\" bug and if your account is banned, this should get you unbanned")
