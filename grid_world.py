#NAME - HARDEEKH GARG
#ROLL NUMBER - 2019040
#SECTION - A
#GROUP - 4
#IP ASSIGNMENT 4

from random import randint, shuffle, sample
from os import system
from time import sleep

class grid():
    def __init__(self,N,start,goal,myObstacles, myRewards):
        self.N=N
        self.start=start
        self.goal=goal
        self.myObstacles=myObstacles
        self.myRewards=myRewards

        #class variable to denote number of rotations
        n=0
        
    def rotateClockwise(self, n):

        #loop rotates the coordinates of obstacles and rewards
        for j in range(n):
            
            for i in range(self.N*self.N):
                if(i<len(self.myObstacles)):
                    self.myObstacles[i].x, self.myObstacles[i].y = self.myObstacles[i].y, self.N - 1 - self.myObstacles[i].x
                if(i<len(self.myRewards)):
                    self.myRewards[i].x, self.myRewards[i].y = self.myRewards[i].y, self.N - 1 - self.myRewards[i].x

            for i in range(len(self.myObstacles)):                  

                #condition to check if or not rotation results in collision with an obstacle,
                #if yes, rotation is not carried out
                
                if(p1.x==self.myObstacles[i].x and p1.y==self.myObstacles[i].y):
                    #restoring points in case of no rotation
                    p1.energy+=self.N//3
                    
                    #reversing the changes in case obstacle is found
                    for k in range(self.N*self.N):
                        if(k<len(self.myObstacles)):
                            self.myObstacles[k].x, self.myObstacles[k].y = self.N - 1 - self.myObstacles[k].y, self.myObstacles[k].x
                        if(k<len(self.myRewards)):
                            self.myRewards[k].x, self.myRewards[k].y = self.N - 1 - self.myRewards[k].y, self.myRewards[k].x
                            
                    #loop to check excess energy
                    for l in range(len(self.myRewards)):
                        if(p1.x==self.myRewards[l].x and p1.y==self.myRewards[l].y):
                            p1.energy-=self.myRewards[l].value*self.N
                            break
                            
                    print("Invalid Rotation! Collision with obstacle detected!")
                    sleep(2)
                    break
                

                
    def rotateAnticlockwise(self, n):

        #logic similar to rotate clockwise is employed here
        
        for j in range(n):
            
            for i in range(self.N*self.N):
                if(i<len(self.myObstacles)):
                    self.myObstacles[i].x, self.myObstacles[i].y = self.N - 1 - self.myObstacles[i].y, self.myObstacles[i].x
                if(i<len(self.myRewards)):
                    self.myRewards[i].x, self.myRewards[i].y = self.N - 1 - self.myRewards[i].y, self.myRewards[i].x
                    
            for i in range(len(self.myObstacles)):                    
                
                if(p1.x==self.myObstacles[i].x and p1.y==self.myObstacles[i].y):
                    p1.energy+=self.N//3
                    
                    for k in range(self.N*self.N):
                        if(k<len(self.myObstacles)):
                            self.myObstacles[k].x, self.myObstacles[k].y = self.myObstacles[k].y, self.N - 1 - self.myObstacles[k].x
                        if(k<len(self.myRewards)):
                            self.myRewards[k].x, self.myRewards[k].y = self.myRewards[k].y, self.N - 1 - self.myRewards[k].x
                            
                    for l in range(len(self.myRewards)):
                        if(p1.x==self.myRewards[l].x and p1.y==self.myRewards[l].y):
                            p1.energy-=self.myRewards[l].value*self.N
                            break
                    
                    print("Invalid Rotation! Collision with obstacle detected!")
                    sleep(2)
                    break
                    

                
                    
    def showGrid(self):
        
        #Printing energy
        print("Energy: ", p1.energy)

        #loop to print grid       
        for i in range(N):
            for j in range(N):              
            
                if(i==p1.x and j==p1.y):
                    print("O", end=" ")
                    continue

                elif(i==self.goal[0] and j==self.goal[1]):
                    print("G", end=" ")
                    continue

                #condition to print X to show the path
                elif(P[i][j]>=1):
                    print("X", end=" ")
                    continue

                #counter variable x to check collision with obstacles or getting rewards
                x=0
                for k in range(len(self.myObstacles)):
                    if(k<len(self.myRewards) and i==self.myRewards[k].x and j==self.myRewards[k].y):
                        print(self.myRewards[k].value, end=" ")
                        x+=1
                        continue
    
                    elif(i==self.myObstacles[k].x and j==self.myObstacles[k].y):
                        print("#", end=" ")
                        x+=1
                        continue
                    
                #condition to print "." wherever there is no obstacle or reward or player or goal
                if(x<1):
                    print(".", end=" ")
            #line break        
            print()
        

