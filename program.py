import time
import pygame

from sprite import Player, Enemy, WIDTH, HEIGHT


pygame.init()
pygame.display.set_caption("Dino Game")

FONT = pygame.font.Font('freesansbold.ttf', 32)

screen = pygame.display.set_mode([WIDTH, HEIGHT])

enemies, player = [], Player()

fpsClock = pygame.time.Clock()
FPS = 60
speed = 5
running = True

def draw():
  screen.fill((255, 255, 255))
  for enemy in enemies:
    enemy.draw(pygame, screen)
  player.draw(pygame, screen)

def update():
  for enemy in enemies:
    if enemy.update(speed) or (enemy.x < 200 and enemy.collides_with(player)):
      enemies.remove(enemy)

  # run statically
  player.update(speed) 

while running:

  before = round(time.time()*1000)

  # manage events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        player.UP_PRESSED(event)
      elif event.key == pygame.K_DOWN:
        player.DOWN_PRESSED(event)
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        player.UP_RELEASED(event)
      elif event.key == pygame.K_DOWN:
        player.DOWN_RELEASED(event)
      elif event.key == pygame.K_SPACE:
        enemies.append(Enemy())
  
  # draw to the screen
  draw()

  # update sprites
  update()

  after = round(time.time()*1000)

  

  pygame.display.flip()
  fpsClock.tick(FPS)

pygame.quit()