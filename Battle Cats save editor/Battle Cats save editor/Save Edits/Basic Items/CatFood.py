def catFood(path):
    answer = input("Warning, editing cat food at all can get you banned after a few days, would you like to continue? (yes/no):")
    if answer.lower() == "no":
        return
    stream = io.open(path, mode='rb')

    stream.seek(7)
    catfoodB = stream.read(4)
    stream.close()

    CatFood = int.from_bytes(catfoodB, "little")
    print(f'You have {CatFood} cat food')

    print("How much cat food do you want?(max 45000, but I recommend below 20k, to be safe")

    CatFood = int(input())
    if CatFood > 45000:
        CatFood = 45000
    elif CatFood < 0:
        CatFood = 0

    bytes = (CatFood).to_bytes(2, "little")

    stream = io.open(path, mode='r+b')
    stream.seek(7 + 2)
    allData = bytes + stream.read()
    stream.seek(7)
    stream.write(allData)
    stream.close()
    print(f"Set Cat food to {CatFood}")
