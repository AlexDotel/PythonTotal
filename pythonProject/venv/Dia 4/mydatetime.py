from datetime import datetime

despierta = datetime(2022,10,5,6,7)
duerme = datetime(2022, 10, 5, 23,45)
vigilia = duerme - despierta
print(vigilia)
print(vigilia.seconds)

# Utilizando: from datetime import date
# nacimiento = date(1992, 3,5)
# defuncion = date(2092, 6, 9)
# vida = defuncion - nacimiento
# print(vida)
# print(vida.days)

# Todo lo de abajo con: import datetime
# mi_hora = datetime.time(9,30,00,1000)
# print(mi_hora)
# print(mi_hora.hour)
# print(mi_hora.minute)
# print(mi_hora.second)
# print()
#
# mi_dia = datetime.date(2024, 3, 23)
# print(mi_dia)
# print(mi_dia.year)
# print(mi_dia.ctime())
# print(mi_dia.today())

# # Lo siguiente importando: from datetime import datetime
# mi_fecha = datetime(2024, 3, 23, 14, 37, 24)
# print(mi_fecha)
#
# # Cambiamos el mes de mi fecha
# mi_fecha = mi_fecha.replace(month=10)
# print(mi_fecha)