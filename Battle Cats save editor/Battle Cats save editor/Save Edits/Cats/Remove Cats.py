def RemCats(path:str):
    occurrence = OccurrenceB(path)
    with io.open(path, mode='r+b') as stream:
        i = occurrence[0] + 4
        while i <= occurrence[1] - 4:
            stream.seek(i)
            stream.write((0).to_bytes(1, "little"))
            i += 4
        print("Removed all cats")
