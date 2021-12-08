from module import take_info_PC, take_info_NET, take_info_memory, take_info_T, output


def run():
    output.show(temperature=take_info_T.get_temperature(), net=take_info_NET.get_net(),
                prec=take_info_PC.get_prec(), memory=take_info_memory.get_memory())


open('log.json','w')

if __name__=='__main__':
    run()