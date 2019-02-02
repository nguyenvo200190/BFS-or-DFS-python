# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 07:45:18 2019

@author: vophanguyen
"""

def ReadGrid(filename):
        read = open(filename,'r')
        grid = []
        line = read.readline()
        while line:
            gridline = []
            for once in line:
             if once =='1' or once == '0':
                gridline.append(int(once))
            grid.append(gridline)
            line = read.readline()
        read.close()
        return grid
    
def getChildren(father,grid):
    child = []
    child_line =[]
    #get right
    if grid[father[0]][father[1]+1]==0:
        child_line.append(father[0])
        child_line.append(father[1]+1)
    if child_line:
     child.append(child_line)
     child_line =[]
    #get down
    if grid[father[0]+1][father[1]]==0:
        child_line.append(father[0]+1)
        child_line.append(father[1])
    if child_line:
     child.append(child_line)
     child_line =[]
    #get left
    if grid[father[0]][father[1]-1]==0:
        child_line.append(father[0])
        child_line.append(father[1]-1)
    if child_line:
     child.append(child_line)
    return child

def expandNode(node,child):
#    print("node in:",node)
#    print("child in:",child)
    fatherToChild=[]
    fatherToChild.append(node)
    for x in child:
      fatherToChild.append(x)
#    print("chekc:",fatherToChild)
    return fatherToChild
def writeGrid(grid,start,goal,path):
    try:
        create =open('newGrid.txt','x')
        write = open('newGrid.txt','w')
        for line in grid:
            for index in range(len(line)):
                if index < len(line)-1 :
                    write.write(str(line[index]))
                    write.write(" ")
                else:
                    write.write(str(line[index]))
            write.write("\n")
        create.close()
    except FileExistsError:
        write = open('newGrid.txt','w')
        for line in grid:
            for index in range(len(line)):
                if index < len(line)-1 :
                    write.write(str(line[index]))
                    write.write(" ")
                else:
                    write.write(str(line[index]))
            write.write("\n")
        write.close()
            
def availableGrid(grid):
   av =[]
   for i in range(len(grid)):
     for j in range(len(grid[i])):
         avLine = []
         if grid[i][j]==0:
             avLine.append(i)
             avLine.append(j)
         if avLine:
          av.append(avLine)
   return av
         
        
    
def main():
    ava = availableGrid(ReadGrid('grid.txt'))
    check = 0
    start =[]
    goal =[]
    #Input Start
    while check <= 0:
        print("\nGet input of location Start:")
        print("Locations the agent cann traverse:")
        print(ava)
        inputs = input("Selec first one:")
        start.append(int(inputs))
        inputs = input("Selec second one:")
        start.append(int(inputs))
        if start in ava:
            check +=1
        else:
            print("Please select again")
    #Input Goal
    check = 0
    while check <= 0:
        print("\nGet input of location Goal:")
        print(" locations the agent cann traverse:")
        print(ava)
        print("Please dont select same location Start:", start)
        inputs = input("Selec first one:")
        goal.append(int(inputs))
        inputs = input("Selec second one:")
        goal.append(int(inputs))
        if goal in ava and goal not in start:
            check +=1
        else:
            print("Please select again")    
    openList = [start]
    closeList = []
    nodeList =[]
    node = []
    #Menu select which algorithm to use (DFS or BFS)
    print("plese selec:\n1.BES\n2.DFS")
    inputs = input("Enter your choice:")
    if inputs == '1': #BFS
      while openList:
        node =openList.pop(0)
        if node == goal:
            print ("Success")
            break
        closeList.append(node)
        grid = ReadGrid('grid.txt')
        child = getChildren(node,grid)
        childGet = []
        for c in child:
            if c not in openList and c not in closeList:
                openList.append(c)
                childGet.append(c)
        nodeList.append(expandNode(node,childGet))
    elif inputs == '2': #DFS
        while openList:
          node =openList.pop(-1)
          if node == goal:
            print ("Success")
            break
          closeList.append(node)
          grid = ReadGrid('grid.txt')
          child = getChildren(node,grid)
          childGet = []
          for c in child:
            if c not in openList and c not in closeList:
                openList.append(c)
                childGet.append(c)
          nodeList.append(expandNode(node,childGet))
    else:
        print("eror")
    if inputs =='1' or inputs =='2': #Check inputs 
     path=[node]
     #Get the Path
     for line in range(0,len(nodeList)):
        for i in nodeList[-1-line]:
            if i == node:
                path.append(nodeList[-1-line][0])
            node = path[-1] 
     print("pat:",path)
     grid = ReadGrid('grid.txt')
     #Create the path in Grid with ‘S’ for the initial state, ‘G’ for the goal state, and ‘*’ to the rest of path
     grid[path[0][0]][path[0][1]]="G"
     grid[path[-1][0]][path[-1][1]]="S"
     for i in range(1,len(path)-1):
        grid[path[i][0]][path[i][1]]='*'
     for line in grid:
        for i in range(len(line)):
            print(line[i],end=" ")
        print("\n")
     #Write the new file
     writeGrid(grid,start,goal,path)
    
main()
    