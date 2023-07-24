import sys

N = int(sys.stdin.readline().strip())  # 몇칸인지
way = sys.stdin.readline().strip()  # 경로
wayLength = len(way)

dasolMap = []
for i in range(N):
    dasolMap.append(sys.stdin.readline().strip())

zombie = []
switch = set()

for i in range(N):
    for j in range(N):
        if dasolMap[i][j] == 'Z':
            zombie.append([i,j])
        elif dasolMap[i][j] == 'S':
            switch.add((i,j))
switchLight = switch.copy()

class Ahri:
    def __init__(self, way, length) -> None:
        self.way = way
        self.length = length
        self.direction = 0 # F :0, R :1, L:2, B :3
        self.directDict = {"F" :0, "R" :1, "L":2, "B" :3}
        self.curr = [0,0]
        self.die = False
    def move(self, step):
        thisStep = self.directDict[self.way[step]]
        # print(thisStep)
        if thisStep == 0:
            if self.direction == 2:
                if self.curr[1] < N-1:
                    self.curr[1] += 1
            elif self.direction == 1:
                if self.curr[1] > 0:
                    self.curr[1] -= 1
            elif self.direction == 3:
                if self.curr[0] > 0:
                    self.curr[0] -= 1
            else:
                if self.curr[0] < N-1:
                    self.curr[0] += 1
        else:
            if self.direction == 0:
                self.direction = thisStep
            elif self.direction == 3:
                if thisStep == 1:
                    self.direction = 2
                elif thisStep == 2:
                    self.direction == 1
            else:
                if self.direction == thisStep:
                    self.direction = 3
                else:
                    self.direction = 0
        return tuple(self.curr)
                    

class Zombie:
    def __init__(self, curr) -> None:
        self.curr = curr
        self.forward = True
    def isforward(self):
        if self.curr[0] == N-1 and self.forward == True:
            self.forward = False
            return False

testAhri = Ahri(way, wayLength)
zombieIns = []        
for zom in zombie:
    zombieIns.append(Zombie(zom))

for step in range(wayLength):
    # print(step)
    ahriCurr = testAhri.move(step)
    # print(ahriCurr)
    # print(switch)
    if ahriCurr in switch:
        # print("in")
        for row in [-1,0,1]:
            for col in [-1,0,1]:
                switchLight.add((ahriCurr[0]+row, ahriCurr[1]+col))

    # print(switchLight)
    for zombie in zombieIns:
        if tuple(zombie.curr) == ahriCurr and ahriCurr not in switchLight:
            print("Aaaaaah!")
            testAhri.die = True
            break
        if zombie.isforward() == False:
            continue
        if zombie.forward == True:
            zombie.curr[0]+=1
        else:
            zombie.curr[0]-=1
        if tuple(zombie.curr) == ahriCurr and ahriCurr not in switchLight:
            print("Aaaaaah!")
            testAhri.die = True
            break
        # print(zombie.curr, ahriCurr)

    if testAhri.die == True:
        break
if testAhri.die == False:
    print("Phew...")