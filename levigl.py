from modulefinder import Module
from pygame import Surface
from typing import Tuple
from tkinter.font import Font
import pygame
from __future__ import Frame, Animation

class Frame:
  def __init__(self, img: pygame.image):
    self.img = img

class Animation:
  def __init__(self, frames: Frame, time_between: int, time_after = 0, repeat = 1):
    self.frames = frames
    self.time_between = time_between
    self.time_after = time_after
    self.repeat = repeat

WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


class Graphics2D:

    """
    The Graphics2D class is a recreation of the Java javax.swing.Graphics2D class. It is useful for removing repetitive references to the same variables, and dynamic coding.

    Attributes of common drawing methods such as color or font are not used as parameters. Instead, they are variables stored in the Graphics2D object, accessible with get / set methods, which are automatically accessed when used.

    Made by Nate Levison
    v0.3.1

    Changelog:
        - v0.3.1 - 7/5/2022: Fixed consistency
        - v0.3.0 - 7/4/2022: Documentation
        - v0.2.0 - 7/2/2022: Images
        - v0.1.0 - 7/1/2022: Creation
    """

    def __init__(self, screen: Surface, pygame: Module) -> None:
        """
        Makes a Graphics2D object.
        The Graphics2D class is based off of the standard Java library, javax.swing.Graphics2D.
        It allows for less repetition and dynamic coding.
        """

        self.screen = screen
        self.pygame = pygame
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.color = (0, 0, 0)
        self.usepack = False
        self.pack = ""
        self.alpha = 255

    def set_font(self, font) -> None:
        """
        Set the font being used in the text() method
        """

        self.font = font

    def get_font(self) -> Font:
        """
        Get the font being used in the text() method
        """

        return self.font

    def load_font(self, file, size) -> Font:
        """
        Loads a font with a file path.
        """

        return self.pygame.font.Font(file, size)

    def text_dimensions(self, text) -> Tuple:
        """
        Get the dimensions in pixels of a string of text with the current font.
        """

        return self.font.size(text)

    def text_width(self, text) -> int:
        """
        Get the width in pixels of a string of text with the current font, by accessing text_dimensions()
        """

        return self.text_dimensions(text)[0]

    def text_height(self, text) -> int:
        """
        Get the height in pixels of a string of text with the current font, by accessing text_dimensions()
        """

        return self.text_dimensions(text)[1]

    def set_color(self, color: Tuple) -> None:
        """
        Set the color being used in any shape drawings
        """

        self.color = color

    def get_color(self) -> Tuple:
        """
        Set the color being used in any shape drawings
        """

        return self.color

    def text(self, text: str, x: int, y: int) -> None:
        """
        Draws text to the screen with the default font, or given font.
        """

        text_surface = self.font.render(text, True, self.color)
        self.screen.blit(text_surface, (x, y))

    def circle(self, x: int, y: int, radius: int) -> None:
        """
        Draws a circle, with point (x+r,y+r) being at x,y, with radius r, with color given.
        """

        self.pygame.draw.circle(self.screen, self.color, (x, y), radius)

    def rect(self, x: int, y: int, w: int, h: int) -> None:
        """
        Draws a rectangle with the top left corner at (x,y) with width w and height h, with color given.
        """

        self.pygame.draw.rect(self.screen, self.color,
                              self.pygame.Rect(x, y, w, h))

    def fill(self, color: Tuple) -> None:
        """
        Colors the entire screen with a solid color. The same as saying rect(0, 0, w, h, color)
        """

        self.screen.fill(color)

    def image(self, img: Surface, x: int, y: int) -> None:
        """
        Draws an image to the screen, using an image object obtained from getImage(path).
        """
        self.screen.blit(img, (float(x), float(y)))

    def get_image(self, imgpath: str, w: int, h: int):
        """
        Creates an image object from a file path, with width w and height h.
        """

        if self.usepack:
            return self.pygame.transform.scale(self.pygame.image.load(self.pack + imgpath), (w, h))
        else:
            return self.pygame.transform.scale(self.pygame.image.load(imgpath), (w, h))

    def scale_image(self, image, w, h):

        return self.pygame.transform.scale(image, (w, h))

    def draw(self) -> None:
        """
        Draws all changes to the screen for a singular frame.
        """

        self.pygame.display.flip()
