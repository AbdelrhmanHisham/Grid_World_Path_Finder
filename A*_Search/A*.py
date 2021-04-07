

def Action(state , mov , cst):
    return [state[0]+cst,state[1]+mov[0] , state[2]+mov[1]]

def Free_Collision(World ,Pos):

    Free = True
    Border_x = len(World)-1
    Border_y = len(World[0]) -1

# Check x Border
    if (Pos[1] < 0 or Pos[1] > Border_x ):
        Free = False
# Check y Border
    if (Pos[2] < 0 or Pos[2] > Border_y ):
        Free = False
# Ckeck the node is Free or Not
    if (Free == True):
        if (World[Pos[1]][Pos[2]] == 1):
            Free = False

    return Free

def Not_Visited(visit_list , nxt_state):
    return (visit_list[nxt_state[1]][nxt_state[2]] == 0)

def Expand(World,Open_Space ,hur,visited_World ,Pos , mov , sg):
    next_state = []
    visited_World[Pos[1]][Pos[2]] = 1
    for i in range(4):
        next_state = Action(Pos , mov[i] , (cost + hur[Pos[1]][Pos[2]]))
        if ((Free_Collision(World , next_state) == True )): 
            if (Not_Visited(visited_World , next_state)==True) :
                if(Open_Space.count(next_state) == 0):
                    Open_Space.append(next_state)
                    sg[next_state[1]][next_state[2]] = i
    
    Open_Space.remove(Pos)

Map_World = [[0,1,0,0,0,0],
             [0,1,0,0,0,0],
             [0,1,0,0,0,0],
             [0,1,0,0,0,0],
             [0,0,0,1,0,0]]

visited_World = [[0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]

Expanded_World = [[-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1]]

Action_World = [[0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]


Hueristic_Fun = [[9,8,7,6,5,4],
                [8,7,6,5,4,3],
                [7,6,5,4,3,2],
                [6,5,4,3,2,1],
                [5,4,3,2,1,0]]

Policy = [[' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' '],
          [' ',' ',' ',' ',' ',' ']]


Open_list = []
Visited_List =[]
goal = [ len(Map_World)-1 , len(Map_World[0])-1]
init = [0,0,0]
cost = 1
Policy[goal[0]][goal[1]] = '*'

movement = [[-1 ,0], #UP
            [0 ,-1], #LEFT
            [1 , 0],  #DOWN
            [0 , 1] #RIGHT
            ]


movement_sign = ['^' ,'<' ,'V' ,'>']
Open_list.append(init)

state = "Searching !!!"
current_x = 0
current_y = 0
Expanded_World[current_x][current_x] = 0

x = 0
target_vector = []
count = 1
while (state != "Search End"):

    Expand(Map_World , Open_list ,Hueristic_Fun ,visited_World, Open_list[0] , movement ,Action_World)
    # print(Open_list)
    if (len(Open_list) == 0) :
        state = "Search FAil !!!"
        print(state)
        break


    current_x = Open_list[0][1]
    current_y = Open_list[0][2]
    Expanded_World[current_x][current_y] = count

    count = count +1

    if (current_x == goal[0] and current_y == goal[1]) :
        target_vector = Open_list[0]
        state = "Search End"
    


print (state)
print(target_vector)

print(Expanded_World[0])
print(Expanded_World[1])
print(Expanded_World[2])
print(Expanded_World[3])
print(Expanded_World[4])

current_x = goal[0]
current_y = goal[1]

Path = []
while(current_x != init[1] or current_y != init[2]):
    Path.append([current_x,current_y])
    x2 = current_x - movement[Action_World[current_x][current_y]][0]
    y2 = current_y - movement[Action_World[current_x][current_y]][1]

    Policy[x2][y2] = movement_sign[Action_World[current_x][current_y]]
    current_x = x2
    current_y = y2


Path.reverse()

print(Action_World[0])
print(Action_World[1])
print(Action_World[2])
print(Action_World[3])
print(Action_World[4])

print(Policy[0])
print(Policy[1])
print(Policy[2])
print(Policy[3])
print(Policy[4])

print("***********************************")
print(Path)