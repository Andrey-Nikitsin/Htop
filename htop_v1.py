import psutil as ps
from collections import namedtuple


def get_prec():
    dict={}
    cpu_prec = ps.cpu_percent(0.5)
    dict.update({'Процент загрузки ЦП':cpu_prec})
    return dict

def get_count():
    dict={}
    cpu_count = ps.cpu_count()
    dict.update({'Количество ядер':cpu_count})
    return dict

def get_net():
    dict={}
    net=ps.net_io_counters()
    net._asdict()
    dict.update(
        {'Пакетов отправленно':net.packets_sent,
         'Пакетов получено':net.packets_recv}
    )
    return dict

def get_temperature():
    sensor_t = ps.sensors_temperatures()
    dict = {}
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
    dict={}
    dict.update(
        {'Всего памяти':round(((memory.total)/1000000000),1),
         'Памяти использовано':round((memory.used)/1000000000,1),
         'Процент занятой памяти':(memory.percent),
         'Памяти свободно':round((memory.free)/1000000000,1)}
    )
    return dict

def l_print(key):
    l=len(key)
    l_pr=32-l
    return '|{}{:.>'f'{l_pr}''}|'

def show(**kwargs):
    i=0
    print('|{:.^67}|'.format('ДАННЫЕ ТЕМПЕРАТУРНЫХ ДАТЧИКОВ'))
    for key in kwargs['temperature']:
        if i%2==0:
            print(str(l_print(key)).format(key, kwargs['temperature'][key]),end=' ')
            i+=1
        else:
            print(str(l_print(key)).format(key, kwargs['temperature'][key]))
            i+=1
    print()
    print('|{:.^67}|'.format('ИНФОРМАЦИЯ О ПАМЯТИ'))
    for key in kwargs['memor']:
        if i % 2 == 0:
            print(str(l_print(key)).format(key, kwargs['memor'][key]), end=' ')
            i += 1
        else:
            print(str(l_print(key)).format(key, kwargs['memor'][key]))
            i += 1
    print()
    print('|{:.^67}|'.format('ИНФОРМАЦИЯ О ПРОЦЕССОРЕ'))
    for key in kwargs['count_pc']:
        print(str(l_print(key)).format(key, kwargs['count_pc'][key]),end=' ')
    for key in kwargs['pc']:
        print(str(l_print(key)).format(key, kwargs['pc'][key]))
    print()
    print('|{:.^67}|'.format('ИНФОРМАЦИЯ О СЕТИ'))
    for key in kwargs['net']:
        print(str(l_print(key)).format(key, kwargs['net'][key]),end=' ')
    print()

def run():
    show(pc=get_prec(),count_pc=get_count(),temperature=get_temperature(),memor=get_memory(),
         net=get_net())

if __name__=='__main__':
    run()
