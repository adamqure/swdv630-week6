class Dishwasher():
    def wash(self):
        print("Dishes Clean")

class Laundromat():
    def washClothes(self):
        print("Clothes Washed")
        print("Clothes Folded")

class MessCleaner():
    def pickUpKidsToys(self):
        print("Kids toys picked up")

    def sweepFloor(self):
        print("Floor Swept")

    def mopFloor(self):
        print("Floor Mopped")

class HouseCleaner():
    def cleanHouse(self):
        Dishwasher().wash()
        Laundromat().washClothes()
        MessCleaner().pickUpKidsToys()
        MessCleaner().sweepFloor()
        MessCleaner().mopFloor()

def main():
    HouseCleaner().cleanHouse()
    print("House All Clean")

main()