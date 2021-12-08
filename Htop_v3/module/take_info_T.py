import psutil as ps
from Htop_v3.module.lib import dec


@dec.dec_get
def get_temperature():
    sensor_t = ps.sensors_temperatures()
    dict = {'ДАННЫЕ ТЕМПЕРАТУРНЫХ ДАТЧИКОВ':'ДАННЫЕ ТЕМПЕРАТУРНЫХ ДАТЧИКОВ'}
    for i,j in sensor_t.items():
        if len(j)>1:
            for elem in j:
                elem._asdict()
                dict.update({elem.label:(elem.current,'c\xb0')})
        else:
            g=j[0]
            g._asdict()
            dict.update({i:(g.current,'c\xb0')})
    return dict