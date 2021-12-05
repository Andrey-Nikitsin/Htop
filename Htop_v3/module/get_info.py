import psutil as ps
from collections import namedtuple

def get_info():
    sensor_t = ps.sensors_temperatures()
    dict = {}
    dict.update({'ДАННЫЕ ТЕМПЕРАТУРНЫХ ДАТЧИКОВ':'ДАННЫЕ ТЕМПЕРАТУРНЫХ ДАТЧИКОВ'})
    for i,j in sensor_t.items():
        if len(j)>1:
            for elem in j:
                elem._asdict()
                dict.update({elem.label:elem.current})
        else:
            g=j[0]
            g._asdict()
            dict.update({i:g.current})
    dict.update({'ИНФОРМАЦИЯ О СЕТИ':'ИНФОРМАЦИЯ О СЕТИ'})
    net = ps.net_io_counters()
    net._asdict()
    dict.update(
        {'Пакетов отправленно': net.packets_sent,
         'Пакетов получено': net.packets_recv}
    )
    dict.update({'ИНФОРМАЦИЯ О ПАМЯТИ': 'ИНФОРМАЦИЯ О ПАМЯТИ'})
    memory = ps.virtual_memory()
    memory._asdict()
    dict.update(
        {'Всего памяти': round(((memory.total) / 1000000000), 1),
         'Памяти использовано': round((memory.used) / 1000000000, 1),
         'Процент занятой памяти': (memory.percent),
         'Памяти свободно': round((memory.free) / 1000000000, 1)}
    )
    cpu_prec = ps.cpu_percent(0.5)
    cpu_count = ps.cpu_count()
    dict.update({'ИНФОРМАЦИЯ О ПРОЦЕССОРЕ':'ИНФОРМАЦИЯ О ПРОЦЕССОРЕ'})
    dict.update({'Количество ядер':cpu_count,
                 'Процент загрузки ЦП':cpu_prec}
                )
    return dict