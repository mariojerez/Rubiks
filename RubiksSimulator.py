import numpy as np

class Rubiks27:

    def __init__(self):
      self.front = [['w','w','w'],['w','w','w'],['w','w','w']]
      self.right = [['b','b','b'],['b','b','b'],['b','b','b']]
      self.left = [['g','g','g'],['g','g','g'],['g','g','g']]
      self.top = [['o','o','o'],['o','o','o'],['o','o','o']]
      self.back = [['y','y','y'],['y','y','y'],['y','y','y']]
      self.bottom = [['r','r','r'],['r','r','r'],['r','r','r']]
      self.tempFace = [[None,None,None],[None,None,None],[None,None,None]]

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

    def returnCube(self):
      return {"front":self.front, "right":self.right, "left":self.left, "top":self.top, "back":self.back, "bottom":self.bottom}
    
    # Sets the cells of the column in self.tempFace to be what the cells were of the row in the actual face
    def row_to_column(self,faceName,rowNum,colNum):
      row = self.returnCube()[faceName][rowNum]
      for i in range(3):
        cell = row[i]
        self.tempFace[i][colNum] = cell

    def column_to_row(self,faceName,colNum,rowNum):
      col = []
      for i in range(3):
        col.append(self.returnCube()[faceName][i][colNum])
      self.tempFace[rowNum] = col
      

    def resetTempFace(self):
      self.tempFace = [[None,None,None],[None,None,None],[None,None,None]]

    def cloneCube(self):
      clone = Rubiks27()
      for faceName in self.returnCube():
        for rowNum in range(3):
          for colNum in range(3):
            clone.returnCube()[faceName][rowNum][colNum] = self.returnCube()[faceName][rowNum][colNum]
      return clone
          

      clone.front = self.front
      clone.right = self.right
      clone.left = self.left
      clone.back = self.back
      clone.top = self.top
      clone.bottom = self.bottom
      return clone


    def front_clockwise(self):
      temp = self.cloneCube() # make changes to temp
      # update front face 
      ### row 0 becomes column 2
      self.row_to_column('front',0,2)
      ### row 1 becomes column 1
      self.row_to_column('front',1,1)
      ### row 2 becomes column 0
      self.row_to_column('front',2,0)

      temp.front = self.tempFace
      self.resetTempFace()

      # update right face
      ### row 2 of top face becomes row 2 of right format
      row2Top = self.top[2]
      for i in range(3):
        temp.right[i][0] = row2Top[i]

      # update left face 
      ### row 0 of bottom becomes column 3 of left face
      self.tempFace = self.cloneCube().left
      self.row_to_column('bottom',0,2)
      temp.left = self.tempFace
      self.resetTempFace()

      # update top face 
      ### col 2 of left face becomes row 2 of top face
      self.tempFace = self.cloneCube().top
      self.column_to_row("left",2,2)
      temp.top = self.tempFace
      self.resetTempFace()

      # update bottom face 
      ### column 0 of right face becomes row 0 of bottom face
      self.tempFace = self.cloneCube().bottom
      self.column_to_row("right",0,0)
      temp.bottom = self.tempFace
      self.resetTempFace()

      self.front = temp.front
      self.right = temp.right
      self.left = temp.left
      self.top = temp.top
      self.bottom = temp.bottom


