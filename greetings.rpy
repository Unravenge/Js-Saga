label hi:
    you "Hi everyone!"
    $ lname = renpy.input("My name is [name]")
    $ lname = lname.strip()
    you "[name] [lname], 17 years old. I chose ICT because"
    menu because:
        "Games":
            jump games
        "Dream":
            jump dream
        "Make a joke":
            jump joke
label hello:
    you "Hello, everyone!"
    $ lname = renpy.input("My name is [name]")
    $ lname = lname.strip()
    you "[name] [lname], 17 years old. I chose ICT because"
    menu because2:
        "Games":
            jump games
        "Dream":
            jump dream
        "Make a joke":
            jump joke
label gm:
    you "Good morning, everyone!"
    $ lname = renpy.input("My name is [name]")
    $ lname = lname.strip()
    you "[name] [lname], 17 years old. I chose ICT because"
    menu because3:
        "Games":
            jump games
        "Dream":
            jump dream
        "Make a joke":
            jump joke
#Game/Dream/Joke
label games:
    you "I love playing games and I thought to myself, what if I create my own one and let other people play it?"
    jump con
label dream:
    you "I aspire to become a great developer someday."
    jump con
label joke:
    you "A beggar told me. Kidding aside, I aspire to become a great developer someday."
    #show shayne
    shayne "*chuckle*"
    #hide shayne
    jump con
