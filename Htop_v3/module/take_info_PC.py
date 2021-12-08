import psutil as ps
from Htop_v3.module import dec


@dec.dec_get
def get_prec():
    dict={}
    cpu_prec = ps.cpu_percent(0.5)
    dict.update({'precent cp':(cpu_prec,'%')})
    cpu_count = ps.cpu_count()
    dict.update({'count cp':(cpu_count,'num')})
    return dict

