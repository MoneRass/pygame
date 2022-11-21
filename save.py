import json
from score_board import name_box

with open('database.txt') as f:
        data=f.read()
        current_data=json.loads(data)
        f.close()

def readfile():
    
    pos_index=20

    with open('database.txt') as f:
        data=f.read()

    game_data=json.loads(data)
    j=0

    for i in sorted(game_data,key=game_data.get, reverse=True):
        name_data = i+'\t\t'+str(game_data[i])
        name_box(i, str(game_data[i]), pos_index)
        pos_index+=100
        if(pos_index>=500):
            break
        


readfile()