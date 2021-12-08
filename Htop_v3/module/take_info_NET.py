import psutil as ps
from Htop_v3.module.lib import dec


@dec.dec_get
def get_net():
    dict={'ИНФОРМАЦИЯ О СЕТИ':'ИНФОРМАЦИЯ О СЕТИ'}
    net=ps.net_io_counters()
    net._asdict()
    dict.update(
        {'Пакетов отправленно':(net.packets_sent,'pakets'),
         'Пакетов получено':(net.packets_recv,'pakets')}
    )
    return dict