import pygame

class Game:
  '''
  Class of game window
  '''
  
  def __init__(self):
    print('Game init')
    self.SCREEN_SIZE = self.SCREEN_H, self.SCREEN_W = 640, 480
    self.DELAY = 10 # 100fps :)
    
    self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
  
  def run(self):
    '''
    run game window cycle
    '''
    print('Game run')
    while True:
      pass
      
      pygame.time.delay(self.DELAY)
  
  def mainMenu(self):
    print('Game main menu')
    pass
  
  def start(self):
    print('Game start')
    pass
  
  def exit(self):
    print('Game exit')
    pass
  
  
print('game module loaded')
