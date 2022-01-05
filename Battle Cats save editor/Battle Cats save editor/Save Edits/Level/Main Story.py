def Stage(path:str):
    with io.open(path, mode='r+b') as stream:
        allData = stream.read()

        ColouredText("What chapters do you want to complete?(1-9)\n1.&Empire of cats chapter 1&\n2.&Empire of cats chapter 2&\n3.&Empire of cats chapter 3&\n4.&Into the future chapter 1&\n5.&Into the future chapter 2&\n6.&Into the future chapter 3&\n7.&Cats of the cosmos chapter 1&" +
        "\n8.&Cats of the cosmos chapter 2&\n9.&Cats of the cosmos chapter 3&\n10.&All chapters&", "White", "Cyan")
        choice = int(input())
        # Starting position of stage cleared flags
        startPos = 946
        # Length of each chapter's stage cleared flags, 16 0x00 bytes separate each chapter
        blockLen = (47 * 4) + 16
        # Position of total number of stages cleared
        lvlCountPos = 906
        # All chapters
        if choice == 10:
            # Set stages to be cleared
            for j in range(10):
                for i in range(48):
                    stream.seek(startPos + (i * 4))
                    stream.write((2).to_bytes(1, "little"))
                startPos += blockLen
            # Set total number of stages cleared
            for i in range(9):
                stream.seek(lvlCountPos + (i * 4))
                stream.write((48).to_bytes(1, "little"))
        elif choice < 10:
            if choice > 3:
                choice += 1
            # Set start point to correct chapter
            startPos += (choice - 1) * blockLen
            # Set stages to be cleared
            for i in range(48):
                stream.seek(startPos + (i * 4))
                stream.write((3).to_bytes(1, "little"))
            # Set total number of stages cleared
            stream.seek(lvlCountPos + ((choice - 1) * 4))
            stream.write((48).to_bytes(1, "little"))
        else:
            print("Please enter a recognised number")
            Stage(path)
