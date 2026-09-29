import json

print("💧🔥 ¡Test de Aura Nen de la Asociación de Cazadores! ⛓️⚡\n")

puntos = 0
puntos += int(input("1. En una batalla prefieres:\n[1] Atacar de frente\n[2] Usar trucos\n[3] Analizar de lejos\nElige un número: "))
puntos += int(input("2. Tu mayor defecto es ser:\n[1] Terco/a\n[2] Impredecible\n[3] Nervioso/a\nElige un número: "))

if puntos <= 3:
    tipo = "Intensificador (Como Gon) 👊"
elif puntos == 4:
    tipo = "Transformador (Como Killua) ⚡"
elif puntos == 5:
    tipo = "Materializador (Como Kurapika) ⛓️"
else:
    tipo = "Especialista (Como Chrollo) 🕷️"

print(f"\n✨ El agua ha reaccionado... Tu aura es de tipo: {tipo} ✨")

# Guardar el historial de pruebas en un archivo JSON
try:
    with open("registro_cazadores.json", "r") as f:
        datos = json.load(f)
except FileNotFoundError:
    datos = []

datos.append({"resultado_aura": tipo})

with open("registro_cazadores.json", "w") as f:
    json.dump(datos, f, indent=4)
    
print("\n[+] Resultado clasificado y guardado en registro_cazadores.json")
