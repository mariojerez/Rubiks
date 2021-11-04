'''
To try out the cube:
>cube = Rubiks3()
>print(cube)
>cube.clockwise("white") #or some other color
>print(cube)

Note: The side color of a cube side is defined by the color of the center cell on that side
'''
class Rubiks3:

    def __init__(self):
      self.white = [['w','w','w'],['w','w','w'],['w','w','w']]
      self.blue = [['b','b','b'],['b','b','b'],['b','b','b']]
      self.green = [['g','g','g'],['g','g','g'],['g','g','g']]
      self.orange = [['o','o','o'],['o','o','o'],['o','o','o']]
      self.yellow = [['y','y','y'],['y','y','y'],['y','y','y']]
      self.red = [['r','r','r'],['r','r','r'],['r','r','r']]
      self.tempFace = [[None,None,None],[None,None,None],[None,None,None]]
      self.orientation = {"front":self.white, "right":self.blue, "left":self.green, "back": self.yellow, "top":self.orange, "bottom":self.red}

    def __str__(self):
      cube = self.returnCube()
      cubeString = ""
      for sideName in cube:
        cubeString += sideName + '\n'
        side = ""
        for row in cube[sideName]:
          for cell in row:
            side += cell + '\t'
          side += '\n'
        side += '\n'
        cubeString += side
      return cubeString

    def updateOrientation(self, frontName):
      if frontName == "white":
        self.orientation = {"front":self.white, "right":self.blue, "left":self.green, "back": self.yellow, "top":self.orange, "bottom":self.red}

      elif frontName == "blue":
        self.orientation = {"front":self.blue, "right":self.yellow, "left":self.white, "back": self.green, "top":self.orange, "bottom":self.red}

      elif frontName == "green":
        self.orientation = {"front":self.green, "right":self.white, "left":self.yellow, "back": self.blue, "top":self.orange, "bottom":self.red}
      elif frontName == "yellow":
        self.orientation = {"front":self.yellow, "right":self.green, "left":self.blue, "back": self.white, "top":self.orange, "bottom":self.red}
      elif frontName == "orange":
        self.orientation = {"front":self.orange, "right":self.blue, "left":self.green, "back": self.red, "top":self.yellow, "bottom":self.white}
      elif frontName == "red":
        self.orientation = {"front":self.red, "right":self.blue, "left":self.green, "back": self.orange, "top":self.white, "bottom":self.yellow}
      else:
        print('invalid face name. Must be either "white", "blue", "orange", "green", "yellow", or "red".')
      

    def returnCube(self):
      return {"white":self.white, "blue":self.blue, "green":self.green, "orange":self.orange, "yellow":self.yellow, "red":self.red}
    
    # Sets the cells of the column in self.tempFace to be what the cells were of the row in the actual face
    def row_to_column(self,faceName,rowNum,colNum,referenceCube):
      face = referenceCube.orientation[faceName]
      row = face[rowNum]
      for i in range(3):
        cell = row[i]
        self.tempFace[i][colNum] = cell

    def column_to_row(self,faceName,colNum,rowNum,referenceCube):
      face = referenceCube.orientation[faceName]
      col = []
      for i in range(3):
        col.append(face[i][colNum])
      self.tempFace[rowNum] = col
      
    def resetTempFace(self):
      self.tempFace = [[None,None,None],[None,None,None],[None,None,None]]

    def cloneCube(self):
      clone = Rubiks3()
      for faceName in self.returnCube():
        for rowNum in range(3):
          for colNum in range(3):
            clone.returnCube()[faceName][rowNum][colNum] = self.returnCube()[faceName][rowNum][colNum]
      return clone

    def updateSidesFrontOrientation(self):
      self.white = self.orientation[self.whereIs("w")]
      self.blue = self.orientation[self.whereIs("b")]
      self.green = self.orientation[self.whereIs("g")]
      self.orange = self.orientation[self.whereIs("o")]
      self.red = self.orientation[self.whereIs("r")]
      self.yellow = self.orientation[self.whereIs("y")]

    def whereIs(self, color_char):
      for side in self.orientation:
        if self.orientation[side][1][1] == color_char:
          return side

    def whatColorIs(self, sideName):
      side = self.orientation[sideName]
      color = side[1][1]
      if color == 'w':
        color = "white"
      elif color == 'o':
        color = "orange"
      elif color == 'b':
        color = "blue"
      elif color == 'g':
        color = "green"
      elif color == 'y':
        color = "yellow"
      elif color == 'r':
        color = "red"
      return color


    ## Sets the side specified to self.tempFace or some other face user inputs
    def updateSide(self, sideName, referenceSide="tempFace"):
      if referenceSide == "tempFace":
        referenceSide = self.tempFace
      if sideName == "white":
        for c in range(3):
          for r in range(3):
            self.white[c][r] = self.tempFace[c][r]
        
      elif sideName == "orange":
        for c in range(3):
          for r in range(3):
            self.orange[c][r] = self.tempFace[c][r]
      elif sideName == "blue":
        for c in range(3):
          for r in range(3):
            self.blue[c][r] = self.tempFace[c][r]
      elif sideName == "green":
        for c in range(3):
          for r in range(3):
            self.green[c][r] = self.tempFace[c][r]
      elif sideName == "yellow":
        for c in range(3):
          for r in range(3):
            self.yellow[c][r] = self.tempFace[c][r]
      elif sideName == "red":
        for c in range(3):
          for r in range(3):
            self.red[c][r] = self.tempFace[c][r]

    def clockwise(self,frontFace):
      self.updateOrientation(frontFace)
      reference = self.cloneCube()
      reference.updateOrientation(frontFace)

      # Update front face
      ### row 0 becomes column 2
      self.row_to_column('front',0,2,reference)
      ### row 1 becomes column 1
      self.row_to_column('front',1,1,reference)
      ### row 2 becomes column 0
      self.row_to_column('front',2,0,reference)
      self.updateSide(self.whatColorIs("front"))


      # update right face
      ### row 2 of top face becomes col 0 of right face 
      self.tempFace = reference.cloneCube().orientation["right"]
      row = reference.orientation["top"][2]
      for i in range(3):
        self.tempFace[i][0] = row[i]
      self.updateSide(self.whatColorIs("right"))
      
      

      # update left face 
      ### row 0 of bottom becomes column 2 of left face
      self.tempFace = reference.cloneCube().orientation["left"]
      self.row_to_column('bottom',0,2,reference)
      self.updateSide(self.whatColorIs("left"))

      # update top face 
      ### col 2 of left face becomes row 2 of top face
      self.tempFace = reference.cloneCube().orientation["top"]
      self.column_to_row("left",2,2,reference)
      self.updateSide(self.whatColorIs("top"))
      

      # update bottom face 
      ### column 0 of right face becomes row 0 of bottom face
      self.tempFace = reference.cloneCube().orientation["bottom"]
      self.column_to_row("right",0,0,reference)
      self.updateSide(self.whatColorIs("bottom"))
      

    def deriveScore(self):
      cubeDictionary = self.returnCube()
      points = 0
      for faceName in cubeDictionary:
        face = cubeDictionary[faceName]
        for row in face:
          for cell in row:
            if cell == cubeDictionary[faceName][1][1]:
              points += 1
      return points
