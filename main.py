import sys
 
import pygame
from pygame.locals import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
x, y = 320, 450
movingLeft = False
movingRight = False
 
# Game loop.
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_DOWN:
        y += 10
      if event.key == K_UP:
        y -= 10
      if event.key == K_LEFT:
        movingLeft = True
      if event.key == K_RIGHT:
        movingRight = True
    if event.type == MOUSEMOTION:
      x=event.pos[0]
      y=event.pos[1]
      print(event)
  # Update.
  if movingLeft:
   x -= 1
  if movingRight:
   x +=1
 
  # Draw.
  screen.fill((255, 255, 255))
  pygame.draw.circle(
    screen,
    (0, 255, 0),
    (x, y),
    20
  )

 
  pygame.display.flip()
  fpsClock.tick(fps)
