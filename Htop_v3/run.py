from module import take_info_PC, take_info_NET, take_info_memory, take_info_T, output
import json
from datetime import datetime

t = datetime.now()

with open('log.json','w') as file:
    json.dump([str(t)],file) #создал файл с временем в списке, дальше будем добавлять логи с этот список


def run():
    output.show(temperature=take_info_T.get_temperature(), net=take_info_NET.get_net(),
                prec=take_info_PC.get_prec(), memory=take_info_memory.get_memory())



if __name__=='__main__':
    run()