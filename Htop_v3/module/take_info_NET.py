import psutil as ps
from Htop_v3.module import dec


@dec.dec_get
def get_net():
    dict={}
    net=ps.net_io_counters()
    net._asdict()
    dict.update(
        {'packets setn':(net.packets_sent,'pakets'),
         'packets recv':(net.packets_recv,'pakets')}
    )
    return dict