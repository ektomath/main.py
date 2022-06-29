# ------------------------------------------------------
# This module contains all graphics-classes for the cannon game.
# The two primary classes have these responsibilities:
#  * GameGraphics is responsible for the main window
#  * Each PlayerGraphics is responsible for the graphics of a 
#    single player (score, cannon, projectile)
# In addition there are two UI-classes that have no
# counterparts in the model:
#  * Button
#  * InputDialog
# ------------------------------------------------------

# This is the only place where graphics should be imported!
from graphics import *


class GameGraphics:
    def __init__(self, gameobject):
        self.game = gameobject
        self.win = GraphWin("Cannon game", 640, 480, autoflush=False)
        self.win.setCoords(-110, -10, 110, 155)
        self.player_graphics1 = PlayerGraphics(self.game.player1, self.win, self.game.getCannonSize(), self.game.getBallSize())
        self.player_graphics2 = PlayerGraphics(self.game.player2, self.win, self.game.getCannonSize(), self.game.getBallSize())
        self.ground = Line(Point(-110, 0), Point(110, 0))
        self.ground.draw(self.win)

    def getWindow(self):
        return self.win

    def sync(self):
        self.player_graphics1.sync()
        self.player_graphics2.sync()


class PlayerGraphics:
    def __init__(self, playerobject, win, cannonsize, ballsize):
        self.cannonsize = cannonsize
        self.player = playerobject
        self.cannon = Rectangle(Point(self.player.getX()-cannonsize/2, 0), Point(self.player.getX()+cannonsize/2, self.cannonsize))
        self.cannon.setFill(self.player.getColor())
        self.cannon.draw(win)
        self.ballsize = ballsize
        self.win = win
        self.projectile = None

        self.scoreboard = Text(Point(self.player.getX(), -5), f'Score: {self.player.getScore()}')
        self.scoreboard.setTextColor(self.player.getColor())
        self.scoreboard.draw(win)


    def sync(self):
        if self.player.getProjectile():
            if self.projectile is not None:
                self.projectile.move(self.player.getProjectile().getX() - self.oldX,
                                    self.player.getProjectile().getY() - self.oldY)
            else:
                self.projectile = Circle(Point(self.player.getProjectile().getX(), self.player.getProjectile().getY()), self.ballsize)
                self.projectile.setFill(self.player.getColor())
                self.projectile.draw(self.win)

            self.oldX = self.player.getProjectile().getX()
            self.oldY = self.player.getProjectile().getY()

        self.scoreboard.undraw()
        self.scoreboard.setText(f'Score: {self.player.getScore()}')
        self.scoreboard.draw(self.win)



""" A somewhat specific input dialog class (adapted from the book) """
class InputDialog:
    """ Creates an input dialog with initial values for angle and velocity and displaying wind """
    def __init__(self, angle, vel, wind):
        self.win = win = GraphWin("Fire", 200, 300)
        win.setCoords(0, 4.5, 4, .5)
        Text(Point(1, 1), "Angle").draw(win)
        self.angle = Entry(Point(3, 1), 5).draw(win)
        self.angle.setText(str(angle))
        
        Text(Point(1, 2), "Velocity").draw(win)
        self.vel = Entry(Point(3, 2), 5).draw(win)
        self.vel.setText(str(vel))
        
        Text(Point(1, 3), "Wind").draw(win)
        self.height = Text(Point(3, 3), 5).draw(win)
        self.height.setText("{0:.2f}".format(wind))
        
        self.fire = Button(win, Point(1, 4), 1.25, .5, "Fire!")
        self.fire.activate()
        self.quit = Button(win, Point(3, 4), 1.25, .5, "Quit")
        self.quit.activate()

    """ Waits for the player to enter values and click a button """
    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    """ Gets the values entered into this window, typically called after interact """
    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        return a, v

    """ Closes the input window """
    def close(self):
        self.win.close()


""" A general button class (from the book) """
class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """ 

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "RETURNS true if button active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        "RETURNS the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0