class Obstacle():
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Reward():
    def __init__(self,x,y,value):
        self.x=x
        self.y=y
        self.value=value

class Player():
    def __init__(self,x,y,energy):
        self.x=x
        self.y=y
        self.energy=energy
        
    #class variable for movement inputs
    s=""
    
    def makeMove(self,s):
        
        self.s=self.s.upper()

        #traversing through the string entered by the user
        for i in range(len(self.s)):

            #detecting alphabet for knowing move type
            if(self.s[i].isalpha()):

                #initializing numerical value of the move
                numerical=""

                #loop to extract numerical value by looping till the next alphabet
                for j in range(i+1,len(self.s)):
                    if(self.s[j].isalpha()):
                        break
                    if(self.s[j].isdigit()):
                        numerical+=s[j]
                        
                numerical=int(numerical)
                

                
                #looping through each move, one at a time
                for j in range(numerical):

                    
                    #updating log of visited cells, to print "X" in the grid, 
                    P[p1.x][p1.y]+=1
                    
                    #storing values of x and y coordinates of player in temp variables, in case we need to roll back changes
                    tempx=p1.x
                    tempy=p1.y
                    
                    if(self.s[i]!="C" and self.s[i]!="A"): #condition for UDLR moves
                
                        if(self.s[i]=="U"):
                            
                            p1.x-=1
                            if(abs(p1.x+1)%N==0):
                                p1.x=N-1
                            else:
                                p1.x=abs(p1.x+1)%N-1
                            
                        if(self.s[i]=="D"):
                            
                            p1.x+=1
                            if((p1.x+1)%N==0):
                                p1.x=N-1
                            else:
                                p1.x=(p1.x+1)%N-1

                        if(self.s[i]=="R"):
                            
                            p1.y+=1
                            if((p1.y+1)%N==0):
                                p1.y=N-1
                            else:
                                p1.y=(p1.y+1)%N-1

                        if(self.s[i]=="L"):
                            
                            p1.y-=1
                            if(abs(p1.y+1)%N==0):
                                p1.y=N-1
                            else:
                                p1.y=abs(p1.y+1)%N-1

                        #decrementing score in case of UDLR moves
                        p1.energy-=1

                    else: #condition for rotatory moves
                        
                        #it is assumed that the each grid rotation will be shown. For example, if the grid is rotated clockwise
                        #3 times, the grid will be shown after each rotation. Also, if the 3rd rotation is an invalid one,
                        #the grid is rotated only 2 times.
                        
                        if(self.s[i]=="C"):
                            grid1.rotateClockwise(1)
                            p1.energy-=N//3
                            grid1.showGrid()
                            

                        elif(self.s[i]=="A"):
                            grid1.rotateAnticlockwise(1)
                            p1.energy-=N//3
                            grid1.showGrid()
                            
                                      

                    #OUTPUT STATEMENTS FOLLOW
                            
                    #checking victory
                    if(p1.x==grid1.goal[0] and p1.y==grid1.goal[1] and p1.energy>=0 and len(grid1.myRewards)==0):
                        
                        print("Congratulations! You Won!")
                        
                        sleep(2)
                        exit()

                    #A checker variable x to check collision with obstacle to rollback changes later on    
                    x=0
                    
                    #checking if player collides with an obstacle or scores a point
                    #it is assumed that move will be terminated only at the instant when player collides with obstacle.
                    #For example - in R3L4D2, if D1 is an invalid move, then player moves only till R3L4 and stops. It also loses points
                    #for colliding with an obstacle.
                    
                    for k in range(len(grid1.myObstacles)):
                        if(p1.x==grid1.myObstacles[k].x and p1.y==grid1.myObstacles[k].y):
                            p1.energy-=4*N
                            x+=1
                            p1.x=tempx
                            p1.y=tempy
                            continue
                            
                            
                        elif(k<len(grid1.myRewards) and p1.x==grid1.myRewards[k].x and p1.y==grid1.myRewards[k].y):
                            p1.energy+=grid1.myRewards[k].value*N
                            grid1.myRewards.remove(grid1.myRewards[k])
    
                                        
                    #condition which prints message corresponding to collision with an obstacle       
                    if(x==1):
                        system('cls')        
                        grid1.showGrid()
                        print("You collided with an obstacle! Move stopped here!")
                        if((p1.x!=grid1.goal[0] or p1.y!=grid1.goal[1]) and p1.energy<=0):
                            print("Sorry! You Lose!")
                            sleep(2)
                            exit()
                        sleep(0.5)
                        break

                    #condition printing message corresponidng to losing the game
                    if((p1.x!=grid1.goal[0] or p1.y!=grid1.goal[1]) and p1.energy<=0):
                        print("Sorry! You Lose!")
                        sleep(2)
                        exit()
                        
                    #condition to clear screen and show the next grid
                    if(x==0):
                        system('cls')
                        grid1.showGrid()
                        sleep(0.5)
                        
        #loop to reset 2D list P, which is used to show "X" trail
        for a in range(N):
                for(b) in range(N):
                    P[a][b]=0
                    
                    

