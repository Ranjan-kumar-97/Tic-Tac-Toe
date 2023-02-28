def print_list(l):
    #Takes a list and prints all items
    j=0
    for k in l:
        print("!",end=" ")
        print(k,end=" ")
        j+=1
        if j==3 or j==6 or j==9:
            print("!\n")
    


def tic_tac_toe():
    matrix=[1,2,3,4,5,6,7,8,9]
    win_lose(matrix)

    

def win_lose(grid):
    choice=str(input("Please enter your choice from O and X\t: "))
    pl1=choice.upper()
    if pl1=="O" or pl1=="X":
        print("Player 1\t:"+pl1)
        if pl1 == "O":
            pl2='X'
            print("Player 1\t:"+pl2)
        else:
            pl2="O"
            print("Player 2\t:"+pl2)
        i= range(1,10)
        w=0
        temp=pl1
        try:
            while any(item in i for item in grid):
                print_list(grid)
                print("Enter Position for ",temp +"\t:",end="")
                move=int(input())
                if move in range(1,10):
                    ind=grid.index(move)
                    grid[ind]=temp

                    if grid[0]==grid[3]==grid[6] or grid[0]==grid[1]==grid[2] or grid[0]==grid[4]==grid[8]:
                        print("You won", grid[0])
                        w=1
                        break
                    elif grid[2]==grid[5]==grid[8] or grid[2]==grid[4]==grid[6]:
                        print("You won", grid[2])
                        w=1
                        break
                    elif grid[6]==grid[7]==grid[8]:
                        print("You won", grid[6])
                        w=1
                        break
                    elif grid[3]==grid[4]==grid[5]:
                        print("You won", grid[3])
                        w=1
                        break
                    elif grid[1]==grid[4]==grid[7]:
                        print("You won", grid[1])
                        w=1
                        break 
                    if grid[0]!=1 and grid[1]!=2 and grid[2]!=3 and grid[3]!=4 and grid[4]!=5 and grid[5]!=6 and grid[6]!=7 and grid[7]!=8 and grid[8]!=9 and w!=1:
                        print("Match Tie")
                        break


                    if temp==pl1:
                        temp=pl2
                    elif temp==pl2:
                        temp=pl1


                else:
                    print("Wrong choice, Please chose from:")

        except:
            print("\nChoice Repeated!")
            print("Be carefull next time!\n")
    else:
        print("Wrong choice, only O or X!")
    
    

      
        

tic_tac_toe()
