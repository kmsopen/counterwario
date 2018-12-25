class Field:
  
  def __init__(self,x,y,symbol):
    self.x = x
    self.y = y
    self.symbol = symbol
    self.image_name = "field_sky.png"
    if symbol == "B":
      self.image_name = "field_bricks.png"
    if symbol == "C":
      self.image_name = "field_clouds.png" 
    if symbol == "G":
      self.image_name = "field_ground.png"
    if symbol == "P":
      self.image_name = "field_pipe.png"
    if symbol == "L":
      self.image_name = "field_lava.png"      
    if symbol == "M":
      self.image_name = "field_bridge.png"        
    if symbol == "S":
      self.image_name = "field_secret.png"   