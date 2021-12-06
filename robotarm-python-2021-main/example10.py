from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:
move = 8
robotArm.grab()
for moveRight in range(9):
    robotArm.moveRight()
robotArm.drop()
for cubes in range(4):
    for moveLeft in range(move):
        robotArm.moveLeft()
    move -= 2
    robotArm.grab()
    for moveRight in range(move + 1):
        robotArm.moveRight()
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()