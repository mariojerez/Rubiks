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



    def front_clockwise(self):
      # update front face 
      ### row 0 becomes column 2
      self.row_to_column('front',0,2)


      ### row 2 becomes column 2

      ### row 3 becomes column 1

      # update right face 

      # update left face 

      # update top face 

      # update back face 

      # update bottom face 


