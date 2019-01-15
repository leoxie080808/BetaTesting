myList = [0,1,2,3]
flagOne = True 
flagTwo = False

def setup():
    size(900, 600)
    noStroke()
    
def draw():
    mouseHovering(flagOne, flagTwo)
    if flagOne == True:
        fill(120,120,120)
        rect(500,500,50,50)
    elif flagOne == False:
        fill(230,120,0)
        rect(500,500,50,50)
    
    if flagTwo == True:
        fill(120,0,230)
        rect(100,100,50,50)
    elif flagTwo == False:
        fill(0,0,120)
        rect(100,100,50,50)
    
    
    
def mouseHovering(x,y):
    global flagOne, flagTwo 
    if mouseX in range(200,300) and mouseY in range(200,300) and mousePressed:
        flagOne = False
        print("Yes")
    elif mouseX in range(400,500) and mouseY in range (200,300)and mousePressed:
        flagTwo = True
        print("Maybe")
    else:
        flagOne = True 
        flagTwo = False 
        print("No")
    return flagOne
    return flagTwo
    
