import psutil as ps
from Htop_v3.module.lib import dec


@dec.dec_get
def get_memory():
    memory = ps.virtual_memory()
    memory._asdict()
    dict={'ИНФОРМАЦИЯ О ПАМЯТИ':'ИНФОРМАЦИЯ О ПАМЯТИ'}
    dict.update(
        {'Всего памяти':(round(((memory.total)/1000000000),1),'gb'),
         'Памяти использовано':(round((memory.used)/1000000000,1),'gb'),
         'Процент занятой памяти':((memory.percent),'%'),
         'Памяти свободно':(round((memory.free)/1000000000,1),'gb')}
    )
    return dict

