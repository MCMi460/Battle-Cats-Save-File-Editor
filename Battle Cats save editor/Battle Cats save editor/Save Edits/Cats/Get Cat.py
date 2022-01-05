def Cats(path:str):
    occurrence = OccurrenceB(path)
    with io.open(path, mode='r+b') as stream:
        ids = 0
        i = occurrence[0] + 4
        while i <= occurrence[1] - 4:
            if ids != 542:
                stream.seek(i)
                stream.write((1).to_bytes(1, "little"))
            ids += 1
            i += 4
        print("Gave all cats")
