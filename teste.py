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

data = date(year=2023, month=6, day=29)
print(data)

indice_da_semana = data.weekday()
print(indice_da_semana)

dia_da_semana = DIAS[indice_da_semana]
print(dia_da_semana)

numero_do_dia_da_semana = data.isoweekday()
print(numero_do_dia_da_semana)