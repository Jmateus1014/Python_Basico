def run():
    mi_diccionario={
        'llave1':1,
        'llave2':2,
        'llave3':3
    }
    # for llaves in mi_diccionario.values():
    #     print(llaves)
    # for llaves in mi_diccionario.keys():
    #     print(llaves)
    for llaves, contenido in mi_diccionario.items():
        print(llaves+' tiene '+str(contenido))
    # print(mi_diccionario['llave1'])


if __name__ == '__main__':
    run()