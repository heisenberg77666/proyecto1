import random

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    puntos_usuario = 0
    puntos_computadora = 0
    

    jugar_otra_vez = "si"
    while jugar_otra_vez == "si":
        for ronda in range(1, 4):  # Bucle para las 3 rondas
            print(f"\n--- Ronda {ronda} ---")

            eleccion_usuario = ""
            while eleccion_usuario not in opciones:
                eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
                if eleccion_usuario not in opciones:
                    print("Opción no válida. Por favor, elige entre piedra, papel o tijera.")

            eleccion_computadora = random.choice(opciones)

            print(f"\nTú elegiste: {eleccion_usuario}")
            print(f"La computadora eligió: {eleccion_computadora}\n")

            if eleccion_usuario == eleccion_computadora:
                print("¡Es un empate!")
            elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
                 (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
                 (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
                print("¡Ganaste esta ronda!")
                puntos_usuario += 1
            else:
                print("Perdiste esta ronda. La computadora gana.")
                puntos_computadora += 1
            
            print(f"Puntuación actual - Tú: {puntos_usuario}, Computadora: {puntos_computadora}")

        # Después de las 3 rondas, determinar el ganador final
        print("\n--- Resultados Finales ---")
        if puntos_usuario > puntos_computadora:
            print("Felicidades, le ganaste a la computadora")
        elif puntos_computadora > puntos_usuario:
            print("Lo lamento, la computadora ha ganado.")
        else:
            print("Es un empate")

        # Preguntar si quieren jugar de nuevo
        opciones_validas = ["si", "no"]
        while True:
            jugar_otra_vez = input("\n¿Quieres jugar otra vez (si/no)? ").lower()
            if jugar_otra_vez == "si":
                puntos_usuario = 0
                puntos_computadora = 0
                break
            elif jugar_otra_vez == "no":
                print("Gracias por jugar. Adiós")
                return puntos_usuario, puntos_computadora
            else:
                if jugar_otra_vez not in opciones_validas:
                    print("Opción no válida. Por favor, elige 'si' o 'no'.")

# Inicio del juego
if __name__ == "__main__":
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!""\nJugarás contra la computadora en 3 rondas.")
    puntos_usuario, puntos_computadora = jugar_piedra_papel_tijera()
    print("Puntos Usuario: ", + puntos_usuario)
    print("Puntos Computadora: " , + puntos_computadora)