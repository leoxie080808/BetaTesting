from enemy import Enemy
from yellow_dwarf import Yellow_Dwarf
from red_giant import Red_Orc
from tower import Tower
from circle import Circle
from square import Square
from ice_tower import Ice_Tower
from test import Tester
from level_one import Level_One

level_one = Level_One()
restart = True
levels = [1,2,3]
room = 0 
levelRoom = 0 
stars = [0,0,0]
proceedFlag = False

def setup():
    global tower_info, enemy_info, tutorial_page_2, regularFont, mountain_img, defaultFont, map_img, info_img, upgrades_popup, info_img_2
    size(1280, 720)
    noStroke()
    tester = Tester()
    tester.test_tower()
    tester.test_enemy()
    tester.test_level_one()
    regularFont = createFont("Lucida Sans Demibold", 12)
    
    tower_info = loadImage("tower_info.png")
    enemy_info = loadImage("enemy_info.png")
    tutorial_page_2 = loadImage("tutorial_part2.png")
    mountain_img = loadImage("menuScreenMountain.png")
    map_img = loadImage("levelSelectImage.png")
    defaultFont = createFont("SansSerif.plain", 25)
    info_img = loadImage("level info.png")
    upgrades_popup = loadImage("upgrades_unlockeed.png")
    info_img_2 = loadImage("updates.png")
    
    levelStatusTest()
    #drawingTest()
    
    
def draw():
    global level_one, room
    background(0)
    
    if room == 0:
        image(mountain_img, 0, 0, 1280, 720)
        textFont(defaultFont)
        text("Press the space bar to continue", 460, 680)
    elif room == 1:
        image(map_img, 0, 0, 1280, 720)
        fill(255,255,120)
        drawing()
        
        fill(255, 255, 0)
        totalStarSum = sum(stars) 
        text("Stars: " + str(totalStarSum), 1180, 100)
    elif room ==2:
       levelStatus()
       starCalculatorTest()
       #levelStatusTest()
    elif room ==3:
        #reverseLevel()
        #starTesting()
        level_one.playing_level = True
        level_one.draw_level()
        level_one.spawn_enemies()
        level_one.build_towers()
        show_tutorial()
        complete_level()
        if level_one.quit:
            room = 1
            level_one = Level_One()
        
def keyPressed():
    
    global room, levelFlag 
    if room == 0 and key == ' ':
        room +=1     

def mousePressed():
        """
        Increments the wave, allows for user to click towers and upgrade/build new ones
        Note: This function is long as placing code elsewhere seems to cause the code to potentially
        run multiple times
        """
        global level_one
        if level_one.playing_level:
            textFont(regularFont)
            level_one.increment_wave()
            level_one.select_land_plot()
            level_one.build_new_tower()
            level_one.tower_is_selected()
            level_one.upgrade_towers()
            level_one.increment_tutorial_page()
            if level_one.is_game_over() or level_one.is_level_passed():
                print("choosing option")
                level_one.choose_option()
                
def drawing():
    global room, levelRoom  
    for x in levels:
        if x == 1: 
            if level_one.completed:
                fill(100, 255, 0)
            else:
                fill(255,255,120)
            ellipse(265,502,100,50)
            if not level_one.playing_level and mouseX in range (215, 315) and mouseY in range(477, 527) and mousePressed:
                room = 2
                levelRoom = 1
                
        elif x == 2: 
            fill(255, 255, 120) 
            ellipse(363, 385, 100, 50)
            if not level_one.playing_level and mouseX in range(313, 413) and mouseY in range(360, 410) and mousePressed:
                room = 2
                levelRoom = 2
                
        elif x== 3:
            fill(255, 255, 120)
            ellipse(611, 485, 100, 50)
            if not level_one.playing_level and mouseX in range(561, 661) and mouseY in range(460, 510) and mousePressed:
                room = 2 
                levelRoom = 3

"""
def drawingTest():
    global room, levelRoom, level_one
     
    mouseX = 216
    mouseY = 488 
    mousePressed = True
    not level_one.playing_level
    drawing()    
    assert room == 2
 """   


def levelStatus():
    global room, levelRoom
    if levelRoom == 1:
        firstLevel()
    elif levelRoom == 2:
        secondLevel()
    elif levelRoom == 3:
        thirdLevel()
    elif levelRoom == 4:
        room =1

def levelStatusTest():
    global levelRoom, room 
    levelRoom = 4
    levelStatus()
    assert room == 1
    levelRoom = 0 
    room = 0
    
        
                              
                                                            
