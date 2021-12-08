import psutil as ps
from Htop_v3.module.lib import dec


@dec.dec_get
def get_prec():
    dict={'ИНФОРМАЦИЯ О ПРОЦЕССОРЕ':'ИНФОРМАЦИЯ О ПРОЦЕССОРЕ'}
    cpu_prec = ps.cpu_percent(0.5)
    dict.update({'Процент загрузки ЦП':(cpu_prec,'%')})
    cpu_count = ps.cpu_count()
    dict.update({'Количество ядер':(cpu_count,'num')})
    return dict

