label femaleScene:
    hide screen genderChoice
    #Prologue
    scene outside with fade

    show female

    you "Woah! So this is STI College!"

    you "I'm so excited. I should go inside."

    scene lobby with fade
    show happyF
    tour "Welcome to STI College, [name]!"
    tour "Are you her?"
    tour "Do you have any question?"
    menu questions2:
        "None":
            jump none
        "Do you have IT related courses?":
            jump it
        "How much is the tuition fee for senior high school?":
            jump shs

    # This ends the game.

    return
