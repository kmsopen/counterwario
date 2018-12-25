import pygame
import sys
import cwplayer
import cwenemy
import cwfield
import cwcamera

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
    self.camera = cwcamera.Camera(0,0,640,480)
    
    self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
    
    self.STATE_INIT = 0
    self.STATE_MAIN_MENU = 1
    self.STATE_GAME = 2
    self.state = self.STATE_INIT
    
    self.players = []  # TODO: class Player
    self.enemies = []  # TODO: class Enemy
    self.fields = []  # TODO: class Field
    # battlefield will be array of strings
    self.battlefield = [] 
    self.FIELD_SIZE = 30  # px
    
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
          self.exit()
        # key down
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pass
        # key up
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_ESCAPE:
            self.exit()
          if event.key == pygame.K_5 \
          and self.state == self.STATE_MAIN_MENU:
            self.exit()
          if event.key == pygame.K_1 \
          and self.state == self.STATE_MAIN_MENU:
            self.num_players = 1
            self.startLevel("level_test")
          if event.key == pygame.K_2 \
          and self.state == self.STATE_MAIN_MENU:
            self.num_players = 2
            self.startLevel("level_test")       
            
          # HACK test camera
          if event.key == pygame.K_LEFT:
            self.camera.x -= 1
          if event.key == pygame.K_RIGHT:
            self.camera.x += 1
          
            
      # processing
      pass
    
      # drawing
      
      self.screen.fill(self.BLACK)
      for i in self.images:
        tmp_rect = i[1]  # TODO maybe something wrong
        tmp_rect.left -= self.camera.x
        tmp_rect.bottom -= self.camera.y  # TODO test, maybe vise versa
        
        #self.screen.blit(i[0], i[1])
        self.screen.blit(i[0], tmp_rect)
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
    
  
  def startLevel(self, level_name):
    print('Game start level', level_name)
    
    self.camera.move(0,0)
    
    self.battlefield = []
    
    # open map file
    map_started = False
    map_file_name = "maps/" + level_name + ".map"
    print("Opening map file", map_file_name)
    with open(map_file_name, "r") as fm:
      for line in fm:
        print(line)
        if line.startswith("START"):
          map_started = True
        elif line.startswith("END"):
          map_started = False
        else:
          if map_started:    # read map to battlefield
            self.battlefield.append(line)

    # clear images
    self.images = []  # clear list

    # create game objects
    self.enemies = []  # clear list
    self.fields = []  # clear list
    x = 0
    y = 15
    for line in self.battlefield:
      x = 0
      for symbol in line:
        # field
        #if symbol in (" ","H","1","2","3","4"\
        #  ,"5","6","7","8","9","0","G","B","P","C"): 
        f = cwfield.Field(x,y,symbol)
        self.fields.append(f)
          
        image = pygame.image.load('images/' + f.image_name)
        image_rect = image.get_rect()
        image_rect.top = self.FIELD_SIZE * (15-f.y)
        image_rect.left = self.FIELD_SIZE * f.x
        #image_rect.right = self.FIELD_SIZE * (f.x + 1) 
        #image_rect.bottom = self.FIELD_SIZE * (15-f.y + 1) 
        self.images.append((image, image_rect))

        # enemy?
        if symbol in ("1","2","3","4"\
          ,"5","6","7","8","9","0"):  
          e = cwenemy.Enemy(x,y,symbol)
          self.enemies.append(e)
        
        #TODO: hero?
        
        x += 1  
      y -= 1
    # change state of game
    self.state = self.STATE_GAME
  
  def exit(self):
    print('Game exit')
    sys.exit()
  
  
print('game module loaded')
