
# Joshua Liu
# 2023-06-16
# Sierpinski Triangle Simulation

import pygame
import math

pygame.init()
clock = pygame.time.Clock()

# Changeable values
ANIMATE = True
depthOfSierpinski = 7
animationSpeed = depthOfSierpinski * 3.3

BACKGROUND, TRIANGLE_COLOR = (0, 0, 0), (0, 255, 0)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Sierpinski Triangle"), screen.fill(BACKGROUND)

done = False


def drawSierpinski(depth):
    length = SCREEN_WIDTH
    startingPoint = (0,50)
    pointA = startingPoint
    pointB = (length / 2 + startingPoint[0], (math.sqrt(3) / 2) * length + startingPoint[1])
    pointC = (length + startingPoint[0], startingPoint[1])
    drawTriangle(pointA, pointB, pointC)
    sierpinski(pointA, pointB, pointC, depth)


def drawTriangle(pointA, pointB, pointC):
    pygame.draw.polygon(screen, TRIANGLE_COLOR, (pointA, pointB, pointC), 1)
    if ANIMATE:
        clock.tick(animationSpeed), pygame.display.update()


def sierpinski(pointA, pointB, pointC, depth):
    if depth == 0:
        return
    midpointAB, midpointAC, midpointBC = midpoint(pointA, pointB), midpoint(pointA, pointC), midpoint(pointB, pointC)
    drawTriangle(midpointAB, midpointAC, midpointBC)
    sierpinski(pointA, midpointAB, midpointAC, depth - 1)
    sierpinski(midpointAB, pointB, midpointBC, depth - 1)
    sierpinski(midpointAC, midpointBC, pointC, depth - 1)


def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)


if __name__ == "__main__":
    drawSierpinski(depthOfSierpinski)
    pygame.display.update()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
