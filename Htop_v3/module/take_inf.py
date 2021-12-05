import psutil as ps
from collections import namedtuple

def get_prec():
    dict={'ИНФОРМАЦИЯ О ПРОЦЕССОРЕ':'ИНФОРМАЦИЯ О ПРОЦЕССОРЕ'}
    cpu_prec = ps.cpu_percent(0.5)
    dict.update({'Процент загрузки ЦП':cpu_prec})
    cpu_count = ps.cpu_count()
    dict.update({'Количество ядер':cpu_count})
    return dict

def get_net():
    dict={'ИНФОРМАЦИЯ О СЕТИ':'ИНФОРМАЦИЯ О СЕТИ'}
    net=ps.net_io_counters()
    net._asdict()
    dict.update(
        {'Пакетов отправленно':net.packets_sent,
         'Пакетов получено':net.packets_recv}
    )
    return dict

def get_temperature():
    sensor_t = ps.sensors_temperatures()
    dict = {'ДАННЫЕ ТЕМПЕРАТУРНЫХ ДАТЧИКОВ':'ДАННЫЕ ТЕМПЕРАТУРНЫХ ДАТЧИКОВ'}
    for i,j in sensor_t.items():
        if len(j)>1:
            for elem in j:
                elem._asdict()
                dict.update({elem.label:elem.current})
        else:
            g=j[0]
            g._asdict()
            dict.update({i:g.current})
    return dict

def get_memory():
    memory = ps.virtual_memory()
    memory._asdict()
    dict={'ИНФОРМАЦИЯ О ПАМЯТИ':'ИНФОРМАЦИЯ О ПАМЯТИ'}
    dict.update(
        {'Всего памяти':round(((memory.total)/1000000000),1),
         'Памяти использовано':round((memory.used)/1000000000,1),
         'Процент занятой памяти':(memory.percent),
         'Памяти свободно':round((memory.free)/1000000000,1)}
    )
    return dict