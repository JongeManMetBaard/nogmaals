from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
for blokjes in range(7):
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        break
    for bewegenRechts in range(blokjes + 1):
        robotArm.moveRight()
    robotArm.drop()
    for bewegenLinks in range(blokjes + 1):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