#taking input for side of grid
N=int(input("enter side of square grid: "))

#creating empty 2d list for storing visited cells
P=[[0 for i in range(N)] for j in range(N)]


#generating a list for sampling of random obstacles and rewards, and shuffling it
samp=[]
for i in range(N):
    for j in range(N):
        samp.append([i,j])

shuffle(samp)


#setting up N*N//3 obstacle and N*N//6 rewards
obstacle_count=N*N//3
reward_count=N*N//6
obstacle=[]
reward=[]

#starting and ending positions entered as lists
generator=[[0,randint((N-1)//10, 9*(N-1)//10)], [randint((N-1)//10, 9*(N-1)//10), 0], [0,randint(0,N-1)], [randint(0, N-1), 0]]


#creating new grid with randomly generated data
#in case goal position coincides with obstacle/reward, the goal position takes priority

grid1=grid(N, generator[randint(0,3)], generator[randint(0,3)],obstacle, reward)

#statement to change start and goal in case they are the same

if(grid1.start[0]==grid1.goal[0] and grid1.start[1]==grid1.goal[1]):
    grid1.start=[0,N-1]
    grid1.goal=[N-1,0]

#creating array for obstacles and rewards as objects and generating random objects
for i in range(N*N):
    
    if(i<N*N//2):
            obs=Obstacle(samp[i][0], samp[i][1])
            if((grid1.start[0]!=obs.x or grid1.start[1]!=obs.y) and (grid1.goal[0]!=obs.x or grid1.goal[1]!=obs.y)):
                if(len(obstacle)<N*N//3):
                    obstacle.append(obs)
    else:
            rew=Reward(samp[i][0], samp[i][1], randint(1,9))
            if((grid1.start[0]!=rew.x or grid1.start[1]!=rew.y) and (grid1.goal[0]!=rew.x or grid1.goal[1]!=rew.y)):
                if(len(reward)<N*N//6):
                    reward.append(rew)




#creating new player
p1=Player(grid1.start[0],grid1.start[1],2*N)

#showing initial grid
grid1.showGrid()


#loop which runs till game is over

while(p1.energy>=0 or (p1.x!=grid1.goal[0] or p1.y!=grid1.goal[1])):

    #taking input of moves and sending them to makeMove function
    p1.s=input("Enter your next move: ")
    p1.makeMove(p1.s)
    


