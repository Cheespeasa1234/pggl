from __future__ import annotations
import random
import pygame
WIDTH = 800
HEIGHT = 500

def darken(color: tuple) -> tuple:
  r,g,b = color
  r -= 10 if r > 10 else 0
  g -= 10 if g > 10 else 0
  b -= 10 if b > 10 else 0
  return (r, g, b)

class Sprite:
  def __init__(self, x, col):
    self.x = x
    self.w = 40
    self.h = 100
    self.y = HEIGHT - self.h
    self.col = col
  def collides_with(self, sprite: Sprite) -> bool:
    return self.hitbox().colliderect(sprite.hitbox())
  def draw(self, pygame: pygame, screen: pygame.Surface) -> None:
    pygame.draw.rect(screen, self.col, (self.x, self.y, self.w, self.h))
  def update(self, speed):
    self.x -= speed
  def hitbox(self) -> pygame.Rect:
    return pygame.Rect(self.x, self.y, self.w, self.h)
class Enemy(Sprite):
  def __init__(self):
    self.x = WIDTH - 40
    if random.randint(0,1) == 0:  # cactus 
      self.w = 30 + 10 * random.randint(1, 3)
      self.h = 60 + 10 * random.randint(0, 3)
      self.y = 0 + self.h
    else:                         # bird
      self.w = 30
      self.h = 20
      self.y = 0 + 10 * random.randint(2, 8)
    self.col = (255, 0, 0)
  
  def draw(self, pygame: pygame, screen: pygame.Surface) -> None:
    pygame.draw.rect(screen, self.col, (self.x, self.y, self.w, self.h))
  def update(self, speed):
    self.x -= speed
    if self.x < 0:
      return -1
    return 0
class Controllable:
  def UP_PRESSED(self, event: pygame.event) -> None:
    pass
  def DOWN_PRESSED(self, event: pygame.event) -> None:
    pass
  def UP_RELEASED(self, event: pygame.event) -> None:
    pass
  def DOWN_RELEASED(self, event: pygame.event) -> None:
    pass

class Player(Sprite, Controllable):

  # Constructor
  def __init__(self):
    self.x, self.y = 20, 0
    self.w, self.h = 40, 100
    self.dy = 0
    self.ddy = 1
    self.up = False
    self.used_jump = False
    self.ducking = False
    self.col = (0, 255, 100)

  # Controller
  def UP_PRESSED(self, event): 
    self.up = True
  def UP_RELEASED(self, event):
    self.up = False
  def DOWN_PRESSED(self, event):
    self.ducking = True
  def DOWN_RELEASED(self, event):
    self.ducking = False

  # Main method abstractors
  # Draw every frame
  def draw(self, pygame: pygame, screen: pygame.Surface) -> None:
    pygame.draw.rect(screen, self.col, (self.x, self.y, self.w, self.h))

  # Update every couple of frames
  def update(self, speed):
    airborne = self.y + self.h + self.dy <= HEIGHT
    jumping = self.up and abs(self.y) > 200

    # if jumping and have not used jump: set self.dy
    if jumping and not self.used_jump:
      self.dy = -10
    # otherwise, set jump to used
    else:
      self.used_jump = True
      self.ddy = 1

    # if ducking and on ground:
    if self.ducking and not airborne:
      self.h = 50
    else:
      self.h = 100

    # if not on ground:
    if airborne:
      # move sprite
      self.y += self.dy
      # gravity
      self.dy += self.ddy
    # if on ground:
    else:
      # move to bottom of screen
      self.y = HEIGHT - self.h
      # set dy to 0
      self.dy = 0
      self.ddy = 0
      # unuse jump
      self.used_jump = False