from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glPointSize(5.0)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# DDA method defined multiple times as I was
# unable to call one method multiple times in a row

def DDA1(x1, y1, x2, y2):
    delX = x2 - x1
    delY = y2 - y1
    steps = 0
    if (abs(delX) > abs(delY)):
        steps = abs(delX)
    else:
        steps = abs(delY)

    x_inc = delX / steps
    y_inc = delY / steps

    glBegin(GL_POINTS)
    for step in range(1, steps + 1):
        glColor(1.0, 0.0, 0.0)
        glVertex2f(round(x1), round(y1))
        x1 = x1 + x_inc
        y1 = y1 + y_inc

    glEnd()

def DDA2(x1, y1, x2, y2):
    delX = x2 - x1
    delY = y2 - y1
    steps = 0
    if (abs(delX) > abs(delY)):
        steps = abs(delX)
    else:
        steps = abs(delY)

    x_inc = delX / steps
    y_inc = delY / steps


    glBegin(GL_POINTS)
    for step in range(1, steps + 1):
        glColor(1.0, 0.0, 0.0)
        glVertex2f(round(x1), round(y1))
        x1 = x1 + x_inc
        y1 = y1 + y_inc

    glEnd()

def DDA3(x1, y1, x2, y2):
    delX = x2 - x1
    delY = y2 - y1
    steps = 0
    if (abs(delX) > abs(delY)):
        steps = abs(delX)
    else:
        steps = abs(delY)

    x_inc = delX / steps
    y_inc = delY / steps

    glBegin(GL_POINTS)
    for step in range(1, steps + 1):
        glColor(1.0, 0.0, 0.0)
        glVertex2f(round(x1), round(y1))
        x1 = x1 + x_inc
        y1 = y1 + y_inc

    glEnd()

def dottedDDA(x1, y1, x2, y2):
    delX = x2 - x1
    delY = y2 - y1
    m = 0
    if (abs(delX) > abs(delY)):
        m = abs(delX)
    else:
        m = abs(delY)

    x_inc = delX / m
    y_inc = delY / m
    glBegin(GL_POINTS)

    for m in range(1, m + 1):
        if (m % 2)==0:
            glColor(0.0, 0.0, 1.0)
            glVertex2f(round(x1), round(y1))
            x1 = x1 + x_inc
            y1 = y1 + y_inc
        else:
            glColor3f(0.0, 0.0, 0.0)
            glVertex2f(round(x1), round(y1))
            x1 = x1 + x_inc
            y1 = y1 + y_inc

    glEnd()
    #glutSwapBuffers()


def showScreen():
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #glColor3f(0.0, 1.0, 1.0)

    # DRAW METHODS

    DDA1(100, 100, 100, 300)         # vertical line
    DDA2(100, 100, 200, 100)         # top horizontal line
    DDA3(100, 300, 200, 300)         # bottom horizontal line
    dottedDDA(100, 200, 200, 200)    # dotted line

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("plot letter E with DDA")
glutDisplayFunc(showScreen)

init()
glutMainLoop()