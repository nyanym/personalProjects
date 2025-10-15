# (0,0) is at the top left of the grid
import random


def printGrid(array):  # makes grid from array
    grid = ""
    for row in range(len(array)):
        for col in range(len(array[row])):
            grid += str(array[row][col]) + " "
        grid += "\n"
    return grid


def checkwin():
    return spacesrevealed == height*width-numbombs


def checksurroundingbombs():
    bombs = 0
    possibledirections = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
    for x, y in possibledirections:
        changedx = xcoord + x
        changedy = ycoord + y
        if [changedx, changedy] in bombcoords:
            bombs += 1
    return bombs


while True:
    # prints grid
    array = []
    height = int(input("Height of grid?: "))
    width = int(input("Width of grid?: "))

    def createarray():
        for row in range(height):
            gridrow = []
            for col in range(width):
                gridrow.append("X")
            array.append(gridrow)
        return array
    array = createarray()
    print("\n"+printGrid(array))

# logic for bombs
    bombcoords = []
    numbombs = int(input("How many bombs?: "))
    if 0 > numbombs > height*width:
        print(f"Please input a valid number of bombs (between 0 to {height*width}).")
        continue

    def bombs(numbombs):
        for i in range(numbombs):
            bombx = random.randint(0, width-1)
            bomby = random.randint(0, height-1)
            while [bombx, bomby] in bombcoords:
                bombx = random.randint(0, width-1)
                bomby = random.randint(0, height-1)
            bombcoords.append([bombx, bomby])
        return bombcoords
    bombcoords = bombs(numbombs)
    # print("\n"+str(bombs(numbombs)))

# checks which coords r safe
    safecoords = []

    def safe():
        for row in range(height):
            for col in range(width):
                if [row, col] not in bombcoords:
                    safecoords.append([row, col])
                    continue
        return safecoords
    safecoords = safe()
    # print("\n"+str(safe()))

# Check win
    spacesrevealed = 0
# game
    while True:
        print()
        if checkwin():
            print("\n"+"You Win!"+"\n")
            break
        xcoord = int(input(f"Give me an x-coordinate from 0 to {width-1}: "))  # xcoord works fine
        if xcoord not in range(width):
            print("\n"+"Please enter a value within the valid range.")
            continue
        ycoord = int(input(f"Give me an y-coordinate from 0 to {height-1}: "))  # ycoord is opposite
        if ycoord not in range(height):
            print("\n"+"Please enter a value within the valid range.")
            continue
        # checks if bomb
        if [xcoord, ycoord] in bombcoords:
            array[ycoord][xcoord] = "💥"  # is there less ugly character?
            print("\n" + printGrid(array))
            print("You Lose!"+"\n")
            break
        # checks if safe
        elif [xcoord, ycoord] in safecoords:
            bombs = checksurroundingbombs()
            array[ycoord][xcoord] = bombs
            print("\n" + printGrid(array))
            spacesrevealed += 1
            if checkwin():
                print("\n"+"You Win!"+"\n")
                break
# restarting
    restart = input("Restart? [y/n]: ")
    if restart == "y":
        print()
        continue
    else:
        break
print("\n"+"Game Stopped")
