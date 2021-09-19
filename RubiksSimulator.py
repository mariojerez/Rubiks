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
        print('invalid face name. Must be a color like "blue"')
      

    def returnCube(self):
      return {"white":self.white, "blue":self.blue, "green":self.green, "orange":self.orange, "yellow":self.yellow, "red":self.red}
    
    # Sets the cells of the column in self.tempFace to be what the cells were of the row in the actual face
    def row_to_column(self,faceName,rowNum,colNum):
      face = self.orientation[faceName]
      row = face[rowNum]
      for i in range(3):
        cell = row[i]
        self.tempFace[i][colNum] = cell

    def column_to_row(self,faceName,colNum,rowNum):
      face = self.orientation[faceName]
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
          

      clone.white = self.white
      clone.blue = self.blue
      clone.green = self.green
      clone.yellow = self.yellow
      clone.orange = self.orange
      clone.red = self.red
      return clone


    def clockwise(self,frontFace):
      self.updateOrientation(frontFace)
      temp = self.cloneCube() # make changes to temp cube
      temp.updateOrientation(frontFace)
      clone = self.cloneCube() # for reference
      clone.updateOrientation(frontFace)
      # update front face 
      ### row 0 becomes column 2
      self.row_to_column('front',0,2)
      ### row 1 becomes column 1
      self.row_to_column('front',1,1)
      ### row 2 becomes column 0
      self.row_to_column('front',2,0)

      temp.orientation["front"] = self.tempFace
      self.resetTempFace()

      # update right face
      ### row 2 of top face becomes row 2 of right format
      row2Top = self.orientation["top"][2]
      for i in range(3):
        temp.orientation["right"][i][0] = row2Top[i]

      # update left face 
      ### row 0 of bottom becomes column 3 of left face
      self.tempFace = clone.orientation["left"]
      self.row_to_column('bottom',0,2)
      temp.left = self.tempFace
      self.resetTempFace()

      # update top face 
      ### col 2 of left face becomes row 2 of top face
      self.tempFace = clone.orientation["top"]
      self.column_to_row("left",2,2)
      temp.top = self.tempFace
      self.resetTempFace()

      # update bottom face 
      ### column 0 of right face becomes row 0 of bottom face
      self.tempFace = clone.orientation["bottom"]
      self.column_to_row("right",0,0)
      temp.orientation["bottom"] = self.tempFace
      self.resetTempFace()

      self.white = temp.white
      self.blue = temp.blue
      self.green = temp.green
      self.orange = temp.orange
      self.red = temp.red
      self.yellow = temp.yellow
