import os
import sys

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
    maze_grid = [["#" for i in range(width)] for i in range(height)]
    print(f"Maze grid created with {width} columns and {height} rows")

    if width > 0 and height > 0:
        print(f"First row: {maze_grid[0]}")




    # PARSING ENTRY AND EXIT POINTS
    entry_str = config_settings.get("ENTRY", "0,0")
    entry_x, entry_y = map(int, entry_str.split(","))
    #^map function is like a stamp apply x to x amount of x

    exit_str = config_settings.get("EXIT", "19,14") #20,15
    exit_x, exit_y = map(int, exit_str.split(","))

    print(f"Entry point set: X = {entry_x} Y = {entry_y}")
    print(f"Exit point set: X = {exit_x} Y = {exit_y}")


    #MARKING COORDINATES
    maze_grid[entry_y][entry_x] = "S" #Start
    maze_grid[exit_y][exit_x] = "E" #Exit


    print()
    print("=== Maze preview ===")
    for row in maze_grid:
        print(" ".join(row))





if __name__ == "__main__":
    main()

    
    