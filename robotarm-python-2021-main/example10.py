from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for bewegenRecht in range (9):
    robotArm.moveRight()
robotArm.drop()
for blokjes in range (4):
    for bewegenLinks in range(5):
        robotArm.moveLeft()
    robotArm.grab()
    for bewegenRecht in range(4):
        robotArm.moveRight()
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()