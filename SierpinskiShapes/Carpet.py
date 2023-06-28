
# Joshua Liu
# 2023-06-16
# Sierpinski Carpet Simulation

import pygame
import math

pygame.init()
clock = pygame.time.Clock()

# Changeable values
ANIMATE = True
depthOfSierpinskiCarpet = 3
animationSpeed = depthOfSierpinskiCarpet * 3.3

BACKGROUND, SQUARE_COLOR = (0, 0, 0), (0, 255, 0)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Sierpinski Carpet"), screen.fill(BACKGROUND)

done = False


def drawSierpinskiCarpet(depth):
    length = SCREEN_WIDTH
    startingPoint = (0, 0)
    pointA = startingPoint
    pointB = (startingPoint[0] + length, startingPoint[1])
    pointC = (startingPoint[0] + length, startingPoint[1] + length)
    pointD = (startingPoint[0], startingPoint[1] + length)
    drawLine(pointA, pointB), drawLine(pointB, pointC), drawLine(pointC, pointD)
    sierpinskiCarpet(pointA, pointB, pointC, pointD, depth)


def drawLine(point1, point2):
    pygame.draw.line(screen, SQUARE_COLOR, point1, point2, 1)
    if ANIMATE:
        clock.tick(animationSpeed), pygame.display.update()


def sierpinskiCarpet(pointA, pointB, pointC, pointD, depth):
    if depth == 0:
        return
    line1Start = line1Point(pointA, pointB)
    line1End = line1Point(pointD, pointC)
    line2Start = line2Point(pointA, pointB)
    line2End = line2Point(pointD, pointC)
    line3Start = line3Point(pointA, pointD)
    line3End = line3Point(pointB, pointC)
    line4Start = line4Point(pointA, pointD)
    line4End = line4Point(pointB, pointC)
    drawLine(line1Start, line1End)
    drawLine(line2Start, line2End)
    drawLine(line3Start, line3End)
    drawLine(line4Start, line4End)
    sierpinskiCarpet(
        pointA, line1Start, (line1Start[0], line3Start[1]), line3Start, depth - 1
    )
    sierpinskiCarpet(
        line1Start,
        line2Start,
        (line2Start[0], line3Start[1]),
        (line1Start[0], line3Start[1]),
        depth - 1,
    )
    sierpinskiCarpet(
        line2Start, pointB, line3End, (line2Start[0], line3Start[1]), depth - 1
    )
    sierpinskiCarpet(
        (line2Start[0], line3Start[1]),
        line3End,
        line4End,
        (line2Start[0], line4Start[1]),
        depth - 1,
    )
    sierpinskiCarpet(
        (line2Start[0], line4Start[1]), line4End, pointC, line2End, depth - 1
    )
    sierpinskiCarpet(
        (line1Start[0], line4Start[1]),
        (line2Start[0], line4Start[1]),
        line2End,
        line1End,
        depth - 1,
    )
    sierpinskiCarpet(
        line4Start, (line1Start[0], line4Start[1]), line1End, pointD, depth - 1
    )
    sierpinskiCarpet(
        line3Start,
        (line1Start[0], line3Start[1]),
        (line1Start[0], line4Start[1]),
        line4Start,
        depth - 1,
    )


def line1Point(point1, point2):
    return ((point2[0] - point1[0]) / 3 + point1[0], point1[1])


def line2Point(point1, point2):
    return ((point2[0] - point1[0]) / 3 * 2 + point1[0], point1[1])


def line3Point(point1, point2):
    return (point1[0], (point2[1] - point1[1]) / 3 + point1[1])


def line4Point(point1, point2):
    return (point1[0], (point2[1] - point1[1]) / 3 * 2 + point1[1])


if __name__ == "__main__":
    drawSierpinskiCarpet(depthOfSierpinskiCarpet)
    pygame.display.update()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
