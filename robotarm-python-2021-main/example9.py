from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
# Jouw python instructies zet je vanaf hier:
for proces in range (4):
    for blokjes in range(proces + 1):
        robotArm.grab()
        for bewegenRechts in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for bewegenLinks in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()