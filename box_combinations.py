"""
Calculates which combination of boxes on shelves can fit in a given space regarding one dimension (i.e. height or width).
Especially useful for planning a shelf with systems like AUER Euro boxes
"""

# Definitions
space = 50
board_gauge = 1.2
wiggle_space = 1
boxes = [7.5, 12, 17, 22, 27, 32] # Heights of AUER Boxes with 40 or 30 width
possibilities = set()


def get_combination(combination):
    possible_boxes = get_possible_boxes(calculate_rest(combination))
    if not possible_boxes:
        possibilities.add(tuple([calculate_rest(combination), tuple(sorted(combination))]))
        return
    for box in possible_boxes:
        new_combination = combination.copy()
        new_combination.append(box)
        get_combination(new_combination)


def get_possible_boxes(rest):
    possible_boxes = []
    for box in boxes:
        if box + wiggle_space <= rest:  # Box needs a bit wiggle room
            possible_boxes.append(box)
    return possible_boxes


def calculate_rest(combination):
    nofboards = 2  # Top and bottom Board are always needed
    if not combination:
        nofboards += len(combination)-1  # Between two boxes, there is always a board
    rest = space - (nofboards * board_gauge)
    for box in combination:
        rest -= box + wiggle_space  # Each Box needs a bit wiggle room
    return rest


get_combination([])
for possibility in sorted(possibilities):
    print("Remaining: " + str(round(possibility[0], 1)) + " - " + str(possibility[1]))