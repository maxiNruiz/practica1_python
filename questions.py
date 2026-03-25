import random
words ={"lenguages":["python"],"elementos":["programa","variable","funcion","bucle"],"tipos":["cadena","entero","lista",]}
guessed = []
puntaje = 0
attempts = 6
print("¡Bienvenido al Ahorcado!")
print()
print("Categorias:")
print()
for categoria in words:
    print(categoria)
cat = input("elija una: ")
valores = random.sample(words[cat], len(words[cat]))
for word in valores:
    guessed = []
    puntaje = 0
    attempts = 6

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje +=6
            print(f"Puntaje: {puntaje}")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        if len(letter)>1 or not letter.isalpha() :
            print("Entrada no valida")
            continue
        if letter in guessed:
            print("Ya usaste esa letra.")
            continue
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0
        print(f"Puntaje: {puntaje}")