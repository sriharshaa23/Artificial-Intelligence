import copy
import random


# to get all successors 
#can create the successor by just changing the value of queen_position list
def getAllSuccessors(currNode):
    
    successors = []
    
    for i in range(8):      #for rows
        
        
        for j in range(1,9):    #for columns
            
            if (currNode[i]!=j):
                sucNode = currNode.copy()
                sucNode[i] = j
                successors.append(sucNode)
    return successors


# calculating totalDelta value    
def getTotalDelta(bestSuccessors,currNode):
    
    totalDelta = 0
    for node in bestSuccessors:
        totalDelta = totalDelta + numAttacks(node) - numAttacks(currNode)
    
    return totalDelta
    
            
# to get bestSuccessors 
def getBestSuccessors(successors,currNode):
    res = []
    for node in successors:
        if(numAttacks(currNode) >= numAttacks(node)):
            res.append(node.copy())
    return res

# calculating number of attacks of queens in node
def numAttacks(node):
    
    attacks = 0
    
    for i in range(8):
        for j in range(i+1,8):
            if(node[i]==node[j] or abs(node[i]-node[j]) == abs(i-j)):
                attacks = attacks + 1
    
    return attacks


def stocasticHill_climbing():
    """Perform the stochastic_hill_climbing until we get where there is no successor"""
    
    total_nodes = 0
    # intial-node.
    currNode = []
    
    for i in range(8) : #intializing  random node
        currNode.append(random.randint(1,8))
    
    
    while True:
        print("currNode =",currNode)
        total_nodes+=1
        print("number of attacks =",numAttacks(currNode))
        successors = getAllSuccessors(currNode) #generating all successors
        bestSuccessors = getBestSuccessors(successors,currNode) #choosing best successors from all successors
        totalDelta = getTotalDelta(bestSuccessors,currNode) #total delta values of all best successors
        
     
        
        if(len(bestSuccessors)==0 or totalDelta==0): # if no uphill movement found then stop.
            break
        
        
        
        while True:
            
            choosenSuccessor = bestSuccessors[random.randrange(len(bestSuccessors))] #choosing random successor from bestSuccessors
            
            probabilityOfSuccessorNode = (numAttacks(choosenSuccessor) - numAttacks(currNode))/totalDelta #calculating probability of that node
            
            random_number = random.uniform(0,1) # generating random number between 0,1
            
            
            if random_number <= probabilityOfSuccessorNode:#selecting according to the probability.
                
                currNode = choosenSuccessor
                break
    
    print(currNode)
    print('\n')
    print('\n')
    board = []
    for i in range(8):
        board.append(['*','*','*','*','*','*','*','*'])
    for i in range(8):
        board[i][currNode[i]-1] = 'Q' 
    
    for j in range(8):
        for i in range(8):
            print(board[j][i],end=" ")
        print('\n')
    print("total number of nodes generated=",total_nodes)






if __name__ == "__main__":
    stocasticHill_climbing()