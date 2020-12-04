


with open("Data/inputDay03.txt") as f:
    Map = f.read().splitlines()

Map= list(map(list,Map))

def CountTrees(vert, hor,Map):
    hor_curIndex = 0
    vert_curIndex = 0
    TreeCounter = 0
    while vert_curIndex < (len(Map)) :
        if hor_curIndex >= (len(Map[0])):
            Map = [line + line for line in Map]

        currentPos= (vert_curIndex,hor_curIndex)

        if  Map[currentPos[0]][currentPos[1]] =="#":
            TreeCounter=TreeCounter+1;

        hor_curIndex= hor_curIndex+hor
        vert_curIndex= vert_curIndex+vert
    return TreeCounter

x1_1= CountTrees(1,1,Map)
x1_3= CountTrees(1,3,Map)
x1_5= CountTrees(1,5,Map)
x1_7= CountTrees(1,7,Map)
x2_1= CountTrees(2,1,Map)
print(x1_1*x1_3*x1_5*x1_7*x2_1)
