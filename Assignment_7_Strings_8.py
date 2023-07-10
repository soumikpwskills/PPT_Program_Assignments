def checkStraightLine(coordinates):
    num = len(coordinates)
    if coordinates is None or num == 2: return True
    dy0 = coordinates[1][1] - coordinates[0][1]
    dx0 = coordinates[1][0] - coordinates[0][0]
    for i in range(1,num-1):
        dy1 = coordinates[i+1][1] - coordinates[i][1]
        dx1 = coordinates[i+1][0] - coordinates[i][0]
        if dy0 * dx1 != dy1 * dx0: return False
    return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))