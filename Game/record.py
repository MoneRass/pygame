import json

with open('database.txt') as f:
        data=f.read()
        current_data=json.loads(data)
        f.close()

def writefile(name,score):

    current_data.update({str(name):score})

    with open('database.txt', 'w') as f:
       
        f.write(json.dumps(current_data))
        f.close()

    #print(enter_name)
#writefile("ping",500)