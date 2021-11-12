from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
# Jouw python instructies zet je vanaf hier:
for herhaling in range(5):
    for proces in range(6):
        robotArm.moveRight();
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for bewegen in range(2):
        robotArm.moveRight();
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()