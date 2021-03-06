import numpy as np
import matplotlib.pyplot as plt


def is_in_circle_obstacle(point, xpos, ypos, radius,clearance):  # checks if point is in circle
    if np.sqrt(np.square(ypos - point[1]) + np.square(xpos - point[0])) <= radius+clearance:
        return True
def sign(point1, point2, point3):
    return (point1[0] - point3[0]) * (point2[1] - point3[1]) - (point2[0] - point3[0]) * (point1[1] - point3[1])
def is_in_triangle_obstacle(point, three_points):  # checks if a point is in a triangle
    v1 = three_points[0]
    v2 = three_points[1]
    v3 = three_points[2]
    pt = point
    d1 = sign(pt, v1, v2)
    d2 = sign(pt, v2, v3)
    d3 = sign(pt, v3, v1)
    neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    if not (neg and pos):
        return True
def is_in_slot(point,point1,point2,clearance):  # checks if a point is in a slot or an offset line with clearance

    if is_in_circle_obstacle(point,point1[0],point1[1],0,clearance):
        return True
    if is_in_circle_obstacle(point, point2[0], point2[1], 0, clearance):
        return True


    perp_angle1 = np.arctan2(point1[1]-point2[1],point1[0]-point2[0])+np.pi/2
    perp_angle2 = np.arctan2(point1[1]-point2[1],point1[0]-point2[0])+(3.0/2.0)*np.pi

    point11 = [point1[0]+clearance*np.cos(perp_angle1),point1[1]+clearance*np.sin(perp_angle1)]
    point12 = [point1[0]+clearance*np.cos(perp_angle2),point1[1]+clearance*np.sin(perp_angle2)]
    point21 = [point2[0]+clearance*np.cos(perp_angle1),point2[1]+clearance*np.sin(perp_angle1)]
    point22 = [point2[0]+clearance*np.cos(perp_angle2),point2[1]+clearance*np.sin(perp_angle2)]

    if is_in_triangle_obstacle(point,[point11,point12,point21]):
        return True
    if is_in_triangle_obstacle(point,[point11,point12,point22]):
        return True
    if is_in_triangle_obstacle(point,[point22,point21,point11]):
        return True
    if is_in_triangle_obstacle(point,[point22,point21,point12]):
        return True
def is_not_on_map(point,clearance):  # checks to see if the point is actually on the map, has hardcoded values
    if point[0] < -5+clearance or point[0] > 5-clearance:
        return True
    if point[1] < -5+clearance or point[1] > 5-clearance:
        return True
def is_point_allowed(point,clearance):
    if is_not_on_map(point,clearance):
        return False
    if is_in_circle_obstacle(point,0,0,1,clearance):
        return False
    if is_in_circle_obstacle(point,2.1,-3.1,1,clearance):
        return False
    if is_in_circle_obstacle(point,2.1,3.1,1,clearance):
        return False
    if is_in_circle_obstacle(point,-2.1,-3.1,1,clearance):
        return False

    p1 = [-2.75,3.75] #----------------------one square
    p2 = [-2.75,2.25]
    p3 = [-1.25,3.75]
    p4 = [-1.25,2.25]

    if is_in_triangle_obstacle(point,[p1,p2,p3]): # ------------------------------------------triangles
        return False
    if is_in_triangle_obstacle(point,[p3,p4,p2]): # ------------------------------------------triangles
        return False
    if is_in_triangle_obstacle(point,[p1,p4,p2]): # ------------------------------------------triangles
        return False
    if is_in_triangle_obstacle(point,[p3,p4,p1]): # ------------------------------------------triangles
        return False
    if is_in_slot(point,p1,p2,clearance):
        return False
    if is_in_slot(point,p2,p3,clearance):
        return False
    if is_in_slot(point,p3,p4,clearance):
        return False
    if is_in_slot(point,p4,p1,clearance):
        return False
    if is_in_slot(point,p2,p4,clearance):
        return False

    p1 = [-4.75,0.75] #----------------------two square
    p2 = [-3.25,0.75]
    p3 = [-3.25,-0.75]
    p4 = [-4.75,-0.75]

    if is_in_triangle_obstacle(point,[p1,p2,p3]): # ------------------------------------------triangles
        return False
    if is_in_triangle_obstacle(point,[p3,p4,p2]): # ------------------------------------------triangles
        return False
    if is_in_triangle_obstacle(point,[p1,p4,p2]): # ------------------------------------------triangles
        return False
    if is_in_triangle_obstacle(point,[p3,p4,p1]): # ------------------------------------------triangles
        return False
    if is_in_slot(point,p1,p2,clearance):
        return False
    if is_in_slot(point,p2,p3,clearance):
        return False
    if is_in_slot(point,p3,p4,clearance):
        return False
    if is_in_slot(point,p4,p1,clearance):
        return False

    p1 = [4.75,0.75] #----------------------three square
    p2 = [3.25,0.75]
    p3 = [3.25,-0.75]
    p4 = [4.75,-0.75]

    if is_in_triangle_obstacle(point,[p1,p2,p3]): # ------------------------------------------triangles
        return False
    if is_in_triangle_obstacle(point,[p3,p4,p2]): # ------------------------------------------triangles
        return False
    if is_in_triangle_obstacle(point,[p1,p4,p2]): # ------------------------------------------triangles
        return False
    if is_in_triangle_obstacle(point,[p3,p4,p1]): # ------------------------------------------triangles
        return False
    if is_in_slot(point,p1,p2,clearance):
        return False
    if is_in_slot(point,p2,p3,clearance):
        return False
    if is_in_slot(point,p3,p4,clearance):
        return False
    if is_in_slot(point,p4,p1,clearance):
        return False
    return True

