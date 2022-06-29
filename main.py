import graphics
from graphics import *
import gamemodel
import gamegraphics


def graphicFire(game, graphics, angle, vel):
    player = game.getCurrentPlayer()
    proj = player.fire(angle, vel)
    while proj.isMoving():
        proj.update(1/50)
        graphics.sync()
        update(50)
    return proj


def graphicPlay():

    game_on = True
    game = gamemodel.Game(10, 3)
    ggame = gamegraphics.GameGraphics(game)

    while game_on is True:
        previous_angle, previous_velocity = game.getCurrentPlayer().getAim()
        dialog = gamegraphics.InputDialog(previous_angle, previous_velocity, game.getCurrentWind())
        choice = dialog.interact()
        a, v = dialog.getValues()

        if choice == "Fire!":
            graphicFire(game, ggame, a, v)

            if game.getOtherPlayer().projectileDistance(game.getCurrentPlayer().getProjectile()) == 0:
                game.getCurrentPlayer().increaseScore()
                game.newRound()
                ggame.sync()

        elif choice == "Quit":
            game_on = False

        dialog.close()
        game.nextPlayer()


graphicPlay()
