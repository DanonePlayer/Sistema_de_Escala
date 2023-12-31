from datetime import date

num = date.today().weekday()

sem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

if num < 5:
    print(f"Tenha uma boa {sem[num]}-feira =D")
else:
    print(f"Tenha um bom {sem[num]} =D")


print(f"\n ----------------------------------------- \n")

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]



for i in range(1, 32):
    
    data = date(year=2023, month=7, day=i)
    print(data)

    indice_da_semana = data.weekday()
    print(indice_da_semana)


    dia_da_semana = DIAS[indice_da_semana]
    print(dia_da_semana)

    numero_do_dia_da_semana = data.isoweekday()
    #print(numero_do_dia_da_semana)

    if(numero_do_dia_da_semana == 6 or numero_do_dia_da_semana == 7 ):
        print("Final de semana")