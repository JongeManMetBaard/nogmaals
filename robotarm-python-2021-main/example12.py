from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
for blokjes in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for bewegenRechts in range(9 - blokjes):
            robotArm.moveRight()
        robotArm.drop()
        for bewegenLinks in range(8 - blokjes):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
