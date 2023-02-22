define c = Character("Chica")
define m = Character("Manager")
define g = Character("Grupo")
define f = Character("Fan")

label tronco:

    # Aquí vamos a tener la presentación del personaje principal:
    # El personaje está en un camerino y recibe la carta de un fan.
    # Se debate si seguir cantando, el grupo y el/la manager le llaman desde la puerta
    # Y tomas la decisión de qué ruta quieres seguir.

    scene fondo

    "Intro"

    menu:
        "Actriz":
            jump rama1

        "Idol":
            jump rama2

# los labels a la izquierda, con : al final y su contenido indentado
label rama1:

    # Rama 1

    "Texto Rama 1"

    menu:

        "Ruta Sentimental":

            jump rama1_rutaA

        "Ruta Cachondeo":

            jump rama1_rutaB

        "Ruta Meta":

            jump rama1_rutaC

label rama1_rutaA:

    "Ruta Sentimental"

    jump ending

label rama1_rutaB:

    "Ruta Cachondeo"

    jump ending

label rama1_rutaC:

    "Ruta Meta"

    jump ending

label ending:

    scene bl

    "..."

    "{i}Sea cual sea la ruta que hayas escogido...{/i}"

    "{i}¡Gracias por jugar!{/i}"

    return
