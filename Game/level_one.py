from enemy import Enemy
from yellow_dwarf import Yellow_Dwarf
from red_giant import Red_Orc
from orange_giant import Orange_Giant
from pink_bandit import Pink_Bandit
from tower import Tower
from circle import Circle
from square import Square
from ice_tower import Ice_Tower
import random

class Level_One:
    gold = 340
    lives = 20
    enemies = []
    towers = []
    
    land_plots = []
    land_plots.append([620, 170])
    land_plots.append([502, 220])
    land_plots.append([920, 430])
    land_plots.append([1050, 530])
    land_plots.append([1180, 427])
    land_plots.append([743, 263])
    land_plots.append([501, 100])
    land_plots.append([650, 260])
    land_plots.append([610, 384])
    build_tower = False
    tower_options = []
    tower_options.append([150, 640])
    tower_options.append([250, 640])
    build_loc = []
    
    wave = 0
    tutorial_page = 1
    done_spawning = False
    playing_level = False
    tier_two_locked = True
    tier_three_locked = True
    correct_mouse = False
    restart = False
    quit = False
    completed = False
    degree = 0
    
    def spawn_enemies(self):
        """
        Draws all enemies, and spawns new enemies as the wave increases
        """
        #adding enemies to the wave
        if not self.done_spawning:
            if self.wave == 1:
                for i in range(3):
                    self.enemies.append(Yellow_Dwarf(random.randint(557, 563), -10-(i*15)))
                for i in range(4):
                    self.enemies.append(Yellow_Dwarf(random.randint(557, 563), -140-(i*15)))
                self.done_spawning = True
            if self.wave == 2:
                self.enemies.append(Yellow_Dwarf(563, -10))
                self.enemies.append(Yellow_Dwarf(558, -20))
                self.enemies.append(Red_Orc(560, -45))
                self.enemies.append(Red_Orc(561, -65))
                for i in range(4):
                    self.enemies.append(Yellow_Dwarf(random.randint(557, 563), -160-(i*15)))
                self.done_spawning = True
            if self.wave == 3:
                self.enemies.append(Orange_Giant(560, -10))
                for i in range(3):
                    self.enemies.append(Yellow_Dwarf(random.randint(557, 563), -200-(i*15)))
                for i in range(2):
                    self.enemies.append(Red_Orc(random.randint(557, 563), -260-(i*15)))
                self.done_spawning = True
            if self.wave == 4:
                for i in range(3):
                    self.enemies.append(Red_Orc(random.randint(557, 563), -10-(i*17)))
                for i in range(6):
                    self.enemies.append(Yellow_Dwarf(random.randint(557, 563), -60-(i*15)))
                for i in range(3):
                    self.enemies.append(Red_Orc(random.randint(557, 563), -230-(i*21)))
                self.done_spawning = True
            if self.wave == 5:
                for i in range(3):
                    self.enemies.append(Red_Orc(random.randint(557, 563), -10-(i*17)))
                for i in range(2):
                    self.enemies.append(Pink_Bandit(random.randint(557, 563), -10-(i*20)))
                for i in range(5):
                    self.enemies.append(Red_Orc(random.randint(557, 563), -200-(i*20)))
                for i in range(6):
                    self.enemies.append(Yellow_Dwarf(random.randint(557, 563), -330-(i*15)))
                self.done_spawning = True
                print("wave 5 over!")
            if self.wave == 6:
                for i in range(2):
                    self.enemies.append(Red_Orc(random.randint(557, 563), -10-(i*30)))
                for i in range(3):
                    self.enemies.append(Pink_Bandit(random.randint(557, 563), -100-(i*20)))
                for i in range(2):
                    self.enemies.append(Orange_Giant(random.randint(557, 563), -160-(i*30)))
                for i in range(6):
                    self.enemies.append(Yellow_Dwarf(random.randint(557, 563), -300-(i*15)))
                for i in range(2):
                    self.enemies.append(Red_Orc(random.randint(557, 563), -420-(i*30)))
                self.done_spawning = True
            if self.wave == 7:
                for i in range(6):
                    self.enemies.append(Yellow_Dwarf(random.randint(557, 563), -10-(i*15)))
                for i in range(2):
                    self.enemies.append(Pink_Bandit(random.randint(557, 563), -100-(i*20)))
                for i in range(2):
                    self.enemies.append(Orange_Giant(random.randint(557, 563), -180-(i*30)))
                for i in range(3):
                    self.enemies.append(Red_Orc(random.randint(557, 563), -250-(i*20)))
                for i in range(3):
                    self.enemies.append(Orange_Giant(random.randint(557, 563), -340-(i*30)))
                for i in range(6):
                    self.enemies.append(Yellow_Dwarf(random.randint(557, 563), -480-(i*15)))
                for i in range(3):
                    self.enemies.append(Red_Orc(random.randint(557, 563), -600-(i*20)))
                for i in range(2):
                    self.enemies.append(Pink_Bandit(random.randint(557, 563), -700-(i*15)))
                self.done_spawning = True
        
        #drawing enemies
        for enemy in self.enemies:
            enemy.draw_enemy()
            enemy.update()
            if not enemy.is_living():
                self.gold += enemy.gold_worth
                self.enemies.remove(enemy)
            if enemy.course_passed:
                self.lives -= enemy.weight
                self.enemies.remove(enemy)
    
    def draw_level(self): 
        """
        Draws the path followed by the enemies, plots where towers can be 
        built, and other information
        """
        #Path
        fill(91, 160, 91)
        rect(545, -5, 30, 335)
        rect(545, 305, 250, 30)
        rect(800, 465, 485, 30)
        #Land plots
        fill("#f3f972")
        for plot in self.land_plots:
            ellipse(plot[0], plot[1], 30, 30)
        #Gold bar
        fill(255, 255, 0)
        text("Gold: " + str(self.gold), 100, 75)
        #Number of lives left
        fill(255, 10, 10)
        text("Lives: "+str(self.lives), 100, 55)
        #Spawn next wave
        fill(100, 100, 100)
        rect(100, 100, 50, 50)
        if len(self.enemies) == 0:
            fill(255)
            text("Click to spawn next wave", 100, 165)
        text("Wave: " + str(self.wave) + " / 7", 100, 180)
        #Show tutorial
    
    def build_towers(self):
        """
        Draws all towers, searches for nearby enemies, targets enemies, and attacks
        targets
        """
        for tower in self.towers:
            #tower.show_range()
            tower.draw_tower()
            if tower.is_selected:
                tower.show_range()
                fill(240, 240, 0)
                if tower.tier < 3:
                    rect(tower.xLoc-10, tower.yLoc-50, 20, 20)
                    if tower.tier == 1 and self.tier_two_locked:
                        text("Upgrade locked", tower.xLoc-45, tower.yLoc+40)
                    elif tower.tier == 2 and self.tier_three_locked:
                        text("Upgrade locked", tower.xLoc-45, tower.yLoc+40)
                    else:
                        text("Upgrade cost: " + str(tower.upgrade_cost), tower.xLoc-60, tower.yLoc+40)
                else:
                    text("Tower at max level!", tower.xLoc-50, tower.yLoc+40)
            if tower.trgtd_enmy != None and not tower.enemy_targeted:
                tower.target_enemy()
            elif tower.enemy_targeted and tower.trgtd_enmy != None and not tower.trgtd_enmy.is_invisible:
                tower.shoot_projectile()
                tower.detect_enemy_hit()
                # Note: Make it so that multiple towers can attack at the same time
            else:
                tower.find_enemy(self.enemies)
    
        if self.build_tower:
            fill(1, 139, 4)
            ellipse(150, 640, 30, 30)
            fill(204, 12, 2)
            rect(235, 625, 30, 30)
            fill(107, 166, 229)
            ellipse(350, 640, 30, 30)
            fill(240, 240, 10)
            text("Cost: 70", 125, 670)
            text("Cost: 90", 225, 670)
            text("Cost: 80", 325, 670)
    
    def build_new_tower(self):
        if self.gold >= 70 and self.build_tower and mouseX in range(135, 165) and mouseY in range(625, 655):
            self.towers.append(Circle(self.build_loc[0], self.build_loc[1]))
            self.gold -= 70
            print("tower built!")
            self.build_tower = False
            for plot in self.land_plots:
                if plot[0] == self.build_loc[0] and plot[1] == self.build_loc[1]:
                    self.land_plots.remove(plot)
            self.build_loc.pop(0)
            self.build_loc.pop(0)
        if self.gold >= 90 and self.build_tower and mouseX in range(235, 265) and mouseY in range(625, 655):
            self.towers.append(Square(self.build_loc[0], self.build_loc[1]))
            self.gold -= 90
            print("tower built!")
            self.build_tower = False
            for plot in self.land_plots:
                if plot[0] == self.build_loc[0] and plot[1] == self.build_loc[1]:
                    self.land_plots.remove(plot)
            self.build_loc.pop(0)
            self.build_loc.pop(0)
        if self.gold >= 80 and self.build_tower and mouseX in range(335, 365) and mouseY in range(625, 655):
            self.towers.append(Ice_Tower(self.build_loc[0], self.build_loc[1]))
            self.gold -= 80
            print("tower built!")
            self.build_tower = False
            for plot in self.land_plots:
                if plot[0] == self.build_loc[0] and plot[1] == self.build_loc[1]:
                    self.land_plots.remove(plot)
            self.build_loc.pop(0)
            self.build_loc.pop(0)
    
    def upgrade_towers(self):
        self.is_upgrade_locked()
        for tower in self.towers:
            selected = tower.is_selected
            enough_gold = self.gold >= tower.upgrade_cost
            mouseX_correct = mouseX in range(tower.xLoc-10, tower.xLoc+10)
            mouseY_correct = mouseY in range(tower.yLoc-50, tower.yLoc-30)
            if enough_gold and selected and mouseX_correct and mouseY_correct and tower.tier < 3:
                if tower.tier == 1 and not self.tier_two_locked:
                    self.gold -= tower.upgrade_cost
                    tower.upgrade()
                    tower.is_selected = False
                if tower.tier == 2 and not self.tier_three_locked:
                    self.gold -= tower.upgrade_cost
                    tower.upgrade()
                    tower.is_selected = False
                
    def is_upgrade_locked(self):
        if self.wave > 1:
            self.tier_two_locked = False
        if self.wave > 4:
            self.tier_three_locked = False
    
    def upgrade_towers(self):
        self.is_upgrade_locked()
        for tower in self.towers:
            selected = tower.is_selected
            enough_gold = self.gold >= tower.upgrade_cost
            mouseX_correct = mouseX in range(tower.xLoc-10, tower.xLoc+10)
            mouseY_correct = mouseY in range(tower.yLoc-50, tower.yLoc-30)
            if enough_gold and selected and mouseX_correct and mouseY_correct and tower.tier < 3:
                if tower.tier == 1 and not self.tier_two_locked:
                    self.gold -= tower.upgrade_cost
                    tower.upgrade()
                    tower.is_selected = False
                elif tower.tier == 2 and not self.tier_three_locked:
                    self.gold -= tower.upgrade_cost
                    tower.upgrade()
                    tower.is_selected = False
    
    def tower_is_selected(self):
        for tower in self.towers:
            if mouseX in range(tower.xLoc-25, tower.xLoc+25) and mouseY in range(tower.yLoc-25, tower.yLoc+25):
                if tower.is_selected:
                    tower.is_selected = False
                else:
                    tower.is_selected = True
                    
    def select_land_plot(self):
        for plot in self.land_plots:
            if mouseX in range(plot[0]-20, plot[0]+20) and mouseY in range(plot[1]-20, plot[1]+20):
                if self.build_tower:
                    self.build_tower = False
                    self.build_loc.pop(0)
                    self.build_loc.pop(0)
                else:
                    self.build_tower = True
                    self.build_loc.append(plot[0])
                    self.build_loc.append(plot[1])
    
    def increment_wave(self):
        if mouseX in range(100, 150) and mouseY in range(100, 150) and len(self.enemies) == 0 and self.wave < 7:
            self.wave += 1
            self.done_spawning = False
            print(self.wave)
    
    def increment_tutorial_page(self):
        if mouseX in range(900, 960) and mouseY in range(540, 580):
            self.tutorial_page += 1
    
    def is_game_over(self):
        if self.lives <= 0:
            return True
        return False
    
    def is_level_passed(self):
        if self.wave == 7 and len(self.enemies) == 0 and self.lives > 0:
            return True
        return False
    
    def choose_option(self):
        if mouseX in range(480, 800) and mouseY in range(480, 550):
            self.quit = True
            print("quit is true")
    
    
