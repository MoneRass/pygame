import random

map1 = [
    '                                                                           ',
    '                                                                           ',
    '                                                                           ',
    '                                                                                   ',
    '                                                                 A     A        A   ',
    '        P                     C                                                                            ',
    '                             AAA                                                                                              C     ',
    '                                    A                                                                                         S                          ',
    '                                        A    A                                                                                     S                               ',
    '                                                   X                                                                                                               ',
    '                        XX                       XXX            XXXXXXXXX                                                               S    SSS           T          ',
    '            C     C     XXXXX                      XXXXXX         XXXXXXXXXXXXXX           XXXXXXXXX                                SS             SSS SS SSS        ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXX       XXXXXXXXXXXXXXXXXXX          XXXXXXXXXXXXXX         XXXXXXXXXXXXSSSSSSSSSSSSSSSSSSSSSSSSSSSSS  SSSS                           ']

map2 = [
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '  P                                                                                                       T',
    'XXXXX    XXX   XXX   XXXX     XXXXX   X    XXX      XX  XX  X   X  X   X  X   X   XXX  X  X  XXXX  X    XXX']

map3 = [
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                ',
    '                                                                                     ',
    '                                                                                     ',
    '                                                                                                                                       Z',
    '                                                                                                                                                             Z',
    '   P         XX                           XXXX                                               X      XXXXX                             T   Z',
    '      C X                                                      c    XXXXX               XX X                              XXXX    XXXX  Z',
    'XXXXXXXXX       XXXX  XXXXXXX    XXXXXXXX        XXXXXX     XXXXXXXXXXXXXXXXXXXXXX                           XXXXXXXXX                    ']
    
map4 = [
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '                                                                 ',
    '              C                                                  ',
    '              A                                                  ',
    '  P      A    A                 A        A   C   A  C   A  C   A  C   A                 C     C     C     C        T',
    'AAAAAA   AAAAAA  AAAAAAAAAAA       AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  S  S  S SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS']

all_map = [map1,map2,map3,map4]

level_map = map1
tile_size = 60
screen_width = 1280
screen_height = len(level_map) * tile_size

def random_map():
    n = random.randint(0,1)
    current_map = all_map[n]
    return current_map

def random_mapV2():
    n = random.randint(0,1)
    current_map = all_map[n]

this_is_the_map = random_map()