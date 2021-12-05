from module import output, take_inf

def run():
    output.show(temperature=take_inf.get_temperature(), net=take_inf.get_net(),
                prec=take_inf.get_prec(), memory=take_inf.get_memory())

if __name__=='__main__':
    run()