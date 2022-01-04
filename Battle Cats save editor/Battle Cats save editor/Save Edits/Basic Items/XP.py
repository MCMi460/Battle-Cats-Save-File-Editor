def xp(path:str):
    XP = int(input("How much XP do you want?(max 99999999)\n"))
    if XP > 99999999:
        XP = 99999999
    elif XP < 0:
        XP = 0

    stream = io.open(path, mode='r+b')
    print(f"Set XP to {XP}")

    xp_bytes = (XP).to_bytes(4, "little")
    startPos = 76

    # If using jp, xp is stored 1 offset less
    if gameVer == "jp":
        startPos = 75
    stream.seek(startPos)
    stream.write(xp_bytes)
