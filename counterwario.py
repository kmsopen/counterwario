#!/usr/bin/python3
import game
g = game.Game()
try:
  g.run()
except KeyboardInterrupt as ex:
  print(ex)
print('Exit from the game')
