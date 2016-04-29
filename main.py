node = Node(2, 3)
print(str(node.x) +" - " + str(node.y))

class Field:
    BLACK = 0
    WHITE = 1
    EMPTY = -1

class Node:
    x = None
    y = None
    field = Field.EMPTY
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PlayfieldNode(Node):
    # Compass:
    #     NW    NE
    #
    # E    self     W
    #
    #     SW   SE
    northWest = None
    northEast = None
    east = None
    southEast = None
    southWest = None
    west = None


    #def addStone
