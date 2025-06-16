import random

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]

    eleccion_usuario = ""
    while eleccion_usuario not in opciones:
        eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
        if eleccion_usuario not in opciones:
            print("Opción no válida Por favor, elige entre piedra, papel o tijera.")

    eleccion_computadora = random.choice(opciones)

    print(f"\nTú elegiste: {eleccion_usuario}")
    print(f"La computadora eligió: {eleccion_computadora}\n")

    if eleccion_usuario == eleccion_computadora:
        print("¡Es un empate!")
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
         (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
        print("Ganaste")
    else:
        
        print("Perdiste La computadora gana.")
        

# Inicio
while True:
    for ronda in range(1, 4):
        print(f"\n--- Ronda {ronda} ---")
        jugar_piedra_papel_tijera()


    
        
    