import time

class Enemy:
    type = ""
    xLoc = -1
    yLoc = -1
    health = -1
    weight = -1
    speed = -1
    is_dead = False
    enemy_size = -1
    course_passed = False
    is_invisible = False
    gold_worth = -1
    slowed_speed = -1
    time_slowed = -1
    original_speed = -1
    is_slowed = False
        
    def is_living(self):
        if self.health <= 0:
            return False
        return True
        
    def update(self):
        if self.is_slowed:
            self.speed = self.slowed_speed
            if self.time_slowed <= time.time():
                self.is_slowed = False
                self.speed = self.original_speed
        if self.yLoc < 320:
            self.yLoc += self.speed
        elif round(self.xLoc) < 800:
            self.xLoc += self.speed
        elif round(self.xLoc) >= 800 and round(self.yLoc) < 480:
            self.is_invisible = True
            self.yLoc += self.speed
        elif round(self.yLoc) >= 480:
            self.is_invisible = False
            self.xLoc += self.speed
        if self.xLoc >= 1280:
            self.course_passed = True
