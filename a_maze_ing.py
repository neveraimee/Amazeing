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
    try:
        width = int(config_settings.get("WIDTH", "0")) #use a 0 to avoid a crash if no width/height available
        height = int(config_settings.get("HEIGHT", "0"))
        print(f"Converted width: {width} (Type: {type(width)})") #type class will display the data type
        print(f"Converted height: {height} (Type: {type(height)})")
    except ValueError as e:
        print("Error: WIDTH and HEIGHT must be of interger type")
        return



if __name__ == "__main__":
    main()

    
    