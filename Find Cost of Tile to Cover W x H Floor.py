# Find Cost of Tile to Cover W x H Floor

def ask(cost, width, height):
    return float(cost * width * height)


print("Cost of the floor : ", ask(2, 3, 5))

