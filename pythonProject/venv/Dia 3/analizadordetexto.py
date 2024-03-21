txtoriginal = input("Ingresa un texto a analizar: ")
# txtoriginal = "La Cancion"
letras = []

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())
print("\n")

txt = txtoriginal.lower()
print("Tus letras son", letras)

print(f"La letra {letras[0]} aparece {txt.count(letras[0])} veces")
print(f"La letra {letras[1]} aparece {txt.count(letras[1])} veces")
print(f"La letra {letras[2]} aparece {txt.count(letras[2])} veces")
print("\n")

palabras = txtoriginal.split()
print(f"Tu texto contiene {len(palabras)} palabras")
print("\n")

print(f"El primer caracter de tu texto es {txtoriginal[0]}")
print(f"El ultimo caracter de tu texto es {txtoriginal[-1]}")
print("\n")

listarevertida = palabras
listarevertida.reverse()
txtrevertido = " ".join(listarevertida)
print(txtrevertido)
print("\n")

resultadobusqueda = {True:'La palabra "Python", si esta en tu texto',False:'La palabra Python no esta en tu texto'}
print(resultadobusqueda["python" in txt])