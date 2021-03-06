class Matrix():
  grid =   ['0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0',
            'N','N','N','N','N',
            '0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0']
  shipOne = []
  shipTwo = []
  shipThree = []

playerOne = Matrix()
playerTwo = Matrix()

def lookUp(iVal, bVal):
  if iVal == 0 and bVal == 0:
    return 0 
  else:
    return (iVal*5)  + bVal

def printMatrix(player):
  for i in range(11):
    print [player.grid[lookUp(i,b)] for b in range(5)]

def updateMatrix(value, xVal, yVal, player):
  place = lookUp(yVal,xVal)  
  player.grid[place] = value

# def placeShip(player, x1,x2, y1, y2):
#   isHorizontal = False
#   isVertical = False
#   if x1 == x2:
#     isHorizontal = True
#     isVertical = False
#   elif y1 == y2:
#     isVertical = True
#     isHorizontal = False
#   else:
#     print 'Ship cannot be placed diagonally'
#   if isHorizontal == True:
#     distance = x2 - x1
#   elif isVertical == True:
#     distance = y2 - y1 
#   for i in range(distance):
#     if i == 1:
#       updateMatrix('1',x1,y1, player)
#     elif isHorizontal:
#       updateMatrix('1',(x1+1),y1, player)
#     elif isVertical:
#       updateMatrix('1',x1,(y1+1), player)
    
print 'playerOne'
printMatrix(playerOne)
print 'playerTwo'
printMatrix(playerTwo)
