room = 0
levelFlag = True 
infoLevels = False

def setup():
    size(1280,720)
    noStroke()
    global mountain_img, defaultFont, map_img, info_img
    mountain_img = loadImage("menuScreenMountain.png")
    map_img = loadImage("levelSelectImage.png")
    defaultFont = createFont("SansSerif.plain", 25)
    info_img = loadImage("level info.png")
    
    
def draw():
    levels()
    global mountain_img, defaultFont
    global room, levelFlag 
    global map_img
    image(mountain_img, 0, 0, 1280, 720)

    if room == 0:
        textFont(defaultFont)
        text("Press the space bar to continue", 460, 680)
    elif room == 1:
        image(map_img, 0, 0, 1280, 720)
        fill(255,255,120)
        ellipse(265,502,100,50) #bottom left
        ellipse(363, 385, 100, 50) #middle center 
        ellipse(611, 385, 100, 50)# slightly down center middle ish 
        ellipse(856, 602, 100, 50)# to the right 
        
    
    
    
def keyPressed():
    global room, levelFlag 
    if room == 0 and key == ' ':
        room +=1
        
        
        
def levels():
    global room, infoLevels  
    if room == 1 and mouseX in range (215, 315) and mouseY in range(477, 527) and mousePressed:
            print("yes!!!, first" )
            infoLevels == True
    elif room == 1 and mouseX in range(313, 413) and mouseY in range(360, 410):
        print("YEs!, second")
    elif room == 1 and mouseX in range(561, 661) and mouseY in range(360, 410):
        print("yEs!!, third")
    elif room ==1 and mouseX in range(806, 906) and mouseY in range(577, 627):
        print("yes!, fourth")
    else:
        print("NO")
        
    
            
    
    
    
