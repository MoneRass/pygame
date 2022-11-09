import pygame,sys
from asyncore import write
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


    for i in sorted(game_data,key=game_data.get, reverse=True):
        name_data = i+'\t\t'+str(game_data[i])
        name_box(i, str(game_data[i]), pos_index)
        pos_index+=100
        
        

def writefile():

    current_data.update({"schememe":5000})

    with open('database.txt', 'w') as f:
       
        f.write(json.dumps(current_data))
        f.close()

    #print(enter_name)



writefile()
readfile()