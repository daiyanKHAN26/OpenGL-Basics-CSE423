from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def drawpoints(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def drawlines(): #star with lines
    glBegin(GL_LINES)

    glVertex2f(50, 100)
    glVertex2f(70, 150)

    glVertex2f(70, 150)
    glVertex2f(90, 100)

    glVertex2f(90, 100)
    glVertex2f(40, 130)

    glVertex2f(50, 100)
    glVertex2f(100, 130)

    glVertex2f(40, 130)
    glVertex2f(100, 130)

    glEnd()

def drawtriangle(): #star with triangles
    glBegin(GL_TRIANGLES)

    glVertex2f(150,200)
    glVertex2f(200,300)
    glVertex2f(250,200)

    glVertex2f(200,180)
    glVertex2f(250,280)
    glVertex2f(150,280)

    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here

    drawtriangle()
    drawlines()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()