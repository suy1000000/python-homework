import simplegui
import random
import math

# initialize state
width = 800
height = 600
position = [int(width/2), int(height/2)]
word_position=[int(width/6),int(height/2)]
food_position=[random.randrange(0,width),random.randrange(0,height)]
radius = 15
radius_enemy=15
radius_ball=15
velocity = 1
counter=1
win_counter=0
start_or_not=False
lastkey =simplegui.KEY_MAP['down']
enemy_position=[random.randrange(0,width),random.randrange(0,height)]
enemy_position2=[random.randrange(0,width), random.randrange(0,height)]
enemy_position3=[random.randrange(0,width), random.randrange(0,height)]

#helper functions
def start_game():
    global start_or_not
    word_position=None
    start_or_not=not start_or_not
    timer.start()
    timer2.start()
    timer3.start()
    timer4.start()
    timer5.start()

def stop_handle():
    enemy_position=None
    enemy_position2=None
    enemy_position3=None
    posiotn=None
    food_position=None
    timer.stop()
    timer2.stop()
    timer3.stop()
    timer4.stop()
    timer5.stop()
def is_win():
    global win_counter,is_win
    if  win_counter==6:
        return True
    else:
        return False
def is_dead():
    global counter,is_dead
    if counter==0:
        return True
    elif (is_touched_by_enemy() or is_touched_by_enemy2() or is_touched_by_enemy3()):
        counter=counter-1
        return False
    else:
        return False
def is_touched():
    dis=math.sqrt((position[0]-food_position[0])**2+
                 (position[1]-food_position[1])**2)
    #print "dis:",dis
    if dis<=(radius+radius_ball):
        return True
    elif dis>(radius+radius_ball):
        return False
def is_touched_by_enemy():
    dis=math.sqrt((position[0]-enemy_position[0])**2+
                 (position[1]-enemy_position[1])**2)
    #print "dis:",dis
    if dis<=(radius_enemy+radius_ball):
        return True
    elif dis>(radius_enemy+radius_ball):
        return False
def is_touched_by_enemy2():
    dis=math.sqrt((position[0]-enemy_position2[0])**2+
                 (position[1]-enemy_position2[1])**2)
    #print "dis:",dis
    if dis<=(radius_enemy+radius_ball):
        return True
    elif dis>(radius_enemy+radius_ball):
        return False
def is_touched_by_enemy3():
    dis=math.sqrt((position[0]-enemy_position3[0])**2+
                 (position[1]-enemy_position3[1])**2)
    #print "dis:",dis
    if dis<=(radius_enemy+radius_ball):
        return True
    elif dis>(radius_enemy+radius_ball):
        return False


def food_enemy_touch():
    dis=math.sqrt((enemy_position[0]-food_position[0])**2+
                 (enemy_position[1]-food_position[1])**2)
    #print "dis:",dis
    if dis<=(radius+radius_enemy):
        return True
    elif dis>(radius+radius_enemy):
        return False
def food_enemy2_touch():
    dis=math.sqrt((enemy_position2[0]-food_position[0])**2+
                 (enemy_position2[1]-food_position[1])**2)
    #print "dis:",dis
    if dis<=(radius+radius_enemy):
        return True
    elif dis>(radius+radius_enemy):
        return False
def food_enemy3_touch():
    dis=math.sqrt((enemy_position3[0]-food_position[0])**2+
                 (enemy_position3[1]-food_position[1])**2)
    #print "dis:",dis
    if dis<=(radius+radius_enemy):
        return True
    elif dis>(radius+radius_enemy):
        return False

    
def food_position_change():
    if is_touched():
        #print "touch"
        global radius_ball,win_counter
        win_counter+=1
        if radius_ball <=20:
            radius_ball+=5
        food_position[0]=random.randrange(0,width)
        food_position[1]=random.randrange(0,height)
    if food_enemy_touch():
        global radius_enemy
        if radius_enemy<=50:
            radius_enemy+=10
        food_position[0]=random.randrange(0,width)
        food_position[1]=random.randrange(0,height)
    if food_enemy2_touch():
        if radius_enemy<=150:
            radius_enemy+=25
        food_position[0]=random.randrange(0,width)
        food_position[1]=random.randrange(0,height)
    if food_enemy3_touch():
        if radius_enemy<=100:
            radius_enemy+=15
        food_position[0]=random.randrange(0,width)
        food_position[1]=random.randrange(0,height)
    else:
        #print "NO"
        food_position[0]= food_position[0]
        food_position[1]= food_position[1]

        
def distanceX_with_wall():
    disX=math.fabs(width-enemy_position[0])
    return disX
