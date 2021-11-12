from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for proces in range(7):
    robotArm.grab()
    for bewegenRechts in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for bewegenLinks in range(8):
        robotArm.moveLeft()

    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()