# Plots the entire map
#  plot circles -------------------------------
theta = np.linspace(0, 2*np.pi, 100)
r1 = 1
x1 = r1*np.cos(theta)
y1 = r1*np.sin(theta)
r2 = 1
x2 = r2*np.cos(theta) +(5.1-3)
y2 = r2*np.sin(theta) -3.1
r3 = 1
x3 = r3*np.cos(theta) + (5.1-3)
y3 = r3*np.sin(theta) + (5.1-2)
r4 = 1
x4 = r3*np.cos(theta) + (-5.1+3)
y4 = r3*np.sin(theta) + (-5.1+2)
fig, ax = plt.subplots(1)
ax.plot(x1,y1,'k')
ax.plot(x2,y2,'k')
ax.plot(x3,y3,'k')
ax.plot(x4,y4,'k')
# --------------plots the borders-----------------------
x1, y1 = [5,5], [-5, 5]
x2, y2 = [-5,-5], [-5, 5]
x3, y3 = [-5,5], [5, 5]
x4, y4 = [-5,5], [-5, -5]
plt.plot(x1, y1,'k', x2, y2,'k', x3, y3,'k', x4, y4,'k')
# plots the squares------------------------------------
x1, y1 = [-2.75,-2.75], [3.75, 2.25]
x2, y2 = [-2.75,-1.25], [3.75, 3.75]
x3, y3 = [-2.75,-1.25], [2.25, 2.25]
x4, y4 = [-1.25,-1.25], [3.75, 2.25]
plt.plot(x1, y1,'k', x2, y2,'k', x3, y3,'k', x4, y4,'k')
x1, y1 = [-4.75,-3.25], [0.75, 0.75]
x2, y2 = [-4.75,-3.25], [-0.75,-0.75]
x3, y3 = [-4.74,-4.75], [0.75, -0.75]
x4, y4 = [-3.25,-3.25], [0.75, -0.75]
plt.plot(x1, y1,'k', x2, y2,'k', x3, y3,'k', x4, y4,'k')
x1, y1 = [4.75,3.25], [0.75, 0.75]
x2, y2 = [4.75,3.25], [-0.75,-0.75]
x3, y3 = [4.74,4.75], [0.75, -0.75]
x4, y4 = [3.25,3.25], [0.75, -0.75]
plt.plot(x1, y1,'k', x2, y2,'k', x3, y3,'k', x4, y4,'k')

# Sets the plot characteristics
ax.set_aspect(1)
plt.xlim(-5.1,5.1)
plt.ylim(-5.1,5.1)
plt.title('A* non-holonomic', fontsize=8)


