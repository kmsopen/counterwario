import pygame
import sys

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
      # events
      for event in pygame.event.get():
        # exit
        if event.type == pygame.QUIT: 
          sys.exit()
        # key down
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pass
        # key up
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_ESCAPE:
            pass
            sys.exit()
      
      # processing
      pass
    
      # drawing
      pass
    
      # timer      
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
