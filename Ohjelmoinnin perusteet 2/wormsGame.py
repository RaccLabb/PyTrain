def move(xDir,yDir, coords):
    coords[2] = coords[1]
    coords[1] = coords[0]
    x, y = coords[0]
    coords[0] = (x + xDir, y + yDir)
    print(coords)
    return coords

def gameOverCheck(coords):
    if coords[0] in coords[1:]:
        return True
    else:
        return False
    
def main():
    worm_coordinates = [(1,1), (1,0), (1,-1)]
    while True:
        isGameOver = gameOverCheck(worm_coordinates)
        if isGameOver:
            print("Game Over")
            break

        command = input("W = up\nS = down\nA = left\nD = right\nQ = Lopeta ohjelma \n")
        match command:
            case "w":
                worm_coordinates = move(0,1,worm_coordinates)
            case "s":
                worm_coordinates = move(0,-1,worm_coordinates)
            case "a":
                worm_coordinates = move(-1,0,worm_coordinates)
            case "d":
                worm_coordinates = move(1,0,worm_coordinates)
            case "q":
                print("Ohjelma suljetaan")
                break
            case other:
                print("Virheellinen syöte, kokeile uudestaan!")

if __name__=="__main__":
    main()