clearance = float(input('Clearance in meters: '))
# User inputs --------------------------------------
start_allowed = False
while not start_allowed:
    start_pt = (input('Start point in form X Y Theta: '))
    start_pt = [float(start_pt.split()[0]), float(start_pt.split()[1]),float(start_pt.split()[2])]
    start_allowed = is_point_allowed((start_pt[0],start_pt[1]),clearance)
goal_allowed = False
while not goal_allowed:
    goal_pt = (input('Goal point in form X Y: '))
    goal_pt = [float(goal_pt.split()[0]), float(goal_pt.split()[1])]
    goal_allowed = is_point_allowed(goal_pt,clearance)

wheel_rpms = input('Wheel RPMs in  rpm1 rpm2 : ')
wheel_rpms = [float(wheel_rpms.split()[0]), float(wheel_rpms.split()[1])]

# Hardcoded inputs ---------------------------------
robot_diameter = 0.354 # meters
wheel_diameter = 0.076 # meters
wheel_distance = 0.2 # this is not determined yet
goal_tolerance = .3
weight = 1
wheel_rpms = [.75,1.5] # max velocity is 0.65 m/s
clearance = clearance + robot_diameter/2
occupation_grid_size = 0.25  # used to make non-overlapping nodes
Timestep = .17  # time used to determine how long the robot will drive
path_ary = [] # will hold the final path

occupation_grid =  np.inf*np.ones((int(round(10/occupation_grid_size)), int(round(10/occupation_grid_size))))
plt.plot(start_pt[0],start_pt[1],'go',markersize=3)
plt.plot(goal_pt[0],goal_pt[1],'ro',markersize=3)
eight_actions = [[wheel_rpms[0],wheel_rpms[0]],
                 [wheel_rpms[1],wheel_rpms[1]],
                 [wheel_rpms[0],wheel_rpms[1]],
                 [wheel_rpms[1],wheel_rpms[0]],
                 [0,wheel_rpms[0]],
                 [wheel_rpms[0],0],
                 [0,wheel_rpms[1]],
                 [wheel_rpms[1],0]]

def get_grid_value(point):
    a1 = [int(round((point[0]+5)/occupation_grid_size))]
    a2 = [int(round((point[1]+5)/occupation_grid_size))]
    value = occupation_grid[a1,a2]
    return value
def set_grid_value(point,value):
    a1 = [int(round((point[0]+5)/occupation_grid_size))]
    a2 = [int(round((point[1]+5)/occupation_grid_size))]
    occupation_grid[a1,a2] = value




def cost_2_goal(point): # gives the cost to the goal from a given point
    if point[0] - goal_pt[0] == 0:
        cost = abs(point[1] - goal_pt[1])
    elif point[1] - goal_pt[1] == 0:
        cost = abs(point[0] - goal_pt[0])
    else:
        cost = np.sqrt(np.square(point[0] - goal_pt[0]) + np.square(point[1] - goal_pt[1]))
    return cost
def is_goal(point):  # checks if a point is also the goal
    if cost_2_goal(point) <= goal_tolerance: # this fix
        return True
def step_point_theta(UR,UL): # outputs (x,y,theta) for input (UR,UL) taken at x,y = 0
    t=0
    r=wheel_diameter/2
    L=wheel_distance
    X0,Y0 = 0,0
    dt=0.001
    X1=0
    Y1=0
    Theta0 = 0
    Theta1=Theta0
    while t<Timestep:
        t=t+dt
        X0=X0+X1
        Y0=Y0+Y1
        dx = (r/2)*(UL+UR)*np.cos(Theta1)*dt
        dy = (r/2)*(UL+UR)*np.sin(Theta1)*dt
        dtheta=(r/L)*(UR-UL)*dt # this is in radians
        X1=X1+dx
        Y1=Y1+dy
        Theta1=Theta1+25*dtheta # this is in radians

    X0 = X0+X1
    Y0 = Y0+Y1
    return X0,Y0,(np.rad2deg(Theta1)) # this returns degrees

general_actions = []   # Finds child states at x,y,theta=0, vectorize child states
for action in eight_actions:
    general_actions.append(step_point_theta(action[0],action[1]))
