'''
Information placeholder
'''
import random
import sys


class Initiation():
    def init(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == '--D' or sys.argv[1] == '-dubug':
                self.debug_mode = 1
        else:
            self.debug_mode = 0
        self.tile_sea = '\x1b[5;34;44m' + ' ' + '\x1b[0m'
        self.tile_ship = '\x1b[5;30;47m' + '□' + '\x1b[0m'
        self.tile_ship_dead = '\x1b[5;30;47m' + '■' + '\x1b[0m'
        self.tile_miss = '\x1b[5;37;44m' + '◌' + '\x1b[0m'
        self.tile_border = '\x1b[5;34;44m' + '║' + '\x1b[0m'
        self.turns = 0
        self.deck_enemy = 20
        self.deck_player = 20
        self.lops = []                                                                   # List of Players Ships
        self.loes = []                                                                   # List of Enemys Ships
        self.map_enemy = [[self.tile_sea] * 10 for i in range(10)]
        self.map_player = [[self.tile_sea] * 10 for i in range(10)]
        self.os = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
        self.ros = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'}
        self.ships_list = ('submarine  1', 'submarine  2', 'submarine  3', 'submarine  4', 'destroyer 1', 'destroyer 2', 'destroyer 3', 'cruiser 1', 'cruiser 2', 'battleship')
        self.ships = dict(zip(self.ships_list,(1,1,1,1,2,2,2,3,3,4)))
        self.x = 10
        self.y = 10
        self.position = 0
        main()


def warning(msg):
    print('\x1b[0;31;40m' + msg + '\x1b[0m')


def qucik_place(person):
    if person == 'enemy':
        los = I.loes
        map = I.map_enemy
    else:
        los = I.lops
        map = I.map_player
    templates = [[[[0,4,1],[0,5,1]],[[9,0,1],[9,1,1]],[[9,3,1],[9,4,1]],[[0,0,1],[0,1,1],[0,2,1]],[[0,7,1],[0,8,1],[0,9,1]],[[9,6,1],[9,7,1],[9,8,1],[9,9,1]]],
                 [[[0,5,1],[0,6,1]],[[0,8,1],[0,9,1]],[[2,4,1],[2,5,1]],[[2,0,1],[2,1,1],[2,2,1]],[[2,7,1],[2,8,1],[2,9,1]],[[0,0,1],[0,1,1],[0,2,1],[0,3,1]]],
                 [[[9,5,1],[9,6,1]],[[9,8,1],[9,9,1]],[[7,4,1],[7,5,1]],[[7,0,1],[7,1,1],[7,2,1]],[[7,7,1],[7,8,1],[7,9,1]],[[9,0,1],[9,1,1],[9,2,1],[9,3,1]]],
                 [[[0,2,1],[1,2,1]],[[5,0,1],[6,0,1]],[[8,0,1],[9,0,1]],[[3,2,1],[4,2,1],[5,2,1]],[[7,2,1],[8,2,1],[9,2,1]],[[0,0,1],[1,0,1],[2,0,1],[3,0,1]]],
                 [[[0,7,1],[1,7,1]],[[8,7,1],[9,7,1]],[[0,9,1],[1,9,1]],[[3,9,1],[4,9,1],[5,9,1]],[[7,9,1],[8,9,1],[9,9,1]],[[3,7,1],[4,7,1],[5,7,1],[6,7,1]]],
                 [[[9,0,1],[9,1,1]],[[0,6,1],[0,7,1]],[[0,9,1],[1,9,1]],[[0,0,1],[1,0,1],[2,0,1]],[[0,2,1],[0,3,1],[0,4,1]],[[4,0,1],[5,0,1],[6,0,1],[7,0,1]]],
                 [[[6,0,1],[7,0,1]],[[1,9,1],[2,9,1]],[[9,4,1],[9,5,1]],[[9,0,1],[9,1,1],[9,2,1]],[[9,7,1],[9,8,1],[9,9,1]],[[4,9,1],[5,9,1],[6,9,1],[7,9,1]]]]
    strategy = random.randrange(len(templates))
    los[:0] = templates[strategy]
    temp = tuple()                                                                       # Tuple of tuples of all ships
    for os_y in range(len(los)):
        for os_x in range(len(los[os_y])):
            temp += (tuple(los[os_y][os_x]),)
            if I.debug_mode == 1 or person != 'enemy':
                map[los[os_y][os_x][1]][los[os_y][os_x][0]] = I.tile_ship
    for i in range(4):
        while True:
            x = random.randrange(10)
            y = random.randrange(10)
            if (x,y,1) not in temp and (x - 1,y - 1,1) not in temp and (x,y - 1,1) not in temp and (x + 1,y - 1,1) not in temp and (x - 1,y,1) not in temp and (x + 1,y,1) not in temp and (x - 1,y + 1,1) not in temp and (x,y + 1,1) not in temp and (x + 1,y + 1,1) not in temp:
                temp += ((x,y,1),)
                los.append([[x,y,1]])
                if I.debug_mode == 1 or person != 'enemy':
                    map[y][x] = I.tile_ship
                break
    draw()


def draw():
    print(chr(27) + "[2J")
    print('  Enemy Ships                Your Ships')
    print('  A B C D E F G H I J        A B C D E F G H I J')
    print(' ╔{0}╗      ╔{0}╗'.format('═' * 19))
    for line in range(10):
        print('{0}║{1}║{0:>6}║{2}║'.format(line, I.tile_border.join(I.map_enemy[line]), I.tile_border.join(I.map_player[line])))
    print(' ╚{0}╝      ╚{0}╝'.format('═' * 19))


def place():
    if I.debug_mode == 0:
        for current_ship in range(len(I.ships_list)):
            while True:
                deck = I.ships[I.ships_list[current_ship]]
                try:
                    if current_ship < 4:
                        position = input('Where to arrange the {} (example: А0): '.format(I.ships_list[current_ship])).lower()
                        if len(position) == 2:
                            x,y = list(position)
                            x = I.os[x]
                            y = int(y)
                        else:
                            raise Exception('Incorrect coordinates')
                        if check_node(x, y):
                            I.map_player[y][x] = I.tile_ship
                            I.lops.append([[x,y,1]])
                            break
                        else:
                            raise Exception('Incorrect coordinates')
                    else:
                        position = input('Where to arrange the {} (example: HА0 or VA0): '.format(I.ships_list[current_ship])).lower()
                        if len(position) == 3:
                            z,x,y = list(position)
                            x = I.os[x]
                            y = int(y)
                        else:
                            raise Exception('Incorrect coordinates')
                        if z != 'h' and z != 'v':
                            raise Exception('Incorrect positioning [H]orizontal or [V]ertical')
                        if check_multy(x, y, z, deck):
                            break
                        else:
                            raise Exception('Incorrect coordinates')
                except KeyboardInterrupt:
                    warning('\nABORT')
                    sys.exit()
                except:
                    warning(str(sys.exc_info()[1]))
            draw()
    else:
        qucik_place('player')


def check_node(x, y):
    if y == 0:
        if x == 0 and I.map_player[y][x] == I.map_player[y + 1][x] == I.map_player[y + 1][x + 1] == I.map_player[y][x + 1] == I.tile_sea:
            return True
        elif x == 9 and I.map_player[y][x] == I.map_player[y + 1][x] == I.map_player[y + 1][x - 1] == I.map_player[y][x - 1] == I.tile_sea:
            return True
        elif I.map_player[y][x] == I.map_player[y + 1][x] == I.map_player[y + 1][x - 1] == I.map_player[y][x - 1] == I.map_player[y][x + 1] == I.map_player[y + 1][x + 1] == I.tile_sea:
            return True
    elif y == 9:
        if x == 0 and pattern_a(x, y):
            return True
        elif x == 9 and pattern_b(x, y):
            return True
        elif pattern_b(x, y) and I.map_player[y][x + 1] == I.map_player[y - 1][x + 1] == I.tile_sea:
            return True
    else:
        if x == 0 and pattern_a(x, y) and I.map_player[y + 1][x] == I.map_player[y + 1][x + 1] == I.tile_sea:
            return True
        elif x == 9 and pattern_b(x, y) and I.map_player[y + 1][x] == I.map_player[y + 1][x - 1] == I.tile_sea:
            return True
        elif pattern_b(x, y) and I.map_player[y][x + 1] == I.map_player[y + 1][x + 1] == I.map_player[y][x - 1] == I.map_player[y - 1][x + 1] == I.map_player[y + 1][x - 1] == I.map_player[y + 1][x] == I.tile_sea:
            return True


def pattern_a(x, y):
    return True if I.map_player[y][x] == I.map_player[y - 1][x] == I.map_player[y - 1][x + 1] == I.map_player[y][x + 1] == I.tile_sea else False


def pattern_b(x, y):
    return True if I.map_player[y][x] == I.map_player[y - 1][x] == I.map_player[y - 1][x - 1] == I.map_player[y][x - 1] == I.tile_sea else False


def check_multy(x, y, z, deck):
    temp = []
    if I.map_player[y][x] == I.tile_sea:
        if z == 'h':
            for node in range(deck):
                if I.map_player[y][x + node] != I.tile_sea:
                    return(False)
            if check_node(x, y) and check_node(x + (deck - 1), y):
                for node in range(deck):
                    I.map_player[y][x + node] = I.tile_ship
                    temp.append([x + node, y, 1])
                I.lops.append(temp)
                return(True)
        else:
            for node in range(deck):
                if I.map_player[y + node][x] != I.tile_sea:
                    return(False)
                if check_node(x, y) and check_node(x, y + (deck - 1)):
                    for node in range(deck):
                        I.map_player[y + node][x] = I.tile_ship
                        temp.append([x, y + node,1])
                    I.lops.append(temp)
                    return(True)


def shoot():
    while True:
        try:
            pos = input('Aiming (example: А0): ').lower()
            if len(pos) == 2:
                x,y = list(pos)
                x = I.os[x]
                y = int(y)
            else:
                raise
            k = shoot_check(x,y,'player')
            if k == [1,0]:
                I.map_enemy[y][x] = I.tile_ship_dead
                draw()
                warning('Hit!')
                I.deck_enemy -= 1
            elif k == [1,1]:
                I.map_enemy[y][x] = I.tile_ship_dead
                draw()
                warning('The ship is sunk!')
                I.deck_enemy -= 1
                win_condition('player')
            else:
                if I.map_enemy[y][x] != I.tile_ship_dead:
                    I.map_enemy[y][x] = I.tile_miss
                draw()
                warning('Miss!')
                enemy_turn()
        except KeyboardInterrupt:
            warning('\nABORT')
            sys.exit()
        except SystemExit:
            sys.exit()
        except:
            warning(str('Incorrect coordinates'))


def shoot_check(x,y,person):
    I.turns += 1
    if person == 'player':
        los = I.loes
        map = I.map_enemy
    else:
        los = I.lops
        map = I.map_player
    deck_alive = 0
    for ship in range(10):
        if [x,y,1] in los[ship]:                                                         # find node in ship list
            los[ship][los[ship].index([x,y,1])] = [x,y,0]
            for deck in range(len(los[ship])):
                deck_alive += los[ship][deck][2]
            if deck_alive == 0:
                for deck in range(len(los[ship])):
                    x1,y1,z1 = list(los[ship][deck])
                    for i in range(8):                                                   # mark area around ship deck
                        map[(0 if ((y1 - 1) < 0) else y1 - 1)][(0 if ((x1 - 1) < 0) else x1 - 1)] = \
                            map[(0 if ((y1 - 1) < 0) else y1 - 1)][x1] = map[(0 if ((y1 - 1) < 0) else y1 - 1)][(9 if ((x1 + 1) > 9) else x1 + 1)] = \
                            map[y1][(0 if ((x1 - 1) < 0) else x1 - 1)] = map[y1][(9 if ((x1 + 1) > 9) else x1 + 1)] = \
                            map[(9 if ((y1 + 1) > 9) else y1 + 1)][(0 if ((x1 - 1) < 0) else x1 - 1)] = map[(9 if ((y1 + 1) > 9) else y1 + 1)][x1] = \
                            map[(9 if ((y1 + 1) > 9) else y1 + 1)][(9 if ((x1 + 1) > 9) else x1 + 1)] = I.tile_miss
                for deck in range(len(los[ship])):                                       # mark dead deck
                    x1,y1,z1 = list(los[ship][deck])
                    map[y1][x1] = I.tile_ship_dead
                return([1,1])                                                            # ship destroyed
            else:
                return([1,0])                                                            # deck destroyed


def enemy_turn():
    if I.x != 10:                                                                        # if ship already detected continue attack
        enemy_next_turn(I.x, I.y, I.position)
    else:
        while True:                                                                      # scouting
            x = random.randrange(10)
            y = random.randrange(10)
            if I.map_player[y][x] in (I.tile_sea, I.tile_ship):
                break
        shoot_result = shoot_check(x,y,'enemy')
        if shoot_result in ([1,0], [1,1]):
            I.map_player[y][x] = I.tile_ship_dead
            draw()
            input('{}{}, enemy hit!'.format(I.ros[x],y))
            I.deck_player -= 1
            win_condition('enemy')
            if shoot_result == [1,1]:                                                    # scouting for new ship
                enemy_turn()
            else:                                                                        # attack current ship
                I.x = x
                I.y = y
                enemy_next_turn(I.x, I.y, I.position)
        else:
            I.map_player[y][x] = I.tile_miss
            draw()
            input('{}{}, enemy miss!'.format(I.ros[x],y))


def enemy_next_turn(x, y, position):
    if position == 0:                                                                    # don't know ship orientation (h or v)
        while True:
            position = random.randrange(1,5)
            if position == 1 and ship_orientation(position,x,y) in (I.tile_sea, I.tile_ship):
                break
            elif position == 2 and ship_orientation(position,x,y) in (I.tile_sea, I.tile_ship):
                break
            elif position == 3 and ship_orientation(position,x,y) in (I.tile_sea, I.tile_ship):
                break
            elif position == 4 and ship_orientation(position,x,y) in (I.tile_sea, I.tile_ship):
                break
    if I.position == 0:                                                                  # try to guess orientation
        p = position
    else:                                                                                # continue attack
        p = I.position
    if p in (1, 2):                                                                      # vertical orientation
        if ship_orientation(position,x,y) in (I.tile_sea, I.tile_ship):                  # if new deck next to old one - attack
            if p == 1:
                y = (0 if ((y - 1) < 0) else y - 1)
            else:
                y = (0 if ((y + 1) < 0) else y + 1)
        else:
            for i in range(1,10):
                if ship_orientation(position,x,y,i) == I.tile_miss:                      # if reach end of ship - go back
                    if p == 1:
                        I.position = 2
                    else:
                        I.position = 1
                    enemy_next_turn(I.x, I.y, I.position)
                    return
                elif ship_orientation(position,x,y,i) == I.tile_ship_dead:               # if new deck is already sunk go for next one
                    pass
                else:
                    if p == 1:
                        y = (0 if ((y - i) < 0) else y - i)                              # find new deck and attack
                    else:
                        y = (9 if ((y + i) > 9) else y + i)
                    break
        if y == 0:                                                                       # if reach end of map - change route and go back
            p = 2
        elif y == 9:
            p = 1
    elif p in (3, 4):
        if ship_orientation(position,x,y) in (I.tile_sea, I.tile_ship):
            if p == 3:
                x = (0 if ((x - 1) < 0) else x - 1)
            else:
                x = (9 if ((x + 1) > 9) else x + 1)
        else:
            for i in range(1,10):
                if ship_orientation(position,x,y,i) == I.tile_miss:
                    if p == 3:
                        I.position = 4
                    else:
                        I.position = 3
                    enemy_next_turn(I.x, I.y, I.position)
                    return
                elif ship_orientation(position,x,y,i) == I.tile_ship_dead:
                    pass
                else:
                    if p == 3:
                        x = (0 if ((x - i) < 0) else x - i)
                    else:
                        x = (9 if ((x + i) > 9) else x + i)
                    break
        if x == 0:
            p = 4
        elif x == 9:
            p = 3
    shoot_result = shoot_check(x, y, 'enemy')
    if shoot_result == [1,0] or shoot_result == [1,1]:
        I.map_player[y][x] = I.tile_ship_dead
        draw()
        input('{}{}, enemy hit!'.format(I.ros[x],y))
        I.deck_player -= 1
        win_condition('enemy')
        if shoot_result == [1,1]:
            I.position = 0
            I.x = 10
            I.y = 10
            enemy_turn()
        else:
            I.position = p
            I.x = x
            I.y = y
            enemy_next_turn(I.x, I.y, I.position)
    else:
        if I.map_player[y][x] == I.tile_sea:
            I.map_player[y][x] = I.tile_miss
        draw()
        if I.position % 2 == 1:
            I.position += 1
        else:
            I.position -= 1
        input('{}{}, enemy miss!'.format(I.ros[x],y))


def ship_orientation(p, x, y, i=1):
    if p == 1:
        return(I.map_player[(0 if ((y - i) < 0) else y - i)][x])
    elif p == 2:
        return(I.map_player[(9 if ((y + i) > 9) else y + i)][x])
    elif p == 3:
        return(I.map_player[y][(0 if ((x - i) < 0) else x - i)])
    elif p == 4:
        return(I.map_player[y][(9 if ((x + i) > 9) else x + i)])


def win_condition(person):
    if person == 'player':
        if I.deck_enemy == 0:
            warning('You won by {}th turn!'.format(I.turns))
            sys.exit()
        else:
            print('{} decks of the enemy left!'.format(I.deck_enemy))
    else:
        if I.deck_player == 0:
            warning('The enemy won the {}th turn!'.format(I.turns))
            sys.exit()
        else:
            print('{} yor decks left!'.format(I.deck_player))


def main():
    qucik_place('enemy')
    place()
    shoot()

if __name__ == '__main__':
    I = Initiation()
    I.init()
