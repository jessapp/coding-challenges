def moveTower(height, source, helper, target):

    if height >= 1:

        moveTower(height-1, source, target, helper)
        moveDisk(source, helper)
        moveTower(height-1, target, helper, source)

def moveDisk(source, helper):
    print("moving disk from", source, "to", helper)


moveTower(3, "A", "B", "C")