from functools import wraps
from datetime import datetime
import json


file=open('../Htop_v3/log.json', 'w', encoding='utf-8')

def dec_get(funk):
    @wraps(funk)
    def get():
        """decorator"""
        res=funk()
        t=str(datetime.now())
        json.dump(t, file)
        json.dump(res,file,indent=4,ensure_ascii=False)
        return res
    return get
