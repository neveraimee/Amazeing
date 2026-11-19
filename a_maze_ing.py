import os
import sys
import random

#OPENING THE CELL
NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8 


def open_north(grid, x, y) -> None:
    grid[y][x] -= NORTH
    grid[y - 1][x] -= SOUTH 

def open_east(grid, x, y) -> None:
    grid[y][x] -= EAST
    grid[y][x + 1] -= WEST

def open_south(grid, x, y) -> None:
    grid[y][x] -= SOUTH
    grid[y + 1][x] -= NORTH

def open_west(grid, x, y) -> None:
    grid[y][x] -= WEST
    grid[y][x - 1] -= EAST


#check if neighbouring cells exists!!!! will it fall off the grid
def get_neighbours(x, y, width, height) -> list[tuple[int, int]]: #list of whole number pairs
    neighbours = []
    if y - 1 >= 0:
        neighbours.append((x, y - 1)) #append takes one thing so (()) N
    if x + 1 < width:
        neighbours.append((x + 1, y)) # E
    if y + 1 < height:
        neighbours.append((x, y + 1)) # S
    if x - 1 >= 0:
        neighbours.append((x - 1, y)) # W
    return neighbours




def open_passage(grid, x, y, nextx, nexty) -> None: 
    if nexty == y - 1:
        open_north(grid, x, y)
    elif nextx == x + 1:
        open_east(grid, x, y)
    elif nexty == y + 1:
        open_south(grid, x, y)
    elif nextx == x - 1:
        open_west(grid, x, y)        






#program must run with: python3 a_maze_ing.py config.txt
def main() -> None:
    if len(sys.argv) < 2:
        print("Error: Please run with 'python3 a_maze_ing.py config.txt'")
        return

    config_filename = sys.argv[1]

    #checking the config file exists (incase someone passes a bs name)
    if not os.path.exists(config_filename):
        print(f"Error: The file '{config_filename}' could not be found")
        return

    #parsing the config file
    print(f"Reading the configuration from {config_filename}...")

    config_settings = {}

    with open(config_filename, "r") as inthefile: #read the config file
        for line in inthefile:
            line = line.strip() #removes whitespace
            if not line or line.startswith("#"): #if the line is empty or a comment
                continue 

            if "=" in line: #we want to split on the = to seperate width from 20
                key, value = line.split("=", 1) #1 incase multiple = are passed!!

                config_settings[key.strip()] = value.strip() #strip whitespace and store

    print(f"Saved settings: {config_settings}")

    #now im converting WIDTH and HEIGHT into actual intergers
    #Row = Vertical stack (Height / Y)
    #Column = Horizontal width (Width / X)
    try:
        width = int(config_settings.get("WIDTH", "0")) #use a 0 to avoid a crash if no width/height available
        height = int(config_settings.get("HEIGHT", "0"))
        print(f"Converted width: {width} (Type: {type(width)})") #type class will display the data type of width
        print(f"Converted height: {height} (Type: {type(height)})")
    except ValueError:
        print("Error: WIDTH and HEIGHT must be of interger type")
        return


    #list comprehension to build the grid
    maze_grid = [[15 for i in range(width)] for i in range(height)]
    print(f"Maze grid created with {width} columns and {height} rows")

    #set all to false "these cells have not been visted" then kill me
    visited = [[False for i in range(width)] for i in range(height)] 
    pick = random.Random(42)







    # PARSING ENTRY AND EXIT POINTS
    entry_str = config_settings.get("ENTRY", "0,0")
    entry_x, entry_y = map(int, entry_str.split(","))
    #^map function is like a stamp apply x to x amount of x

    exit_str = config_settings.get("EXIT", "19,14") #20,15
    exit_x, exit_y = map(int, exit_str.split(","))










    open_passage(maze_grid, 0, 0, 1, 0)
    options = get_neighbours(0, 0, width, height)
    print(options)
    for i in range(10):
        print(pick.choice(options))

    print()
    print("=== Maze preview ===")
    for row in maze_grid:
        print(" ".join(format(cell, "X") for cell in row))





if __name__ == "__main__":
    main()

    
    