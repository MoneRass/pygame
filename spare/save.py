from asyncore import write
import json
import score_board

with open('database.txt') as f:
        data=f.read()
        current_data=json.loads(data)
        f.close()

def readfile():
    
    with open('database.txt') as f:
        data=f.read()

    game_data=json.loads(data)


    for i in sorted(game_data,key=game_data.get, reverse=True):
        name_data = i+'\t\t'+str(game_data[i])
        #print(name_data)
        score_board.name_box.name('hey',20)

def writefile():

    current_data.update({"ping":3000})

    with open('database.txt', 'w') as f:
       
        f.write(json.dumps(current_data))
        f.close()
