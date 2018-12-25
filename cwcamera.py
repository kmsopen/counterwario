class Camera:
  """
  Class will be used for offsets of images in game window
  x - left offset
  y - bottom offset
  w - width
  h - height
  """
  
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    
  def move(self,x,y):
    self.x = x
    self.y = y