polar_actions = []
for action in general_actions:
    r = np.sqrt(np.square(action[0])+np.square(action[1]))
    thetan = np.rad2deg(np.arctan2(action[1],action[0])) # this is in radians
    polar_actions.append([r,thetan])

def possible_childern(point,angle):  # transpose and rotate child states with point and theta
    childeren = []
    for action in polar_actions:
        xpos_new = point[0] + action[0]*np.cos(np.deg2rad(action[1]+angle))
        ypos_new = point[1] + action[0]*np.sin(np.deg2rad(action[1]+angle))
        final_direction = action[1] + angle
        childeren.append([xpos_new,ypos_new,final_direction])
    return childeren
class node:  # makes nodes that will be used to save and explore child states

    def __init__(self, location, orientation, cost2come,cost2goal,value,parent,random):
        #global node_cnt
        self.loc = location
        self.orientation = orientation
        self.cost2come = cost2come
        self.cost2goal = cost2goal
        self.parent = parent
        self.value = cost2come + cost2goal
        self.random = random
        #self.counter = node_cnt
        #node_cnt += 1

start_node = node(location=[start_pt[0],start_pt[1]],
                  orientation=start_pt[2],
                  value=cost_2_goal(start_pt),
                  cost2come=0,
                  cost2goal=cost_2_goal(start_pt),
                  parent=None,
                  random =  np.random.uniform())  # used in the case that 2 nodes have the same cost
set_grid_value(start_pt,0)

def find_children(curr_node):  # finds the child states from a given node
    curr_location = curr_node.loc
    curr_orientation = curr_node.orientation
    curr_cost2come = curr_node.cost2come
    allowable_childern = []
    plausable_childern = possible_childern(curr_location,curr_orientation)
    for child in plausable_childern:

        child_distance = np.sqrt(np.square(curr_location[0]-child[0])+np.square(curr_location[1]-child[1]))
        proposed_child_value = curr_cost2come+child_distance+weight*cost_2_goal([child[0],child[1]])
        if is_point_allowed([child[0],child[1]],clearance) and proposed_child_value < get_grid_value([child[0],child[1]]):
            set_grid_value([child[0],child[1]],(proposed_child_value)) # set a new lowest value in the cost grid
            plt.pause(0.05)
            child_node = node(location=[child[0],child[1]],
                              orientation=child[2],
                              cost2come=curr_cost2come+child_distance,
                              cost2goal=cost_2_goal([child[0],child[1]]),
                              value=proposed_child_value,
                              random= np.random.uniform(),
                              parent=curr_node)
            allowable_childern.append([child_node.value,child_node.random,child_node])
    return allowable_childern

def find_path(curr_node):  # Draws the path to the goal on the map
    while(curr_node!=None):
        try:
            path_ary.append([curr_node.loc[0],curr_node.loc[1],curr_node.orientation])
            curr_node = curr_node.parent
            parent_node = curr_node.parent
            x1,y1 = [curr_node.loc[0],parent_node.loc[0]],[curr_node.loc[1],parent_node.loc[1]]
            plt.plot(x1,y1,'r')
        except:
            pass


def solver(l):  # finds the lowest cost in unexplored states, deletes the state, and adds child states

    goal_not_found = 1
    while goal_not_found:
        curr_node_ary = min(l)

        curr_node = curr_node_ary[2]
        plt.plot(curr_node.loc[0],curr_node.loc[1],'yo',markersize=.5)
        parent = curr_node.parent
        l.remove(min(l))
        if parent != None:
            x1,y1 = [curr_node.loc[0],parent.loc[0]],[curr_node.loc[1],parent.loc[1]]
            plt.plot(x1,y1,'b')
        if (is_goal(curr_node.loc)):
            find_path(curr_node)  # find the path to the start node by tracking the node's parent
            print("here we found a goal")
            goal_not_found = 0
        children_list = find_children(curr_node)  # a function to find possible children and update cost
        l = l + children_list  # adding possible children to the list
    return 1


l = [(start_node.value,start_node.random, start_node)]

print("Running..")
flag = solver(l)
if flag == 1:
    print("Path found!")
else:
    print("Solution not found... ")

plt.show()
path_ary = path_ary[::-1]
path_ary = np.array(path_ary)
np.savetxt('path.csv',path_ary,delimiter=",")
print(path_ary)
