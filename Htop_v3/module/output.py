
def l_print(key):
    l=len(key)
    l_pr=32-l
    return '|{}{:.>'f'{l_pr}''}|'

def show(**kwargs):
    for elem in kwargs:
        data=kwargs[str(elem)]
        i=0
        for key, value in data.items():
            if key == value:
                print()
                print('|{:.^67}|'.format(key))
            else:
                if i%2==0:
                    print(str(l_print(key)).format(key,value),end=' ')
                    i+=1
                else:
                    print(str(l_print(key)).format(key, value))
                    i+=1