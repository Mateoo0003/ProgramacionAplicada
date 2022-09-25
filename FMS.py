# Entrada: Vacío, Nivel 1, Nivel 2, Temperatura, Time
# Salida: V1, V2, V3, C, Start temporizador

S1 = [1,0,0,0,0]
S2 = [0,0,0,1,1]
S3 = [0,0,1,0,0]
S4 = [0,1,0,0,0]

def statusmachine(estado,entrada):
    
    if estado == 'S1':
        salida = [1,0,0,0,0]
        if entrada == [0,1,0,0,0]: 
            estado = 'S2'
    elif estado == 'S2':
        salida = [0,0,0,1,1]
        if entrada == [0,0,0,1,1]:
            estado = 'S3'
        elif entrada[3] == [0]:
            estado = 'S4'
    elif estado == 'S3':
        salida = [0,0,1,0,0]
        if entrada == [1,0,0,0,0]:
            estado = 'S1'
    elif estado == 'S4':
        salida = [0,1,0,0,0]
        if entrada == [0,0,1,0,0]:
            estado = 'S3'
    else: 
        salida = [0,0,0,0,0]
        
    return estado, salida

estado = 'S1'
entradas = [[0,1,0,0,0],
            [0,0,0,1,1],
            [0,0,0,0,1],
            [0,0,1,0,0],
            [1,0,0,0,0]]

"""
for entrada in entradas: 
    print('\n')
    print('Estado activo: '+estado+'. Entrada: ',entrada,end='')
    estado,salida=statusmachine(estado,entrada)
    # print('Estado siguiente: '+estado+', Salida: '+salida,end='\n')

print('\n')
"""


        
