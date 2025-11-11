'''
For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
'''

# Read the games.txt file
# Iterate through it and put it into a dictionary? or a list?
# If red cube > 12 and green cube > 13 and blue cube > 14 then the game is impossible



# Initialize cube limits
# Initialize possible_games list

limits_dict = {
    "red": 12,
    "green": 13,
    "blue": 14
    }

possible_games = list()

with open('2023/Day2/games.txt') as f:
    games = f.read().splitlines()

for line in (games):
    gameid, data = line.split(":", 1)   # Separates gameid and the data to two separate lists
    gid = int(gameid.split()[1])
    isValid = True

    for piece in data.replace(";", ",").split(","):    # Get rid of the ";" character and split into a list
        piece = piece.strip()   # Remove redundant white spaces

        if not piece:
            continue
        num_str, color = piece.split(maxsplit=1) # Make two lists "num_str" and "color"
        num = int(num_str) # Convert the string to int

        if num > limits_dict[color]:
            #print(f"{num} is too much of {color} cubes in {gameid}")   # Test printing
            isValid = False
            break
    if isValid:
        possible_games.append(gid)


total = sum(possible_games)
print(total)