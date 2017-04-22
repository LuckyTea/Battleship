import sys
import random

class Initiation():
    def init(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == '--D' or sys.argv[1] == '-dubug':
                self.debug_mode = 1
        else:
            self.debug_mode = 0
        self.tile_sea = '\x1b[5;34;44m'+'〜'+'\x1b[0m'
        self.tile_ship = '\x1b[5;30;47m'+'□'+'\x1b[0m'
        self.tile_ship_dead = '\x1b[5;30;47m'+'■'+'\x1b[0m'
        self.tile_miss = '\x1b[5;31;44m'+'◌'+'\x1b[0m'
        self.turns = 0
        self.loas = []  # List of Ally Ships
        self.loes = []  # List of Enemy Ships
        self.e = [[self.tile_sea]*10 for i in range(10)]
        self.a = [[self.tile_sea]*10 for i in range(10)]
        self.os = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
        self.ros = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'}
        self.sl = ('катер 1', 'катер 2', 'катер 3', 'катер 4', 'эсминец 1', 'эсминец 2', 'эсминец 3', 'крейсер 1', 'крейсер 2', 'линкор')
        self.s = {'катер 1':1, 'катер 2':1, 'катер 3':1, 'катер 4':1, 'эсминец 1':2, 'эсминец 2':2, 'эсминец 3':2, 'крейсер 1':3, 'крейсер 2':3, 'линкор':4}
        main()

def warning(msg):
    print('\x1b[0;31;40m'+msg+'\x1b[0m')

def enemy():
    templates = [[[[0,4,1],[0,5,1]],[[9,0,1],[9,1,1]],[[9,3,1],[9,4,1]],[[0,0,1],[0,1,1],[0,2,1]],[[0,7,1],[0,8,1],[0,9,1]],[[9,6,1],[9,7,1],[9,8,1],[9,9,1]]],
                [[[0,5,1],[0,6,1]],[[0,8,1],[0,9,1]],[[2,4,1],[2,5,1]],[[2,0,1],[2,1,1],[2,2,1]],[[2,7,1],[2,8,1],[2,9,1]],[[0,0,1],[0,1,1],[0,2,1],[0,3,1]]],
                [[[9,5,1],[9,6,1]],[[9,8,1],[9,9,1]],[[7,4,1],[7,5,1]],[[7,0,1],[7,1,1],[7,2,1]],[[7,7,1],[7,8,1],[7,9,1]],[[9,0,1],[9,1,1],[9,2,1],[9,3,1]]],
                [[[0,2,1],[1,2,1]],[[5,0,1],[6,0,1]],[[8,0,1],[9,0,1]],[[3,2,1],[4,2,1],[5,2,1]],[[7,2,1],[8,2,1],[9,2,1]],[[0,0,1],[1,0,1],[2,0,1],[3,0,1]]],
                [[[0,7,1],[1,7,1]],[[8,7,1],[9,7,1]],[[0,9,1],[1,9,1]],[[3,9,1],[4,9,1],[5,9,1]],[[7,9,1],[8,9,1],[9,9,1]],[[3,7,1],[4,7,1],[5,7,1],[6,7,1]]],
                [[[9,0,1],[9,1,1]],[[0,6,1],[0,7,1]],[[0,9,1],[1,9,1]],[[0,0,1],[1,0,1],[2,0,1]],[[0,2,1],[0,3,1],[0,4,1]],[[4,0,1],[5,0,1],[6,0,1],[7,0,1]]],
                [[[6,0,1],[7,0,1]],[[1,9,1],[2,9,1]],[[9,4,1],[9,5,1]],[[9,0,1],[9,1,1],[9,2,1]],[[9,7,1],[9,8,1],[9,9,1]],[[4,9,1],[5,9,1],[6,9,1],[7,9,1]]]]
    strategy = random.randrange(len(templates))
    I.loes[:0] = templates[strategy]
    temp = ()
    for i in range(len(I.loes)):
        for ii in range(len(I.loes[i])):
            temp += (tuple(I.loes[i][ii]),)
            if I.debug_mode == 1:
                I.e[I.loes[i][ii][1]][I.loes[i][ii][0]] = I.tile_ship
    for i in range(4):
        while True:
            x = random.randrange(10)
            y = random.randrange(10)
            if (x,y,1) not in temp and (x-1,y-1,1) not in temp and (x,y-1,1) not in temp and (x+1,y-1,1) not in temp and (x-1,y,1) not in temp and (x+1,y,1) not in temp and (x-1,y+1,1) not in temp and (x,y+1,1) not in temp and (x+1,y+1,1) not in temp:
                temp += ((x,y,1),)
                I.loes.append([[x,y,1]])
                if I.debug_mode == 1:
                    I.e[y][x] = I.tile_ship
                break

def draw():
    print(chr(27) + "[2J")
    for i in range(len(I.a)):
        if i == 0:
            print('  Противник         Флот ')
            print('  ABCDEFGHIJ        ABCDEFGHIJ ')
            print(' ╔══════════╗      ╔══════════╗')
            print('0║'+''.join(I.e[i])+'║     '+'0║'+''.join(I.a[i])+'║')
        elif i == 9:
            print('9║'+''.join(I.e[i])+'║     '+'9║'+''.join(I.a[i])+'║')
            print(' ╚══════════╝      ╚══════════╝')
        else:
            print(str(i)+'║'+''.join(I.e[i])+'║     '+str(i)+'║'+''.join(I.a[i])+'║')
    
def place():
    if I.debug_mode == 0:
        for i in range(len(I.sl)):
            while True:
                ii = I.s[I.sl[i]]
                try:
                    if i < 4:
                        pos = input('Где разместить {} (например: А0): '.format(I.sl[i])).lower()
                        if len(pos) == 2:
                            x,y = list(pos)
                            x = I.os[x]
                            y = int(y)
                        else:
                            raise
                        if x not in range(0,10):
                            warning('Х за пределами')
                            raise
                        if y not in range(0,10):
                            warning('У за пределами')
                            raise
                        if check1(x, y):
                            I.a[y][x] = I.tile_ship
                            I.loas.append([x,y,1])
                            break
                        else:
                            raise
                    else:
                        pos = input('Где и как разместить {} (например: HА0 или VA0): '.format(I.sl[i])).lower()
                        if len(pos) == 3:
                            p,x,y = list(pos)
                            x = I.os[x]
                            y = int(y)
                        else:
                            raise
                        if x not in range(0,10):
                            warning('Х за пределами')
                            raise
                        if y not in range(0,10):
                            warning('У за пределами')
                            raise
                        if p != 'h' and p != 'v':
                            warning('Неверное позиционирование (H)orizontal или (V)ertical')
                            raise
                        if check2(x, y, ii, p):
                            break
                        else:
                            raise
                except KeyboardInterrupt:
                    warning('ABORT')
                    sys.exit()
                except:
                    print(sys.exc_info())
                    warning('Некорректные координаты.')
            draw()
    else:
        templates = [[[[0,4,1],[0,5,1]],[[9,0,1],[9,1,1]],[[9,3,1],[9,4,1]],[[0,0,1],[0,1,1],[0,2,1]],[[0,7,1],[0,8,1],[0,9,1]],[[9,6,1],[9,7,1],[9,8,1],[9,9,1]]],
                    [[[0,5,1],[0,6,1]],[[0,8,1],[0,9,1]],[[2,4,1],[2,5,1]],[[2,0,1],[2,1,1],[2,2,1]],[[2,7,1],[2,8,1],[2,9,1]],[[0,0,1],[0,1,1],[0,2,1],[0,3,1]]],
                    [[[9,5,1],[9,6,1]],[[9,8,1],[9,9,1]],[[7,4,1],[7,5,1]],[[7,0,1],[7,1,1],[7,2,1]],[[7,7,1],[7,8,1],[7,9,1]],[[9,0,1],[9,1,1],[9,2,1],[9,3,1]]],
                    [[[0,2,1],[1,2,1]],[[5,0,1],[6,0,1]],[[8,0,1],[9,0,1]],[[3,2,1],[4,2,1],[5,2,1]],[[7,2,1],[8,2,1],[9,2,1]],[[0,0,1],[1,0,1],[2,0,1],[3,0,1]]],
                    [[[0,7,1],[1,7,1]],[[8,7,1],[9,7,1]],[[0,9,1],[1,9,1]],[[3,9,1],[4,9,1],[5,9,1]],[[7,9,1],[8,9,1],[9,9,1]],[[3,7,1],[4,7,1],[5,7,1],[6,7,1]]],
                    [[[9,0,1],[9,1,1]],[[0,6,1],[0,7,1]],[[0,9,1],[1,9,1]],[[0,0,1],[1,0,1],[2,0,1]],[[0,2,1],[0,3,1],[0,4,1]],[[4,0,1],[5,0,1],[6,0,1],[7,0,1]]],
                    [[[6,0,1],[7,0,1]],[[1,9,1],[2,9,1]],[[9,4,1],[9,5,1]],[[9,0,1],[9,1,1],[9,2,1]],[[9,7,1],[9,8,1],[9,9,1]],[[4,9,1],[5,9,1],[6,9,1],[7,9,1]]]]
        strategy = random.randrange(len(templates))
        I.loas[:0] = templates[strategy]
        temp = ()
        for i in range(len(I.loas)):
            for ii in range(len(I.loas[i])):
                temp += (tuple(I.loas[i][ii]),)
                if I.debug_mode == 1:
                    I.a[I.loas[i][ii][1]][I.loas[i][ii][0]] = I.tile_ship
        for i in range(4):
            while True:
                x = random.randrange(10)
                y = random.randrange(10)
                if (x,y,1) not in temp and (x-1,y-1,1) not in temp and (x,y-1,1) not in temp and (x+1,y-1,1) not in temp and (x-1,y,1) not in temp and (x+1,y,1) not in temp and (x-1,y+1,1) not in temp and (x,y+1,1) not in temp and (x+1,y+1,1) not in temp:
                    temp += ((x,y,1),)
                    I.loas.append([[x,y,1]])
                    I.a[y][x] = I.tile_ship
                    break
        draw()

def check1(x, y):
    if y == 0:
        if x == 0 and I.a[y][x] == I.tile_sea and I.a[y+1][x] == I.tile_sea and I.a[y+1][x+1] == I.tile_sea and I.a[y][x+1] == I.tile_sea:
            return(True)
        elif x == 9 and I.a[y][x] == I.tile_sea and I.a[y+1][x-1] == I.tile_sea and I.a[y+1][x] == I.tile_sea and I.a[y][x-1] == I.tile_sea:
            return(True)
        elif I.a[y][x] == I.tile_sea and I.a[y+1][x-1] == I.tile_sea and I.a[y+1][x] == I.tile_sea and I.a[y+1][x+1] == I.tile_sea and I.a[y][x-1] == I.tile_sea and I.a[y][x+1] == I.tile_sea:
            return(True)
        else:
            return(False)
    elif y == 9:
        if x == 0 and I.a[y][x] == I.tile_sea and I.a[y-1][x] == I.tile_sea and I.a[y-1][x+1] == I.tile_sea and I.a[y][x+1] == I.tile_sea:
            return(True)
        elif x == 9 and I.a[y][x] == I.tile_sea and I.a[y-1][x-1] == I.tile_sea and I.a[y-1][x] == I.tile_sea and I.a[y][x-1] == I.tile_sea:
            return(True)
        elif I.a[y][x] == I.tile_sea and I.a[y-1][x-1] == I.tile_sea and I.a[y-1][x] == I.tile_sea and I.a[y-1][x+1] == I.tile_sea and I.a[y][x-1] == I.tile_sea and I.a[y][x+1] == I.tile_sea:
            return(True)
        else:
            return(False)
    else:
        if x == 0 and I.a[y][x] == I.tile_sea and I.a[y-1][x] == I.tile_sea and I.a[y-1][x+1] == I.tile_sea and I.a[y][x+1] == I.tile_sea and  I.a[y+1][x] == I.tile_sea and I.a[y+1][x+1] == I.tile_sea:
            return(True)
        elif x == 9 and I.a[y][x] == I.tile_sea and I.a[y-1][x] == I.tile_sea and I.a[y-1][x-1] == I.tile_sea and I.a[y][x-1] == I.tile_sea and  I.a[y+1][x] == I.tile_sea and I.a[y+1][x-1] == I.tile_sea:
            return(True)
        elif I.a[y][x] == I.tile_sea and I.a[y-1][x-1] == I.tile_sea and I.a[y-1][x] == I.tile_sea and I.a[y-1][x+1] == I.tile_sea and I.a[y][x-1] == I.tile_sea and I.a[y][x+1] == I.tile_sea and I.a[y+1][x-1] == I.tile_sea and I.a[y+1][x] == I.tile_sea and I.a[y+1][x+1] == I.tile_sea:
            return(True)
        else:
            return(False)

def check2(x, y, ii, z):
    temp = []
    if I.a[y][x] == I.tile_sea:
        if z == 'h':
            for i in range(ii):
                if I.a[y][x+i] != I.tile_sea:
                    return(False)
            if check1(x,y) and check1(x+(ii-1),y):
                for i in range(ii):
                    I.a[y][x+i] = I.tile_ship
                    temp.append([x+i,y,1])
                I.loas.append(temp)
                return(True)
            else:
                return(False)
        else:
            for i in range(ii):
                if I.a[y+i][x] != I.tile_sea:
                    return(False)
                print(x,y,'--',x,y+(ii-1))
                if check1(x,y) and check1(x,y+(ii-1)):
                    for i in range(ii):
                        I.a[y+i][x] = I.tile_ship
                        temp.append([x,y+i,1])
                    I.loas.append(temp)
                    return(True)
                else:
                    print(type(x), x, type(y),y)
                    return(False)
    else:
        return(False)

def shoot():
    while True:
        global stp
        I.turns = I.turns + 1
        try:
            pos = input('Наводка орудия (например: А0): ').lower()
            if len(pos) == 2:
                x,y = list(pos)
                x = I.os[x]
                y = int(y)
            else:
                raise
            if x not in range(0,10):
                warning('Х за пределами')
                raise
            if y not in range(0,10):
                warning('У за пределами')
                raise
            k = shoot_check(x,y,'a')
            if k == [1,0]:
                I.e[y][x] = I.tile_ship_dead
                draw()
                warning('Попадание!')
            elif k == [1,1]:
                I.e[y][x] = I.tile_ship_dead
                draw()
                warning('Корабль потоплен!')
                win_condition()
            else:
                if I.e[y][x] != I.tile_ship_dead:
                    I.e[y][x] = I.tile_miss
                draw()
                warning('Мимо!')
                enemy_turn()
        except KeyboardInterrupt:
            warning('ABORT')
            sys.exit()
        except SystemExit:
            sys.exit()
        except:
            print(sys.exc_info())
            warning('Некорректные координаты.')

def shoot_check(x,y,person):
    if person == 'a':
        for i in range(len(I.loes)):
            if [x,y,1] in I.loes[i]:
                I.loes[i][I.loes[i].index([x,y,1])] = [x,y,0]
                tmp = 0
                for ii in range(len(I.loes[i])):
                    tmp += I.loes[i][ii][2]
                if tmp == 0:
                    for ii in range(len(I.loes[i])):
                        x1,y1,z1 = list(I.loes[i][ii])
                        for iii in range(8):
                            I.e[(0 if ((y1-1) < 0) else y1-1)][(0 if ((x1-1) < 0) else x1-1)] = I.e[(0 if ((y1-1) < 0) else y1-1)][x1] = I.e[(0 if ((y1-1) < 0) else y1-1)][(9 if ((x1+1) > 9) else x1+1)] = I.e[y1][(0 if ((x1-1) < 0) else x1-1)] = I.e[y1][(9 if ((x1+1) > 9) else x1+1)] = I.e[(9 if ((y1+1) > 9) else y1+1)][(0 if ((x1-1) < 0) else x1-1)] = I.e[(9 if ((y1+1) > 9) else y1+1)][x1] = I.e[(9 if ((y1+1) > 9) else y1+1)][(9 if ((x1+1) > 9) else x1+1)] = I.tile_miss
                    for ii in range(len(I.loes[i])):
                        x1,y1,z1 = list(I.loes[i][ii])
                        I.e[y1][x1] = I.tile_ship_dead
                    return([1,1])
                else:
                    return([1,0])
    else:
        for i in range(len(I.loas)):
            if [x,y,1] in I.loas[i]:
                I.loas[i][I.loas[i].index([x,y,1])] = [x,y,0]
                tmp = 0
                for ii in range(len(I.loas[i])):
                    tmp += I.loas[i][ii][2]
                if tmp == 0:
                    for ii in range(len(I.loas[i])):
                        x1,y1,z1 = list(I.loas[i][ii])
                        for iii in range(8):
                            I.a[(0 if ((y1-1) < 0) else y1-1)][(0 if ((x1-1) < 0) else x1-1)] = I.a[(0 if ((y1-1) < 0) else y1-1)][x1] = I.a[(0 if ((y1-1) < 0) else y1-1)][(9 if ((x1+1) > 9) else x1+1)] = I.a[y1][(0 if ((x1-1) < 0) else x1-1)] = I.a[y1][(9 if ((x1+1) > 9) else x1+1)] = I.a[(9 if ((y1+1) > 9) else y1+1)][(0 if ((x1-1) < 0) else x1-1)] = I.a[(9 if ((y1+1) > 9) else y1+1)][x1] = I.a[(9 if ((y1+1) > 9) else y1+1)][(9 if ((x1+1) > 9) else x1+1)] = I.tile_miss
                    for ii in range(len(I.loas[i])):
                        x1,y1,z1 = list(I.loas[i][ii])
                        I.a[y1][x1] = I.tile_ship_dead
                    return([1,1])
                else:
                    return([1,0])

def enemy_turn():
    x = random.randrange(10)
    y = random.randrange(10)
    tmp = shoot_check(x,y,'e')
    if tmp == [1,0] or tmp == [1,1]:
        I.a[y][x] = I.tile_ship_dead
        draw()
        input('{}{}, противник попал.'.format(I.ros[x],y))
        enemy_turn()
    else:
        print('{}{}, противник промазал.'.format(I.ros[x],y))
        pass

def win_condition():
    tmp = 0
    for i in range(len(I.loes)):
        for ii in range(len(I.loes[i])):
            tmp += I.loes[i][ii][2]
    if tmp == 0:
        warning('Ты победил врага на {} ход!'.format(stp))
        sys.exit()
    else:
        print('{} палуб врага осталось'.format(tmp))

def main():
        enemy()
        draw()
        place()
        shoot()

if __name__ == '__main__':
    I = Initiation()
    I.init()