
from copy import copy, deepcopy
from MAPS import BLOCK


def remove_robot_map(map):
    map = deepcopy(map)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == BLOCK.ROBOT:
                map[y][x] = BLOCK.ROAD
    return map

def add_agent_to_map(agents, static_map):
    full_map = deepcopy(static_map)
    # check if robot not above diamon
    for ag in agents.values():
        if len(ag) > 0:
            for a in ag:
                y, x, t = a
                if full_map[y][x] == BLOCK.GOAL and t == BLOCK.DIAM:
                    full_map[y][x] = BLOCK.DIAM_ON_GOAL
                else:
                    full_map[y][x] = t

    # y, x, t = agents['robot']
    # full_map[y][x] = t

    return full_map

def parse_map(imap):
    map = deepcopy(imap)

    diam_on_goals = []
    diams = []
    goals = []
    agents = {'diam_on_goals': [],
             'diams': [],
             'robot': []}

    for y in range(len(map)):
        for x in range(len(map[y])):

            if map[y][x] == BLOCK.ROBOT:
                agents['robot'].append((y, x, BLOCK.ROBOT))
                map[y][x] = BLOCK.ROAD

            elif map[y][x] == BLOCK.DIAM:
                agents['diams'].append((y, x, BLOCK.DIAM))
                map[y][x] = BLOCK.ROAD

            elif map[y][x] == BLOCK.DIAM_ON_GOAL:
                agents['diam_on_goals'].append((y, x, BLOCK.DIAM_ON_GOAL))
                map[y][x] = BLOCK.GOAL

            elif map[y][x] == BLOCK.GOAL:
                goals.append((y,x))

    return map, agents, goals

def create_final(imap: list):
    map = deepcopy(imap)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == BLOCK.ROBOT:
                map[y][x] = BLOCK.ROAD
            elif map[y][x] == BLOCK.GOAL:
                map[y][x] = BLOCK.DIAM_ON_GOAL
            elif map[y][x] == BLOCK.DIAM:
                map[y][x] = BLOCK.ROAD
    return map
