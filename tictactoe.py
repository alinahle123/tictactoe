# TIC TAC TOE game
import random
# function to print a tic-tao-toe grid stored as a list of 3 lists
def print_grid(grid):
    for row in grid:
        for e in row:
            print(e, end = ' ')
        print()

# test the function print_grid

def grid1(lst):
   
    for i in range(3):
        p=[]
        for j in range(3):
            p.append('_')
        lst.append(p)
    return lst
        





def check_win(grid, player):
    for i in grid:
        if (i[0]==player and i[1]==player and i[2]==player):
            print(player,"has won")
            return True
        elif (grid[0][0]==player and grid[1][1]==player and grid[2][2]==player) or (grid[0][2]==player and grid[1][1]==player and grid[2][0]==player):
            print(player,"has won")
            return True
        elif(grid[0][0]==player and grid[1][0]==player and grid[2][0]==player) or (grid[0][1]==player and grid[1][1]==player and grid[2][1]==player) or (grid[0][2]==player and grid[1][2]==player and grid[2][2]==player):
            print(player,"has won")
            return True
        else:
            return False


number='1234567890'
def get_user_pick(empty_cells, grid):
   
    a=input("please choose a row : ")
    c=input("please choose a cell from this row: ")
    if (a and c) in number:
        if 0<=int(a)<3 or 0<=int(c)<3:
            if grid[int(a)][int(c)]==empty_cells:
                grid[int(a)][int(c)]='x'
            else:
                print("this cell is not empty")
                print("choose another one")
                get_user_pick(empty_cells,grid)
        else :
            print("wrong cell")
            get_user_pick(empty_cells,grid)
    else:
        print("a and b should be integers")
        get_user_pick(empty_cells,grid)





def computer_pick(empty_cells, grid):
    while True:
        x=random.randrange(0,3)
        y=random.randrange(0,3)
        if grid[x][y]==empty_cells:
            grid[x][y]='o'
            break
    
                    
        
def tie(grid,empty_cells):
    for i in grid:
        for j in i :
            if j==empty_cells:
                return True
    return False



def tictactoe():
    ''' Your code goes here
    '''
    g=[]
    grid1(g)
    empty_cells='_'
    grid=g
    b=random.choice([computer_pick,get_user_pick])
    n=8
    if b==computer_pick:
        computer_pick(empty_cells,grid)
        print_grid(grid)
        print("------------")
        while n!=0:
            get_user_pick(empty_cells,grid)
            n-=1
            print_grid(grid)
            if check_win(grid,"x"):
                break
            print("---------------")
            computer_pick(empty_cells,grid)
            n-=1
            print_grid(grid)
            if check_win(grid,"o"):
                break
            print("-------------")
            if not tie(grid,empty_cells) and not check_win(grid,"o") and not check_win(grid,"x"):
                print ("tie")
            
    else:
        get_user_pick(empty_cells,grid)
        print_grid(grid)
        print("----------------")
        while n!=0:
            computer_pick(empty_cells,grid)
            n-=1
            print_grid(grid)
            if check_win(grid,"o"):
                break
            print("------------")
            get_user_pick(empty_cells,grid)
            n-=1
            print_grid(grid)
            if check_win(grid,"x"):
                break
            print("------------")
            if not tie(grid,empty_cells) and not check_win(grid,"o") and not check_win(grid,"x"):
                print ("tie")

        

           

# start the game
tictactoe()

