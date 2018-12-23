import pygame
import sys

class Game:
  '''
  Class of game window
  '''
  
  def __init__(self):
    print('Game init')
    self.SCREEN_SIZE = self.SCREEN_H, self.SCREEN_W = 640, 480
    self.DELAY = 10  # 100fps :)
    self.BLACK = (0,0,0)
    self.images = []  # pygame images to draw
    
    self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
    
    self.STATE_INIT = 0
    self.STATE_MAIN_MENU = 1
    self.STATE_GAME = 2
    self.state = self.STATE_INIT
    
  def run(self):
    '''
    run game window cycle
    '''
    print('Game run')
    
    self.mainMenu()
    
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
          if event.key == pygame.K_5 \
          and self.state == self.STATE_MAIN_MENU:
            sys.exit()
      
      # processing
      pass
    
      # drawing
      self.screen.fill(self.BLACK)
      for i in self.images:
        self.screen.blit(i[0], i[1])
      pygame.display.flip()
      
      # timer      
      pygame.time.delay(self.DELAY)
  
  def mainMenu(self):
    self.state = self.STATE_MAIN_MENU
    print('Game main menu')
    pass
    img_menu = pygame.image.load("images/mainmenu.png")
    img_menu_rect = img_menu.get_rect()
    self.images.append((img_menu, img_menu_rect))
    
  
  def start(self):
    print('Game start')
    pass
  
  def exit(self):
    print('Game exit')
    pass
  
  
print('game module loaded')
