nombre = input("Escribe tu nombre: ")
ventas = int(input("Cuanto dinero has vendido este mes? "))
acuerdo = int(input("De que porcentaje es el acuerdo que tienes en comisiones? "))

comision = round((ventas * acuerdo) / 100,2)

print(f"Hola {nombre}, como has vendido {ventas} dolares, y tu acuerdo es de un {acuerdo}% tu comision es {comision}")