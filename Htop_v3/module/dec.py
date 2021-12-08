from functools import wraps
from datetime import datetime
import json



file=open('../Htop_v3/log.json', 'w', encoding='utf-8')

def dec_get(funk):
    @wraps(funk)
    def get():
        """decorator"""
        res=funk()
        file = open('../Htop_v3/log.json', 'r', encoding='utf-8') #открыл файл
        data = json.load(file) # распознал
        data.append(res) #добавил в список новые данные
        with open('../Htop_v3/log.json', 'w') as log:
            json.dump(data,log, indent=4) #записал

        return res
    return get
