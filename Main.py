# Main Runnable file for the CE889 Assignment
# Project built by Lewis Veryard and Hugo Leon-Garza

import GameLoop

config_data = {}

def importConfigFile():
    file = open("Files/Config.con", 'r')
    for line in file:
        line_split = line.split(',')
        for indervidual in line_split:
            content = indervidual.split('=')
            config_data[content[0]] = content[1]


importConfigFile()
print(config_data)


def start_game_window():
    game = GameLoop.init()