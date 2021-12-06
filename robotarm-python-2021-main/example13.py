from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
for blokjes in range(1,8):
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        break
    for bewegenRechts in range(blokjes):
        robotArm.moveRight()
    robotArm.drop()
    for bewegenLinks in range(blokjes):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
