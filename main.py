import random
import sys


class Initiation():
    def init(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == '--D' or sys.argv[1] == '-dubug':
                self.debug_mode = 1
        else:
            self.debug_mode = 0
        self.tile_sea = '\x1b[5;34;44m' + '〜' + '\x1b[0m'
        self.tile_ship = '\x1b[5;30;47m' + '□' + '\x1b[0m'
        self.tile_ship_dead = '\x1b[5;30;47m' + '■' + '\x1b[0m'
        self.tile_miss = '\x1b[5;31;44m' + '◌' + '\x1b[0m'
        self.turns = 0
        self.deck_alive = 20
        self.lops = []  # List of Players Ships
        self.loes = []  # List of Enemys Ships
        self.map_enemy = [[self.tile_sea] * 10 for i in range(10)]
        self.map_player = [[self.tile_sea] * 10 for i in range(10)]
        self.os = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
        self.ros = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'}
        self.ships_list = ('катер 1', 'катер 2', 'катер 3', 'катер 4', 'эсминец 1', 'эсминец 2', 'эсминец 3', 'крейсер 1', 'крейсер 2', 'линкор')
        self.ships = {'катер 1':1, 'катер 2':1, 'катер 3':1, 'катер 4':1, 'эсминец 1':2, 'эсминец 2':2, 'эсминец 3':2, 'крейсер 1':3, 'крейсер 2':3, 'линкор':4}
        main()


def warning(msg):
    print('\x1b[0;31;40m' + msg + '\x1b[0m')


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
    temp = tuple()  # Tuple of tuples of all enemy ships
    for os_y in range(len(I.loes)):
        for os_x in range(len(I.loes[os_y])):
            temp += (tuple(I.loes[os_y][os_x]),)
            if I.debug_mode == 1:
                I.map_enemy[I.loes[os_y][os_x][1]][I.loes[os_y][os_x][0]] = I.tile_ship
    for i in range(4):
        while True:
            x = random.randrange(10)
            y = random.randrange(10)
            if (x,y,1) not in temp and (x - 1,y - 1,1) not in temp and (x,y - 1,1) not in temp and (x + 1,y - 1,1) not in temp and (x - 1,y,1) not in temp and (x + 1,y,1) not in temp and (x - 1,y + 1,1) not in temp and (x,y + 1,1) not in temp and (x + 1,y + 1,1) not in temp:
                temp += ((x,y,1),)
                I.loes.append([[x,y,1]])
                if I.debug_mode == 1:
                    I.map_enemy[y][x] = I.tile_ship
                break


def draw():
    print(chr(27) + "[2J")
    for i in range(len(I.map_player)):
        if i == 0:
            print('  Противник         Флот ')
            print('  ABCDEFGHIJ        ABCDEFGHIJ ')
            print(' ╔══════════╗      ╔══════════╗')
            print('0║' + ''.join(I.map_enemy[i]) + '║     ' + '0║' + ''.join(I.map_player[i]) + '║')
        elif i == 9:
            print('9║' + ''.join(I.map_enemy[i]) + '║     ' + '9║' + ''.join(I.map_player[i]) + '║')
            print(' ╚══════════╝      ╚══════════╝')
        else:
            print(str(i) + '║' + ''.join(I.map_enemy[i]) + '║     ' + str(i) + '║' + ''.join(I.map_player[i]) + '║')


def place():
    if I.debug_mode == 0:
        for current_ship in range(len(I.ships_list)):
            while True:
                deck = I.ships[I.ships_list[current_ship]]
                try:
                    if current_ship < 4:
                        position = input('Где разместить {} (например: А0): '.format(I.ships_list[current_ship])).lower()
                        if len(position) == 2:
                            x,y = list(position)
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
                        if check_node(x, y):
                            I.map_player[y][x] = I.tile_ship
                            I.lops.append([x,y,1])
                            break
                        else:
                            raise
                    else:
                        position = input('Где и как разместить {} (например: HА0 или VA0): '.format(I.ships_list[current_ship])).lower()
                        if len(position) == 3:
                            z,x,y = list(position)
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
                        if z != 'h' and z != 'v':
                            warning('Неверное позиционирование (H)orizontal или (V)ertical')
                            raise
                        if check_multy(x, y, z, deck):
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
        I.lops[:0] = templates[strategy]
        temp = ()  # Tuple of tuples of all players ships
        for os_y in range(len(I.lops)):
            for os_x in range(len(I.lops[os_y])):
                temp += (tuple(I.lops[os_y][os_x]),)
                I.map_player[I.lops[os_y][os_x][1]][I.lops[os_y][os_x][0]] = I.tile_ship
        for i in range(4):
            while True:
                x = random.randrange(10)
                y = random.randrange(10)
                if (x,y,1) not in temp and (x - 1,y - 1,1) not in temp and (x,y - 1,1) not in temp and (x + 1,y - 1,1) not in temp and (x - 1,y,1) not in temp and (x + 1,y,1) not in temp and (x - 1,y + 1,1) not in temp and (x,y + 1,1) not in temp and (x + 1,y + 1,1) not in temp:
                    temp += ((x,y,1),)
                    I.lops.append([[x,y,1]])
                    I.map_player[y][x] = I.tile_ship
                    break
        draw()


def check_node(x, y):
    if y == 0:
        if x == 0 and I.map_player[y][x] == I.tile_sea and I.map_player[y + 1][x] == I.tile_sea and I.map_player[y + 1][x + 1] == I.tile_sea and I.map_player[y][x + 1] == I.tile_sea:
            return(True)
        elif x == 9 and I.map_player[y][x] == I.tile_sea and I.map_player[y + 1][x - 1] == I.tile_sea and I.map_player[y + 1][x] == I.tile_sea and I.map_player[y][x - 1] == I.tile_sea:
            return(True)
        elif I.map_player[y][x] == I.tile_sea and I.map_player[y + 1][x - 1] == I.tile_sea and I.map_player[y + 1][x] == I.tile_sea and I.map_player[y + 1][x + 1] == I.tile_sea and I.map_player[y][x - 1] == I.tile_sea and I.map_player[y][x + 1] == I.tile_sea:
            return(True)
        else:
            return(False)
    elif y == 9:
        if x == 0 and I.map_player[y][x] == I.tile_sea and I.map_player[y - 1][x] == I.tile_sea and I.map_player[y - 1][x + 1] == I.tile_sea and I.map_player[y][x + 1] == I.tile_sea:
            return(True)
        elif x == 9 and I.map_player[y][x] == I.tile_sea and I.map_player[y - 1][x - 1] == I.tile_sea and I.map_player[y - 1][x] == I.tile_sea and I.map_player[y][x - 1] == I.tile_sea:
            return(True)
        elif I.map_player[y][x] == I.tile_sea and I.map_player[y - 1][x - 1] == I.tile_sea and I.map_player[y - 1][x] == I.tile_sea and I.map_player[y - 1][x + 1] == I.tile_sea and I.map_player[y][x - 1] == I.tile_sea and I.map_player[y][x + 1] == I.tile_sea:
            return(True)
        else:
            return(False)
    else:
        if x == 0 and I.map_player[y][x] == I.tile_sea and I.map_player[y - 1][x] == I.tile_sea and I.map_player[y - 1][x + 1] == I.tile_sea and I.map_player[y][x + 1] == I.tile_sea and I.map_player[y + 1][x] == I.tile_sea and I.map_player[y + 1][x + 1] == I.tile_sea:
            return(True)
        elif x == 9 and I.map_player[y][x] == I.tile_sea and I.map_player[y - 1][x] == I.tile_sea and I.map_player[y - 1][x - 1] == I.tile_sea and I.map_player[y][x - 1] == I.tile_sea and I.map_player[y + 1][x] == I.tile_sea and I.map_player[y + 1][x - 1] == I.tile_sea:
            return(True)
        elif I.map_player[y][x] == I.tile_sea and I.map_player[y - 1][x - 1] == I.tile_sea and I.map_player[y - 1][x] == I.tile_sea and I.map_player[y - 1][x + 1] == I.tile_sea and I.map_player[y][x - 1] == I.tile_sea and I.map_player[y][x + 1] == I.tile_sea and I.map_player[y + 1][x - 1] == I.tile_sea and I.map_player[y + 1][x] == I.tile_sea and I.map_player[y + 1][x + 1] == I.tile_sea:
            return(True)
        else:
            return(False)


def check_multy(x, y, z, deck):
    temp = []
    if I.map_player[y][x] == I.tile_sea:
        if z == 'h':
            for node in range(deck):
                if I.map_player[y][x + node] != I.tile_sea:
                    return(False)
            if check_node(x,y) and check_node(x + (deck - 1),y):
                for i in range(deck):
                    I.map_player[y][x + i] = I.tile_ship
                    temp.append([x + node,y,1])
                I.lops.append(temp)
                return(True)
            else:
                return(False)
        else:
            for i in range(deck):
                if I.map_player[y + i][x] != I.tile_sea:
                    return(False)
                if check_node(x,y) and check_node(x,y + (deck - 1)):
                    for i in range(deck):
                        I.map_player[y + i][x] = I.tile_ship
                        temp.append([x,y + i,1])
                    I.lops.append(temp)
                    return(True)
                else:
                    return(False)
    else:
        return(False)


def shoot():
    while True:
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
                I.map_enemy[y][x] = I.tile_ship_dead
                draw()
                warning('Попадание!')
                I.deck_alive -= 1
            elif k == [1,1]:
                I.map_enemy[y][x] = I.tile_ship_dead
                draw()
                warning('Корабль потоплен!')
                I.deck_alive -= 1
                win_condition()
            else:
                if I.map_enemy[y][x] != I.tile_ship_dead:
                    I.map_enemy[y][x] = I.tile_miss
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
    deck_alive = 0
    if person == 'a':
        for ship in range(len(I.loes)):
            if [x,y,1] in I.loes[ship]:
                I.loes[ship][I.loes[ship].index([x,y,1])] = [x,y,0]
                for deck in range(len(I.loes[ship])):
                    deck_alive += I.loes[ship][deck][2]
                if deck_alive == 0:
                    for deck in range(len(I.loes[ship])):
                        x1,y1,z1 = list(I.loes[ship][deck])
                        for iii in range(8):
                            I.map_enemy[(0 if ((y1 - 1) < 0) else y1 - 1)][(0 if ((x1 - 1) < 0) else x1 - 1)] = \
                                I.map_enemy[(0 if ((y1 - 1) < 0) else y1 - 1)][x1] = I.map_enemy[(0 if ((y1 - 1) < 0) else y1 - 1)][(9 if ((x1 + 1) > 9) else x1 + 1)] = \
                                I.map_enemy[y1][(0 if ((x1 - 1) < 0) else x1 - 1)] = I.map_enemy[y1][(9 if ((x1 + 1) > 9) else x1 + 1)] = \
                                I.map_enemy[(9 if ((y1 + 1) > 9) else y1 + 1)][(0 if ((x1 - 1) < 0) else x1 - 1)] = I.map_enemy[(9 if ((y1 + 1) > 9) else y1 + 1)][x1] = \
                                I.map_enemy[(9 if ((y1 + 1) > 9) else y1 + 1)][(9 if ((x1 + 1) > 9) else x1 + 1)] = I.tile_miss
                    for deck in range(len(I.loes[ship])):
                        x1,y1,z1 = list(I.loes[ship][deck])
                        I.map_enemy[y1][x1] = I.tile_ship_dead
                    return([1,1])
                else:
                    return([1,0])
    else:
        for ship in range(len(I.lops)):
            if [x,y,1] in I.lops[ship]:
                I.lops[ship][I.lops[ship].index([x,y,1])] = [x,y,0]
                for deck in range(len(I.lops[ship])):
                    deck_alive += I.lops[ship][deck][2]
                if deck_alive == 0:
                    for deck in range(len(I.lops[ship])):
                        x1,y1,z1 = list(I.lops[ship][deck])
                        for iii in range(8):
                            I.map_player[(0 if ((y1 - 1) < 0) else y1 - 1)][(0 if ((x1 - 1) < 0) else x1 - 1)] = \
                                I.map_player[(0 if ((y1 - 1) < 0) else y1 - 1)][x1] = I.map_player[(0 if ((y1 - 1) < 0) else y1 - 1)][(9 if ((x1 + 1) > 9) else x1 + 1)] = \
                                I.map_player[y1][(0 if ((x1 - 1) < 0) else x1 - 1)] = I.map_player[y1][(9 if ((x1 + 1) > 9) else x1 + 1)] = \
                                I.map_player[(9 if ((y1 + 1) > 9) else y1 + 1)][(0 if ((x1 - 1) < 0) else x1 - 1)] = I.map_player[(9 if ((y1 + 1) > 9) else y1 + 1)][x1] = \
                                I.map_player[(9 if ((y1 + 1) > 9) else y1 + 1)][(9 if ((x1 + 1) > 9) else x1 + 1)] = I.tile_miss
                    for deck in range(len(I.lops[ship])):
                        x1,y1,z1 = list(I.lops[ship][deck])
                        I.map_player[y1][x1] = I.tile_ship_dead
                    return([1,1])
                else:
                    return([1,0])


def enemy_turn():
    x = random.randrange(10)
    y = random.randrange(10)
    shoot_result = shoot_check(x,y,'e')
    if shoot_result == [1,0] or shoot_result == [1,1]:
        I.map_player[y][x] = I.tile_ship_dead
        draw()
        input('{}{}, противник попал.'.format(I.ros[x],y))
        enemy_turn()
    else:
        print('{}{}, противник промазал.'.format(I.ros[x],y))
        pass


def win_condition():
    if I.deck_alive == 0:
        warning('Ты победил врага на {} ход!'.format(I.turns))
        sys.exit()
    else:
        print('{} палуб врага осталось'.format(I.deck_alive))


def main():
    enemy()
    draw()
    place()
    shoot()

if __name__ == '__main__':
    I = Initiation()
    I.init()
