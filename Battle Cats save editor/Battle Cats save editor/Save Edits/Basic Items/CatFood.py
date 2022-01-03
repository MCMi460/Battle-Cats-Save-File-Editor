answer = input("Warning, editing cat food at all can get you banned after a few days, would you like to continue? (yes/no):")
if answer.lower() == "no":
    return
stream = io.open(path, mode='rb')

catfoodB = []
Position = 7
allData = stream.read()
stream.close()

catfoodB.append(allData[Position])
print(f'{int(catfoodB)} ketfud')
