# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class GridIO:
    def ModifyGrid(grid, location, value):
        for l in location:
            grid[l[0]][l[1]] = value
        return grid
    def FinAllFreeLocs(grid):
        print(len(grid))
        location = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                local = []
                if grid[i][j] == 0:
                    local.append(i)
                    local.append(j)
                    location.append(local)
        return location
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
    
    def WriteGrid(filename,grid):
     try:
        create =open(filename,'x')
        write = open(filename,'w')
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
            print("the {} exists".format(filename))
import random
def main():  
    
    read =GridIO.ReadGrid('grid.txt')
    print(read)
    location = GridIO.FinAllFreeLocs(read)
    print(location)
    value = random.randint(2,9)
    grid = GridIO.ModifyGrid(read,location,value)
    print(grid)
    GridIO.WriteGrid("new.txt",grid)
    
main()