def distanceY_with_wall():
    disY=math.fabs(height-enemy_position[1])
    return disY
# event handlers
def keydown(key):
    global lastkey
    if key==simplegui.KEY_MAP['space']:
        start_game()
    elif key == simplegui.KEY_MAP['down']:
        position[1] = position[1] + velocity
        lastkey=simplegui.KEY_MAP['down']
    elif key == simplegui.KEY_MAP['up']:
        position[1] = position[1] - velocity
        lastkey=simplegui.KEY_MAP['up']
    elif key == simplegui.KEY_MAP['right']:
        position[0] = position[0] + velocity
        lastkey=simplegui.KEY_MAP['right']
    elif key == simplegui.KEY_MAP['left']:
        position[0] = position[0] - velocity
        lastkey=simplegui.KEY_MAP['left']

def draw(canvas):
    global start_or_not
    if  (not start_or_not):
        global counter,win_counter
        canvas.draw_text("Please click Space to Start the Game",word_position,40,"Yellow")
        counter=1
        win_counter=0
    if  (not is_dead())and start_or_not and (not is_win()):
        canvas.draw_circle(position, radius_ball,2, "white", "white")
        canvas.draw_circle(food_position,radius,2,"yellow","yellow")
        canvas.draw_circle(enemy_position,radius_enemy,2,"Red","Red")
        canvas.draw_circle(enemy_position2,radius_enemy,2,"Red","Red")
        canvas.draw_circle(enemy_position3,radius_enemy,2,"Red","Red")
        
    elif is_dead():
        canvas.draw_text("You lose.",word_position,40,"Red")
        stop_handle()
    elif is_win():
        canvas.draw_text("You win.",word_position,40,"Yellow")
        stop_handle()
def tick():
    food_position_change()
    if lastkey == simplegui.KEY_MAP['down']:
        position[1] = (position[1] + velocity)%height
    elif lastkey == simplegui.KEY_MAP['up']:
        position[1] = (position[1] - velocity)%height
    elif lastkey == simplegui.KEY_MAP['right']:
        position[0] = (position[0] + velocity)%width
    elif lastkey == simplegui.KEY_MAP['left']:
        position[0] = (position[0] - velocity)%width
def tick2():
    disX=distanceX_with_wall()
    disY=distanceY_with_wall()
    '''
    if disX==0 or disX==width:
        enemy_position[0]=(enemy_position[0]+velocity)%width
     
        enemy_position[1]=(enemy_position[1]+velocity)%height       
        
    elif disY==0 or disY==height:
        enemy_position[1]=(enemy_position[1]+velocity)%height
        
        enemy_position[0]=(enemy_position[1]+velocity)%width
      
    else:
    '''
    enemy_position[0]=(enemy_position[0]+velocity)%width
    enemy_position[1]=(enemy_position[1]+velocity)%height
def tick3():
    disX=distanceX_with_wall()
    disY=distanceY_with_wall()
    '''
        if disX==0 or disX==width:
        enemy_position2[0]=(enemy_position2[0]-velocity)%width
     
        enemy_position2[1]=(enemy_position2[1]+velocity)%height       
        
    elif disY==0 or disY==height:
        enemy_position2[1]=(enemy_position2[1]+velocity)%height
        
        enemy_position2[0]=(enemy_position2[1]-velocity)%width
     
    else:
    '''
    enemy_position2[0]=(enemy_position2[0]-velocity)%width
    enemy_position2[1]=(enemy_position2[1]+velocity)%height
def tick4():
    disX=distanceX_with_wall()
    disY=distanceY_with_wall()
    '''
    if disX==0 or disX==width:
        enemy_position3[0]=(enemy_position3[0]+velocity)%width
     
        enemy_position3[1]=(enemy_position3[1]+velocity)%height       
        
    elif disY==0 or disY==height:
        enemy_position3[1]=(enemy_position3[1]+velocity)%height
        
        enemy_position3[0]=(enemy_position3[1]+velocity)%width
      
    else:
    '''
    enemy_position3[0]=(enemy_position3[0]+velocity)%width
    enemy_position3[1]=(enemy_position3[1]-velocity)%height  
def tick5():
    print "counter:",counter
    print "win:",win_counter

# create frame
frame = simplegui.create_frame("Ball eat Ball", width, height)
timer=simplegui.create_timer(5,tick)
timer2=simplegui.create_timer(1,tick2)
timer3=simplegui.create_timer(2,tick3)
timer4=simplegui.create_timer(3,tick4)
timer5=simplegui.create_timer(1000,tick5)
# register event handlers
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# start frame
frame.start()
