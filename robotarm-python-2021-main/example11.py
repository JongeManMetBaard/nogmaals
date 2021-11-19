from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for bewegenRechts in range(9):
    robotArm.moveRight()
robotArm.moveLeft()
for blokjes in range(14):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else: 
        robotArm.drop()
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()