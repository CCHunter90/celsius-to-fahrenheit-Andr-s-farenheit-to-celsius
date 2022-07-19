grados = str(input('Introduce la unidad de medida (Celsius/Fahrenheit): '))
temperatura = int(input('Introduce la temperatura: '))

def check(grados):
    if grados == 'Celsius' or grados == 'Fahrenheit':
        if grados == 'Celsius':
            escala = 'C'
            conversor(escala, temperatura)
        else:
            escala = 'F'
            conversor(escala, temperatura)
    else:
        grados = str(input('Introduce una unidad de medida válida (Celsius/Fahrenheit): '))
        check(grados)

def conversor(escala, temperatura):
    if escala == 'C':
        resultado = temperatura * 9/5 + 32
        print(f'{temperatura}{escala}º son {resultado}Fº')
    elif escala == 'F':
        resultado = (temperatura - 32) * 5/9
        print(f'{temperatura}{escala}º son {resultado}Cº')
    else:
        print('UnexSPECcTETED ErrORr')

check(grados)