def starCalculatorTest():
    assert starCalculator(18) == 3
    assert starCalculator(6) == 1 
    assert starCalculator(12) == 2
    assert starCalculator(20) == 3 
    assert starCalculator(5) == 1
        
def show_tutorial():
    textFont(regularFont)
    if level_one.wave == 0:
        if level_one.tutorial_page == 1:
            image(tower_info, 320, 180, 640, 360)
            fill(178, 17, 17)
            rect(900, 540, 60, 40)
            fill(255)
            text("Next", 905, 560)
        if level_one.tutorial_page == 2:
            image(tutorial_page_2, 320, 180, 640, 360)
            fill(178, 17, 17)
            rect(900, 540, 60, 40)
            fill(255)
            text("Next", 905, 560)
        fill(255)
        text("Enemies come from here", 580, 10)
        if level_one.tutorial_page == 3:
            image(enemy_info, 320, 180, 640, 360)
            fill(178, 17, 17)
            rect(880, 540, 80, 40)
            fill(255)
            text("Okay, got it!", 882, 560)
    if not level_one.tier_two_locked and level_one.tutorial_page == 4:
        image(upgrades_popup, 320, 180, 640, 360)
        fill(178, 17, 17)
        rect(880, 540, 80, 40)
        fill(255)
        text("Okay, got it!", 882, 560)
    if not level_one.tier_three_locked and level_one.tutorial_page == 5:
        image(upgrades_popup, 320, 180, 640, 360)
        fill(178, 17, 17)
        rect(880, 540, 80, 40)
        fill(255)
        text("Okay, got it!", 882, 560)

def yesButton():
    global room, yesLevel 
    fill(0,250,12)
    rect(740,375,250,150)
    if mouseX in range(740, 1010) and mouseY in range(375, 425) and mousePressed:
        room = 3




def exitButtonLevels():
    global room 
    fill(210,0,0)
    ellipse(900 , 200, 50, 50)
    if mouseX in range(875, 925) and mouseY in range(175, 225) and mousePressed:
        room = 1
    

def firstLevel():
    print("THIS RUNS OKAY!")
    global level, room
    image(info_img, 0, 0,1280, 720)
    textFont(defaultFont)
    text("this is the first level", 460, 680)
    yesButton()
    exitButtonLevels()

def starTesting():
    global stars, levelRoom, room, proceedFlag 
    if proceedFlag == True:
        if mouseX in range(0,200) and mouseY in range (0,200) and mousePressed:
            stars[levelRoom-1] = 3
            room = 1
            
    elif mouseX in range(200,300) and mouseY in range(200,300) and mousePressed:
        room = 2


                
                        
                                
                                                
"""
def reverseLevel():
    global room, levelRoom, stars, proceedFlag  
    if levelRoom == 1:
        proceedFlag = True 
    elif stars[0] < 1 and levelRoom == 2 or stars[0] == 0 and levelRoom == 3:
        print("you must complete the previous level first")
        proceedFlag = False
    elif stars[0] > 0 and levelRoom ==2:
        proceedFlag = True 
    elif stars[1] < 1 and levelRoom ==3: 
        print("you must complete the previous level first")
        proceedFlag = False 
    else:
        proceedFlag = True 
"""
    
def starCalculator(lives):
    if lives >= 18: 
        return 3 
    elif lives <=7:
        return 1
    else: 
        return 2 
    
def secondLevel():
    global level, room, info_img_2
    image(info_img_2, 0, 0, 1280, 720) 
    textFont(defaultFont)
    #text("this is the second level", 460, 680)
    #yesButton()
    exitButtonLevels()

def thirdLevel():
    global level, room
    image(info_img_2, 0, 0, 1280, 720) 
    textFont(defaultFont) 
    #text("this is the third level", 460, 680) 
    #yesButton()
    exitButtonLevels()

def complete_level():
    if level_one.is_game_over():
        fill(63, 19, 19)
        rect(480, 370, 320, 180)
        fill(255)
        text("YOU LOSE", 580, 400)
        rect(480, 480, 320, 70)
        fill(1, 1, 1)
        text("QUIT", 500, 515)
        
    if level_one.is_level_passed():
        fill(63, 19, 19)
        rect(480, 370, 320, 180)
        fill(255)
        level_one.degree = starCalculator(level_one.lives)
        stars[0] = level_one.degree
        text("YOU WIN", 580, 400)
        text("Stars: " + str(level_one.degree), 580, 420)
        rect(480, 480, 320, 70)
        fill(1, 1, 1)
        text("QUIT", 500, 515)
        level_one.completed = True
        
