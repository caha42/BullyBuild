"""
Calculates which boards I need to build a stable box.
"""
# Sketch of box
#----------------------------------------
#   |               |                |
#   |               |                |
#   |               |                |
#   ----------------------------------

# Type 1: Back is completely in the box
# Type 2: Back is between top and bottom
# Type 3: Back is outside of the box, except top

# Definitions
roof_width = 132.5
width = 119.5
height = 50
depth = 63  # TODO check, inside was 61.5
board_gauge = 1.2

type = 2

top = (roof_width, depth)
if type == 1:
    bottom = (width, depth)
    back = (width - 2*board_gauge, height-2*board_gauge)
    sides = (height - 2*board_gauge, depth)
    vertical_support = (height - 2*board_gauge, depth-board_gauge)
elif type == 2:
    bottom = (width, depth)
    back = (width, height-2*board_gauge)
    sides = (height - 2*board_gauge, depth-board_gauge)
    vertical_support = (height - 2*board_gauge, depth-board_gauge)
elif type == 3:
    bottom = (width, depth-board_gauge)
    back = (width, height-board_gauge)
    sides = (height - 2*board_gauge, depth-board_gauge)
    vertical_support = (height - 2*board_gauge, depth-board_gauge)

print(top)
print(bottom)
print(back)
print(sides)
print(sides)
print(vertical_support)