# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("[name]")
define tour = Character("Tour")
define mom = Character("Mom")
define prof = Character("Prof")
define mat = Character("Sir Mat")
define ken = Character("Ken")
define shayne = Character("Shayne")
define king = Character("King")
define vincent = Character("Vincent")

screen genderChoice():
    modal True
    imagebutton:
        idle "images/Characters/male.png"
        hover "images/Characters/male.png"
        xalign 0.2 yalign 0.5
        focus_mask True
        action Jump("maleScene")
    imagebutton:
        idle "images/Characters/female.png"
        hover "images/Characters/female.png"
        xalign 0.8 yalign 0.5
        focus_mask True
        action Jump("femaleScene")
# The game starts here.
label splashscreen:
    scene black with fade
    with Pause(1)

    show text "Kyrios Org Presents" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return

label start:

    $ score = 0
    #Asks for Character's name
    scene lobby with fade
    $ name = renpy.input("What is your name?")
    $ name = name.strip()
    show screen genderChoice()
    with fade
    "Choose your gender"


    return
