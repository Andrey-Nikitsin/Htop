
def l_print(key,n):
    l=len(key)
    l_pr=32-l-n
    return '|{}{:.>'f'{l_pr}''} {}|'

def show(**kwargs):
    for elem in kwargs:
        data=kwargs[str(elem)]
        i=0
        for key, value in data.items():
            if key == value:
                print()
                print(' \033[34m|{:.^69}|'.format(key))
            else:
                n=len(value[1])
                if i%2==0:
                    print('\033[31m',str(l_print(key,n)).format(key,value[0],value[1]),end=' ')
                    i+=1
                else:
                    print(str(l_print(key,n)).format(key,value[0],value[1]))
                    i+=1