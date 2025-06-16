import random

def jugar_piedra_papel_tijera():
    opciones = ['piedra', 'papel', 'tijera']
    rondas = 3 # Rondas a jugar
    puntos_usuario = 0
    puntos_computadora = 0

    for ronda in range(1, rondas + 1):
        rondas = int(input("¿Cuántas rondas quieres jugar? (3, 5, 7): "))
        print(f"\n--- Ronda {ronda} ---")
        usuario = input("Elige piedra, papel o tijera: ").lower()
        while usuario not in opciones:
            print("Opción inválida.")
            usuario = input("Por favor elige piedra, papel o tijera: ").lower()

        computadora = random.choice(opciones)
        print(f"Tú elegiste {usuario}, la computadora eligió {computadora}.")

        if usuario == computadora:
            print("¡Empate!")
        elif (usuario == 'piedra' and computadora == 'tijera') or \
             (usuario == 'papel' and computadora == 'piedra') or \
             (usuario == 'tijera' and computadora == 'papel'):
            print("¡Ganaste esta ronda!")
            puntos_usuario += 1
        else:
            print("La computadora gana esta ronda.")
            puntos_computadora += 1

    print("\n--- Resultado Final ---")
    print(f"Puntos del jugador: {puntos_usuario}")
    print(f"Puntos de la computadora: {puntos_computadora}")

    if puntos_usuario > puntos_computadora:
        print("🎉 ¡Ganaste el juego!")
    elif puntos_computadora > puntos_usuario:
        print("🤖 La computadora ganó el juego.")
    else:
        print("😮 ¡Empate total!")

if __name__ == "__main__":
    jugar_piedra_papel_tijera()