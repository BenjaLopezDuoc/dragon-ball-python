import os
os.system("cls")

nombre_guerrero = input("Ingrese el nombre del guerrero: ")
edad = int(input("Ingrese la edad: "))
raza = input("Ingrese su raza: sayayin - namekiano - humano - androide: ")
nivel_poder = int(input("Ingrese su nivel de poder base: "))

if raza == "sayayin" and nivel_poder < 1000:
    poder_final = nivel_poder
    transformacion = ("No puedes transformarte: ")

elif raza == "sayayin" and 1000 <= nivel_poder <= 4999:
    poder_final = nivel_poder * 2
    transformacion = (" Super sayayin : ")

elif raza == "sayayin" and 5000 <= nivel_poder <= 9999:
    poder_final = nivel_poder * 3
    transformacion = ("Super sayayin 2: ")

elif raza == "sayayin" and nivel_poder >= 10000:
    if edad < 18:
        poder_final = nivel_poder
        transformacion = ("No puedes utilizar el Super sayayin 3: ")
    else:
        poder_final = nivel_poder * 4
        transformacion = ("Super sayayin 3: ")


if raza == "namekiano" and nivel_poder < 2000:
    poder_final = nivel_poder
    transformacion = "No existe"
    if edad > 100:
        poder_final += 1000

elif raza == "namekiano" and 2000 <= nivel_poder <= 7999:
    poder_final = nivel_poder * 2
    transformacion = "No existe"
    if edad > 100:
            poder_final += 1000
            

elif raza == "namekiano" and nivel_poder >= 8000:
    poder_final = nivel_poder * 3
    transformacion = "No existe"
    if edad > 100:
            poder_final += 1000
            


if raza == "humano" and nivel_poder < 1000:
    poder_final = nivel_poder
    transformacion = "No existe"
    if edad >= 30:
            poder_final += 500
            

elif raza == "humano" and 1000 <= nivel_poder <= 2999:
    poder_final = nivel_poder * 2
    transformacion = "No existe"
    if edad >= 30:
        poder_final += 500
        

elif raza == "humano" and nivel_poder >= 3000:
    poder_final = nivel_poder * 3
    transformacion = "No existe"
    if edad >= 30:
        poder_final += 500
        


if raza == "androide" and nivel_poder < 5000:
    poder_final = nivel_poder + 1000
    transformacion = "No existe"

elif raza =="androide" and 5000 <= nivel_poder <= 9999:
    poder_final = nivel_poder + 2000
    transformacion = "No existe"

elif raza =="androide" and nivel_poder >= 10000:
    poder_final = nivel_poder + 5000
    transformacion = "No existe"


if poder_final < 1000:
    rango = "Novato"

elif 1000 <= poder_final <= 4999:
    rango = "Guerrero"

elif 5000 <= poder_final <= 9999:
    rango = "Guerrero Elite"

elif 10000 <= poder_final <= 19999:
    rango = "Guerrero Z"

else:
    rango = "Leyenda"

if edad >= 16 and poder_final >= 1000:
    estado = "apto para combatir: "

else:
    estado = "no apto para combatir: "

print(f"""
======== RESULTADOS ========
Guerrero: {nombre_guerrero}
Edad: {edad}      
Raza: {raza}
Transformacion: {transformacion}
Poder base: {nivel_poder}
Poder final: {poder_final}
Rango: {rango}
Estado: {estado}
                            """)







