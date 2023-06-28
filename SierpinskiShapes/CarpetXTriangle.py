
# Joshua Liu
# 2023-06-16
# Sierpinski Carpet & Triangle Simulation

import pygame
import math

pygame.init()
clock = pygame.time.Clock()

# Changeable values
ANIMATE = False
depthOfSierpinskiCarpet = 3
depthOfSierpinskiTriangle = 5
animationSpeed = depthOfSierpinskiTriangle * 3.3

BACKGROUND, TRIANGLE_COLOR, CARPET_COLOR = (0, 0, 0), (255, 255, 255), (255,255,255)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Sierpinski"), screen.fill(BACKGROUND)

done = False


def drawSierpinskiCarpet(depth):
    length = SCREEN_WIDTH
    pointA = (0, 0)
    pointB = (pointA[0] + length, pointA[1])
    pointC = (pointA[0] + length, pointA[1] + length)
    pointD = (pointA[0], pointA[1] + length)
    drawLine(pointA, pointB), drawLine(pointB, pointC), drawLine(pointC, pointD)
    sierpinskiCarpet(pointA, pointB, pointC, pointD, depth)


def drawLine(point1, point2):
    pygame.draw.line(screen, CARPET_COLOR, point1, point2, 1)
    if ANIMATE:
        clock.tick(animationSpeed), pygame.display.update()


def sierpinskiCarpet(pointA, pointB, pointC, pointD, depth):
    if depth == 0:
        return
    line1Start,line1End = line1Point(pointA, pointB),line1Point(pointD, pointC)
    line2Start,line2End = line2Point(pointA, pointB),line2Point(pointD, pointC)
    line3Start,line3End = line3Point(pointA, pointD),line3Point(pointB, pointC)
    line4Start,line4End = line4Point(pointA, pointD),line4Point(pointB, pointC)
    drawLine(line1Start, line1End), drawLine(line2Start, line2End), drawLine(line3Start, line3End), drawLine(line4Start, line4End)
    drawSierpinskiTriangle((line1Start[0], line3Start[1]), (line2Start[0], line3Start[1]), ((pointB[0] - pointA[0])/2 + pointA[0], line4Start[1]), depthOfSierpinskiTriangle)
    sierpinskiCarpet(pointA, line1Start, (line1Start[0], line3Start[1]), line3Start, depth - 1)
    sierpinskiCarpet(line1Start, line2Start,(line2Start[0], line3Start[1]), (line1Start[0], line3Start[1]),depth - 1)
    sierpinskiCarpet(line2Start, pointB, line3End, (line2Start[0], line3Start[1]), depth - 1)
    sierpinskiCarpet((line2Start[0], line3Start[1]), line3End, line4End, (line2Start[0], line4Start[1]),depth - 1)
    sierpinskiCarpet((line2Start[0], line4Start[1]), line4End, pointC, line2End, depth - 1)
    sierpinskiCarpet((line1Start[0], line4Start[1]), (line2Start[0], line4Start[1]), line2End,line1End,depth - 1)
    sierpinskiCarpet(line4Start, (line1Start[0], line4Start[1]), line1End, pointD, depth - 1)
    sierpinskiCarpet(line3Start, (line1Start[0], line3Start[1]), (line1Start[0], line4Start[1]), line4Start, depth - 1)


def line1Point(point1, point2):
    return ((point2[0] - point1[0]) / 3 + point1[0], point1[1])


def line2Point(point1, point2):
    return ((point2[0] - point1[0]) / 3 * 2 + point1[0], point1[1])


def line3Point(point1, point2):
    return (point1[0], (point2[1] - point1[1]) / 3 + point1[1])


def line4Point(point1, point2):
    return (point1[0], (point2[1] - point1[1]) / 3 * 2 + point1[1])


def drawSierpinskiTriangle(pointA, pointB, pointC, depth):
    drawTriangle(pointA, pointB, pointC)
    sierpinskiTriangle(pointA, pointB, pointC, depth)


def drawTriangle(pointA, pointB, pointC):
    pygame.draw.polygon(screen, TRIANGLE_COLOR, (pointA, pointB, pointC), 1)
    if ANIMATE:
        clock.tick(animationSpeed), pygame.display.update()


def sierpinskiTriangle(pointA, pointB, pointC, depth):
    if depth == 0:
        return
    midpointAB, midpointAC, midpointBC = midpoint(pointA, pointB), midpoint(pointA, pointC), midpoint(pointB, pointC)
    drawTriangle(midpointAB, midpointAC, midpointBC)
    sierpinskiTriangle(pointA, midpointAB, midpointAC, depth - 1)
    sierpinskiTriangle(midpointAB, pointB, midpointBC, depth - 1)
    sierpinskiTriangle(midpointAC, midpointBC, pointC, depth - 1)


def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)


if __name__ == "__main__":
    drawSierpinskiCarpet(depthOfSierpinskiCarpet)
    pygame.display.update()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
