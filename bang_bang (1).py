import random

class BattleShip:
    def __init__(self):
        self.team_name = "Bang"
        self.ships = ships
        self.opponent_board = opponent_board
        self.info = -1
        self.attack_type = 0 # 0 for parity,  1 for hunt and 2 for finish
        self.stack = []
        self.parity = parity
        self.hit_count = 0
        self.fix_direction = ""
        self.attack_status = "partial"
        self.direction = ['R', 'U', 'L', 'D']
        self.special_miss0 = []
        self.special_miss1 = []
        self.hawk_eye = 0
        self.counter = 0
        self.available_ships = [5,5,4,4,3]

    def set_ships(self):
        return self.ships
    
    def addition(self, lis1, lis2):
        for i in range(len(lis1)):
            for j in range(len(lis2[i])):
                lis1[i][j] += lis2[i][j]
        return lis1
    def amax(self, lis):
        x = -1000000
        for i in lis:
            for j in i:
                x = max(x, j)
        return x

    def where(self, lis, amaxi):
        l1 = []
        l2 = []
        for i in range(len(lis)):
            for j in range(len(lis[i])):
                if (lis[i][j]==amaxi):
                    l1.append(i)
                    l2.append(j)
        return [l1, l2]

    def HeatmapGenerator(self,Ship):
        opponent_board_heat =[
        [0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0]
        ,[0,0,0,0,0,0,0,0,0,0]
        ]
        
        goodx = 0
        goody = 0
        H1 = 0
        while H1 < 10:
            H2 = 0
            while H2 < 10:
                if self.opponent_board[H1][H2] != 1 and self.opponent_board[H1][H2] != 0:
                    if 9 - H2 >= (Ship-1):
                        for x in range(Ship):
                            if self.opponent_board[H1][H2+x] != 1 and self.opponent_board[H1][H2+x] != 0:
                                goodx += 1
                            else:
                                goodx -= 100
                            if self.opponent_board[H1][H2+x] == 0:
                                goodx += 10
                        if goodx > 0:    
                            for z in range(Ship):
                                opponent_board_heat[H1][H2+z] += 1
                        if goodx > 10:
                            for z in range(Ship):
                                opponent_board_heat[H1][H2+z] += 100
                    if self.opponent_board[H1][H2] == 0:
                        opponent_board_heat[H1][H2] -= 10000
                H2 += 1
                goodx = 0
            H1 += 1
        
        H2 = 0
        while H2 < 10:
            H1 = 0
            while H1 < 10:
                if self.opponent_board[H1][H2] != 1 and self.opponent_board[H1][H2] != 0:
                    if 9 - H1 >= (Ship-1):
                        for x in range(Ship):
                            if self.opponent_board[H1+x][H2] != 1 and self.opponent_board[H1+x][H2] != 0:
                                goody += 1
                            else:
                                goody -= 100
                            if self.opponent_board[H1+x][H2] == 0:
                                goody += 10
                        if goody > 0:
                            for z in range(Ship):
                                opponent_board_heat[H1+z][H2] += 1
                        if goody > 10:
                            for z in range(Ship):
                                opponent_board_heat[H1+z][H2] += 100
                    if self.opponent_board[H1][H2] == 0:
                        opponent_board_heat[H1][H2] -= 10000
                H1 += 1
                goody = 0
            H2 += 1
        return opponent_board_heat
    
    def attack(self):
        x = -1
        y = -1

        if self.hawk_eye == 1:
            #hawkeye attack
            for i in range(10):
                self.opponent_board[9][i] = 1
                self.opponent_board[i][9] = 1
                if([9,i] in self.parity):
                    self.parity.remove([9,i])
                if([i,9] in self.parity):
                    self.parity.remove([i,9])
            return (9,9)
        else:
            if self.attack_type == 0:
                if len(self.parity) != 0:
                    Heatmap_ALL = [
                    [0,0,0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0,0,0]
                    ,[0,0,0,0,0,0,0,0,0,0]]
                    
                    for i in self.available_ships:
                        Heatmap_ALL = self.addition(Heatmap_ALL,self.HeatmapGenerator(i))
                    next_guess = self.where(Heatmap_ALL, self.amax(Heatmap_ALL))
                    next_coordinates = list(zip(next_guess[0],next_guess[1]))
                    First = (next_coordinates[random.randint(1,len(next_coordinates))-1])
                    x1 = First[0]
                    y1 = First[1]
                    if [x1,y1] in self.parity:
                        x = First[0]
                        y = First[1]
                    else:   
                        rand_elem = random.choice(self.parity)
                        x = rand_elem[0]
                        y = rand_elem[1]
                else:
                    if len(self.special_miss1) != 0:
                        rand_elem = random.choice(self.special_miss1)
                        x = rand_elem[0]
                        y = rand_elem[1]
                        (self.special_miss1).remove([x,y])
                    elif len(self.special_miss0) != 0:
                        rand_elem = random.choice(self.special_miss0)
                        x = rand_elem[0]
                        y = rand_elem[1]
                        (self.special_miss0).remove([x,y])
            elif self.attack_type == 1:
                move = self.fix_direction
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x = self.stack[-1][0]
                    y = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x = self.stack[-1][0]
                    y = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x = self.stack[-1][0]-1
                    y = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x = self.stack[-1][0]+1
                    y = self.stack[-1][1]
            elif self.attack_type == 2:
                if(self.fix_direction=='L'):
                    x = self.stack[-1][0]
                    y = self.stack[-1][1]-1
                elif(self.fix_direction=='R'):
                    x = self.stack[-1][0]
                    y = self.stack[-1][1]+1
                elif(self.fix_direction=='U'):
                    x = self.stack[-1][0]-1
                    y = self.stack[-1][1]
                elif(self.fix_direction=='D'):
                    x = self.stack[-1][0]+1
                    y = self.stack[-1][1]
            if([x,y] in self.parity):
                (self.parity).remove([x,y])
            return (x, y)
    
    def hit_or_miss(self, x, y, info):
        self.info = info

        if self.attack_type == 0:
            if info == 0:
                self.opponent_board[x][y] = 0
                self.counter += 1
                if self.counter == self.available_ships[0]:
                    self.available_ships.remove(self.counter)
                    self.hit_count = 0
                self.attack_type = 1
                (self.stack).append([x, y]) 
                if(y-1<0 or self.opponent_board[x][y-1]!=-1):
                    self.direction.remove('L')
                if(y+1>9 or self.opponent_board[x][y+1]!=-1):
                    self.direction.remove('R')
                if(x-1<0  or self.opponent_board[x-1][y]!=-1):
                    self.direction.remove('U')
                if(x+1>9 or self.opponent_board[x+1][y]!=-1):
                    self.direction.remove('D')
                self.fix_direction = self.direction[self.hit_count]
            elif info == 1:
                self.opponent_board[x][y] = 1
                self.special_miss0.append([x,y])
            elif info == 2:
                self.opponent_board[x][y] = 0
                self.counter += 1
                if self.counter == self.available_ships[0]:
                    self.available_ships.remove(self.counter)
                    self.hit_count = 0
                self.attack_type = 1
                (self.stack).append([x, y]) 
                if(y-1<0 or self.opponent_board[x][y-1]!=-1):
                    self.direction.remove('L')
                if(y+1>9 or self.opponent_board[x][y+1]!=-1):
                    self.direction.remove('R')
                if(x-1<0  or self.opponent_board[x-1][y]!=-1):
                    self.direction.remove('U')
                if(x+1>9 or self.opponent_board[x+1][y]!=-1):
                    self.direction.remove('D')
                self.fix_direction = self.direction[self.hit_count]
            elif info == 3:
                self.opponent_board[x][y] = 0
                self.counter += 1
                if self.counter == self.available_ships[0]:
                    self.available_ships.remove(self.counter)
                    self.hit_count = 0
                self.attack_type = 1
                (self.stack).append([x, y]) 
                if(y-1<0 or self.opponent_board[x][y-1]!=-1):
                    self.direction.remove('L')
                if(y+1>9 or self.opponent_board[x][y+1]!=-1):
                    self.direction.remove('R')
                if(x-1<0  or self.opponent_board[x-1][y]!=-1):
                    self.direction.remove('U')
                if(x+1>9 or self.opponent_board[x+1][y]!=-1):
                    self.direction.remove('D')
                self.fix_direction = self.direction[self.hit_count]
                #hawkeye on
                self.hawkeye = 1
        elif self.attack_type == 1:
            if self.hawk_eye == 1:
                self.hawk_eye = 0
                if info == 0:
                    self.opponent_board[x][y] = 0
                    self.counter += 1
                    if self.counter == self.available_ships[0]:
                        self.available_ships.remove(self.counter)
                        self.hit_count = 0
                    self.attack_type = 2
                    self.fix_direction = self.direction[self.hit_count]
                else:
                    self.special_miss1.append([x,y])
                    self.attack_type = 2
                    self.opponent_board[x][y] = 1
                    self.fix_direction = self.direction[self.hit_count]
            elif info == 0:
                self.opponent_board[x][y] = 0
                self.counter += 1
                if self.counter == self.available_ships[0]:
                    self.available_ships.remove(self.counter)
                    self.hit_count = 0
                self.attack_type = 2
                (self.stack).append([x,y])
                self.fix_direction = self.direction[self.hit_count]
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
                    #next search point impossible
                    fix = False
                    self.attack_status = "complete"
                    pivot = self.stack[0]
                    self.stack = [pivot]
                    if(self.fix_direction=="L"):
                        if('R' in self.direction):
                            self.fix_direction = "R"
                            fix = True
                    elif(self.fix_direction=="R"):
                        if('L' in self.direction):
                            self.fix_direction = "L"
                            fix = True
                    elif(self.fix_direction=="U"):
                        if('D' in self.direction):
                            self.fix_direction = "D"
                            fix = True
                    elif(self.fix_direction=="D"):
                        if('U' in self.direction):
                            self.fix_direction = "U"
                            fix = True

                    if(not fix):
                        self.attack_type = 0
                        self.stack = []
                        self.hit_count = 0
                        self.fix_direction = ""
                        self.attack_status = "partial"
                        self.direction = ['R', 'U', 'L', 'D']
            elif info == 1:
                self.special_miss1.append([x,y])
                self.opponent_board[x][y] = 1
                if self.hit_count < len(self.direction)-1:
                    self.hit_count += 1
                    self.fix_direction = self.direction[self.hit_count]
                else:
                    self.attack_type = 0
                    self.stack = []
                    self.hit_count = 0
                    self.fix_direction = 0
                    self.attack_status = "partial"
                    self.direction = [2, -2, 1, -1]
            elif info == 2:
                self.opponent_board[x][y] = 0
                self.counter += 1
                if self.counter == self.available_ships[0]:
                    self.available_ships.remove(self.counter)
                    self.hit_count = 0
                self.attack_type = 2
                (self.stack).append([x,y])
                self.fix_direction = self.direction[self.hit_count]
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
                    fix = False
                    self.attack_status = "complete"
                    pivot = self.stack[0]
                    self.stack = [pivot]
                    if(self.fix_direction=="L"):
                        if('R' in self.direction):
                            self.fix_direction = "R"
                            fix = True
                    elif(self.fix_direction=="R"):
                        if('L' in self.direction):
                            self.fix_direction = "L"
                            fix = True
                    elif(self.fix_direction=="U"):
                        if('D' in self.direction):
                            self.fix_direction = "D"
                            fix = True
                    elif(self.fix_direction=="D"):
                        if('U' in self.direction):
                            self.fix_direction = "U"
                            fix = True

                    if(not fix):
                        self.attack_type = 0
                        self.stack = []
                        self.hit_count = 0
                        self.fix_direction = ""
                        self.attack_status = "partial"
                        self.direction = ['R', 'U', 'L', 'D']
            elif info == 3:
                self.opponent_board[x][y] = 0
                self.counter += 1
                if self.counter == self.available_ships[0]:
                    self.available_ships.remove(self.counter)
                    self.hit_count = 0
                self.attack_type = 2
                (self.stack).append([x,y])
                self.hawk_eye = 1
                self.fix_direction = self.direction[self.hit_count]
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
                    fix = False
                    self.attack_status = "complete"
                    pivot = self.stack[0]
                    self.stack = [pivot]
                    if(self.fix_direction=="L"):
                        if('R' in self.direction):
                            self.fix_direction = "R"
                            fix = True
                    elif(self.fix_direction=="R"):
                        if('L' in self.direction):
                            self.fix_direction = "L"
                            fix = True
                    elif(self.fix_direction=="U"):
                        if('D' in self.direction):
                            self.fix_direction = "D"
                            fix = True
                    elif(self.fix_direction=="D"):
                        if('U' in self.direction):
                            self.fix_direction = "U"
                            fix = True

                    if(not fix):
                        self.attack_type = 0
                        self.stack = []
                        self.hit_count = 0
                        self.fix_direction = ""
                        self.attack_status = "partial"
                        self.direction = ['R', 'U', 'L', 'D']
        elif self.attack_type == 2:
            if self.hawk_eye == 1:
                self.hawk_eye = 0
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
                    if(self.attack_status=="partial"):
                        fix = False
                        self.attack_status = "complete"
                        pivot = self.stack[0]
                        self.stack = [pivot]
                        if(self.fix_direction=="L"):
                            if('R' in self.direction):
                                self.fix_direction = "R"
                                fix = True
                        elif(self.fix_direction=="R"):
                            if('L' in self.direction):
                                self.fix_direction = "L"
                                fix = True
                        elif(self.fix_direction=="U"):
                            if('D' in self.direction):
                                self.fix_direction = "D"
                                fix = True
                        elif(self.fix_direction=="D"):
                            if('U' in self.direction):
                                self.fix_direction = "U"
                                fix = True
                        if(not fix):
                            self.attack_type = 0
                            self.stack = []
                            self.hit_count = 0
                            self.fix_direction = ""
                            self.attack_status = "partial"
                            self.direction = ['R', 'U', 'L', 'D']

                    elif(self.attack_status == "complete"):
                        self.attack_type = 0 # 0 for parity,  1 for hunt and 2 for finish
                        self.stack = []
                        self.hit_count = 0
                        self.fix_direction = ""
                        self.attack_status = "partial"
                        self.direction = ['R', 'U', 'L', 'D']
                if info == 0:
                    self.opponent_board[x][y] = 0
                    self.fix_direction = self.direction[self.hit_count]
                else:
                    self.special_miss1.append([x,y])
                    self.opponent_board[x][y] = 1
                    self.fix_direction = self.direction[self.hit_count]
            elif info == 0:
                self.opponent_board[x][y] = 0
                self.counter += 1
                if self.counter == self.available_ships[0]:
                    self.available_ships.remove(self.counter)
                    self.hit_count = 0
                (self.stack).append([x,y])
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
                    if(self.attack_status=="partial"):
                        fix = False
                        self.attack_status = "complete"
                        pivot = self.stack[0]
                        self.stack = [pivot]
                        if(self.fix_direction=="L"):
                            if('R' in self.direction):
                                self.fix_direction = "R"
                                fix = True
                        elif(self.fix_direction=="R"):
                            if('L' in self.direction):
                                self.fix_direction = "L"
                                fix = True
                        elif(self.fix_direction=="U"):
                            if('D' in self.direction):
                                self.fix_direction = "D"
                                fix = True
                        elif(self.fix_direction=="D"):
                            if('U' in self.direction):
                                self.fix_direction = "U"
                                fix = True
                        if(not fix):
                            self.attack_type = 0
                            self.stack = []
                            self.hit_count = 0
                            self.fix_direction = ""
                            self.attack_status = "partial"
                            self.direction = ['R', 'U', 'L', 'D']

                    elif(self.attack_status == "complete"):
                        self.attack_type = 0 # 0 for parity,  1 for hunt and 2 for finish
                        self.stack = []
                        self.hit_count = 0
                        self.fix_direction = ""
                        self.attack_status = "partial"
                        self.direction = ['R', 'U', 'L', 'D']
            elif info == 1:
                self.special_miss1.append([x,y])
                self.opponent_board[x][y] = 1
                if(self.attack_status=="partial"):
                    fix = False
                    self.attack_status = "complete"
                    pivot = self.stack[0]
                    self.stack = [pivot]
                    if(self.fix_direction=="L"):
                        if('R' in self.direction):
                            self.fix_direction = "R"
                            fix = True
                    elif(self.fix_direction=="R"):
                        if('L' in self.direction):
                            self.fix_direction = "L"
                            fix = True
                    elif(self.fix_direction=="U"):
                        if('D' in self.direction):
                            self.fix_direction = "D"
                            fix = True
                    elif(self.fix_direction=="D"):
                        if('U' in self.direction):
                            self.fix_direction = "U"
                            fix = True

                    if(not fix):
                        self.attack_type = 0
                        self.stack = []
                        self.hit_count = 0
                        self.fix_direction = ""
                        self.attack_status = "partial"
                        self.direction = ['R', 'U', 'L', 'D']

                elif(self.attack_status == "complete"):
                    self.attack_type = 0 # 0 for parity,  1 for hunt and 2 for finish
                    self.stack = []
                    self.hit_count = 0
                    self.fix_direction = ""
                    self.attack_status = "partial"
                    self.direction = ['R', 'U', 'L', 'D']
            elif info == 2:
                self.opponent_board[x][y] = 0
                self.counter += 1
                if self.counter == self.available_ships[0]:
                    self.available_ships.remove(self.counter)
                    self.hit_count = 0
                (self.stack).append([x,y])
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
                    if(self.attack_status=="partial"):
                        fix = False
                        self.attack_status = "complete"
                        pivot = self.stack[0]
                        self.stack = [pivot]
                        if(self.fix_direction=="L"):
                            if('R' in self.direction):
                                self.fix_direction = "R"
                                fix = True
                        elif(self.fix_direction=="R"):
                            if('L' in self.direction):
                                self.fix_direction = "L"
                                fix = True
                        elif(self.fix_direction=="U"):
                            if('D' in self.direction):
                                self.fix_direction = "D"
                                fix = True
                        elif(self.fix_direction=="D"):
                            if('U' in self.direction):
                                self.fix_direction = "U"
                                fix = True
                        if(not fix):
                            self.attack_type = 0
                            self.stack = []
                            self.hit_count = 0
                            self.fix_direction = ""
                            self.attack_status = "partial"
                            self.direction = ['R', 'U', 'L', 'D']

                    elif(self.attack_status == "complete"):
                        self.attack_type = 0 # 0 for parity,  1 for hunt and 2 for finish
                        self.stack = []
                        self.hit_count = 0
                        self.fix_direction = ""
                        self.attack_status = "partial"
                        self.direction = ['R', 'U', 'L', 'D']
            elif info == 3:
                self.opponent_board[x][y] = 0
                self.counter += 1
                if self.counter == self.available_ships[0]:
                    self.available_ships.remove(self.counter)
                    self.hit_count = 0
                (self.stack).append([x,y])
                self.hawk_eye = 1
                move = self.fix_direction
                x1 = -1
                y1 = -1
                if(move=='R' and self.stack[-1][1]+1<=9 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]+1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]+1
                elif(move=='L'and self.stack[-1][1]-1>=0 and self.opponent_board[self.stack[-1][0]][self.stack[-1][1]-1]==-1):
                    x1 = self.stack[-1][0]
                    y1 = self.stack[-1][1]-1
                elif(move=='U' and self.stack[-1][0]-1>=0 and self.opponent_board[self.stack[-1][0]-1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]-1
                    y1 = self.stack[-1][1]
                elif(move=='D' and self.stack[-1][0]+1<=9 and self.opponent_board[self.stack[-1][0]+1][self.stack[-1][1]]==-1):
                    x1 = self.stack[-1][0]+1
                    y1 = self.stack[-1][1]
                if x1 == -1 and y1 == -1:
                    if(self.attack_status=="partial"):
                        fix = False
                        self.attack_status = "complete"
                        pivot = self.stack[0]
                        self.stack = [pivot]
                        if(self.fix_direction=="L"):
                            if('R' in self.direction):
                                self.fix_direction = "R"
                                fix = True
                        elif(self.fix_direction=="R"):
                            if('L' in self.direction):
                                self.fix_direction = "L"
                                fix = True
                        elif(self.fix_direction=="U"):
                            if('D' in self.direction):
                                self.fix_direction = "D"
                                fix = True
                        elif(self.fix_direction=="D"):
                            if('U' in self.direction):
                                self.fix_direction = "U"
                                fix = True
                        if(not fix):
                            self.attack_type = 0
                            self.stack = []
                            self.hit_count = 0
                            self.fix_direction = ""
                            self.attack_status = "partial"
                            self.direction = ['R', 'U', 'L', 'D']

                    elif(self.attack_status == "complete"):
                        self.attack_type = 0 # 0 for parity,  1 for hunt and 2 for finish
                        self.stack = []
                        self.hit_count = 0
                        self.fix_direction = ""
                        self.attack_status = "partial"
                        self.direction = ['R', 'U', 'L', 'D']

ships = [
[0 ,0 ,4 ,1],
[9 ,0 ,5 ,1],
[5 ,3 ,4 ,1],
[7 ,6 ,3 ,1],
[0 ,9 ,5 ,0]]

parity = []
temp = 1
for i in range(10):
    temp = 1 - temp
    for j in range(10):
        if(temp==1):
            parity.append([i,j])
        temp = 1 - temp

opponent_board = []
for i in range(10):
    lis = []
    for j in range(10):
        lis.append(-1)
    opponent_board.append(lis)