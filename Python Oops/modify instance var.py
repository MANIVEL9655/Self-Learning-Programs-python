class University:
    name = "Madras Univerisity"

    def __init__(self):
        pass
antoObj = University()
kamalObj = University()

print(antoObj.name)
print(kamalObj.name)

print("----------------")
print(University.name)
antoObj.name = "Kamaraj University"
print(antoObj.name)
print(kamalObj.name)