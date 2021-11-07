def performMove():
    global elementInHeap
    global shouldOrder
    global moveCount
    global myList
    global currentMin
    if shouldOrder == 1:
        myList.sort()
        shouldOrder=0
        moveCount+=1
    if len(myList)>1:
        currentMin=myList[1]
    else:
        currentMin = 999999
    myList.pop(0)
    elementInHeap-=1

def performAdd(sight_id):
    global myList
    global elementInHeap
    global shouldOrder
    global currentMin
    elementInHeap+=1
    if sight_id<currentMin:
        currentMin=sight_id
    if elementInHeap>0 and sight_id>currentMin:
        shouldOrder=1
    myList.append(sight_id)

elementInHeap=0  
shouldOrder = 0
moveCount = 0
myList = []
currentMin = 999999

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n*2):
        cmd = input()
        if 'add' in cmd:
            parsedCommand, sight_id = cmd.split(' ')
        else:
            parsedCommand=cmd
        
        if 'add' in parsedCommand:
            performAdd(int(sight_id))
        else:
            performMove()
    print(moveCount)
        