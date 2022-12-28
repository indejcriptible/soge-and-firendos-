# The script of the game goes in this file
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Tommy")
define y = Character("Yumi")
define k = Character("er bicho")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lib

    # Aquí vamos a tener la presentación del personaje principal.
    # El personaje está estudiando y de repente nota un temblor/terremoto.
    # Toda la clase se refugia en un refugio de clase donde casualmente, está una chica que le gusta.
    # Y tomas la decisión de qué ruta quieres seguir.

    "Empieza"

    show pibe

    "¿Qué ruta quieres seguir"

        menu:

        "Ruta 1":
            jump ruta1

        "Ruta 2":
            jump ruta2

        "Ruta 3":
            jump ruta3

    label ruta1

        # Ruta Romantica

        menu:
        
        "Ruta 1: Final A:
        jump ruta1_final_true        
        
        "Ruta 1: Final B:
        jump ruta1_final_false

            
            label ruta1_final_true
            "Ruta 1: Final A:

            jump ending

            label ruta1_final_false
            "Ruta 1: Final B:
            
            jump ending
        

     label ruta2

        # Ruta Comedia

        menu:
        
        "Ruta 2: Final A":
        jump ruta2_final_true        
        
        "Ruta 2: Final B:
        jump ruta2_final_false
            
            label ruta2_final_true
            "Ruta 2: Final A:"

             jump ending

            label ruta2_final_false
            "Ruta 2: Final B:"

              jump ending

          

    label ruta3:

        # Ruta Comedia

        menu:
        
        "Ruta 2: Final A":
        jump ruta2_final_true        
        
        "Ruta 2: Final B:
        jump ruta2_final_false

            label ruta2_final_true
            "Ruta 2: Final A:

            jump ending

            label ruta2_final_false
            "Ruta 2: Final B:

            jump ending
   
    label ending

    "Thanks for playing!"

    return
