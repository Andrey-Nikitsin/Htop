import psutil as ps
from Htop_v3.module import dec


@dec.dec_get
def get_memory():
    memory = ps.virtual_memory()
    memory._asdict()
    dict={}
    dict.update(
        {'total memory':(round(((memory.total)/1000000000),1),'gb'),
         'used memory':(round((memory.used)/1000000000,1),'gb'),
         'percent memory':((memory.percent),'%'),
         'free memory':(round((memory.free)/1000000000,1),'gb')}
    )
    return dict

