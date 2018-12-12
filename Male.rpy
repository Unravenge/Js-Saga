label maleScene:
    hide screen genderChoice
    stop music fadeout 1
    play music "Music/Accumula Town - Pokémon Black & White Music Extended 128 kbps.mp3" fadeout 1.5
    #Prologue
    scene bedroomMale with fade

    show male

    you "*yawn* What time is it?"
    "7:00AM"
    show male with hpunch
    you "Goodness gracious! I'm late for school!"

    scene diningRoom with fade

    show mother
    mom "Good morning, Honey! Eat your breakfast before it gets cold."
    you "I would love to but I'm late mom."
    mom "Let me pack them for you. Make sure to eat it on your way to school."
    you "Thanks mom."
    stop music fadeout 1
    play sound "Music/jeep.wav"
    scene travel with fade
    with Pause(1)
    stop sound fadeout 1

    scene room with fade
    play music "Music/273 - K.K. Soul (Aircheck) 128 kbps.mp3" fadein 1
    show male at left
    show profTablet at right
    you "Good morning sir. Sorry I'm late."
    show profTablet with hpunch
    prof "First day of school and you're late?"
    you "Sorry sir."
    prof "Nah it's okay. Go ahead and take a sit."
    you "Thank you sir"
    "Phew! I thought I was doomed"
    hide male
    show profTablet at center with move
    mat "Okay. Now that we’re all here let me introduce myself. My name is Matthew Alejandrew. I’ve been teaching here for 4 years now."
    mat "I graduated from here, took master’s degree and decided to teach here while working on my projects."
    mat "I will be your JavaScript professor and I hope we could enjoy this lesson while you were learning. "
    mat "Now that I’m done introducing myself, it’s your turn."
    hide profTablet with dissolve
    #show Ken with dissolve
    ken "Hi! My name is Ken Alvarez, 17 years old. I chose ICT because I love computer games."
    #hide ken with dissolve
    #show shayne with dissolve
    shayne "H-hi! My name is Shayne Boniveve, 17 years old. I chose ICT because my mother wanted me to."
    #hide shayne with dissolve
    #show king with dissolve
    king "A pleasant morning to everyone! My name is King Causius, 17 years old. I chose ICT because when I was 15, my father’s friend showed me the world of programmers and I liked it."
    king "I already know a few of programming and I hope I could learn a lot more here in STI."
    #hide king with dissolve
    #show vincent with dissolve
    vincent "My name is Vincent Dante, 17. I chose ICT because I was told this course is easy."
    #hide vincent with dissolve
    show male with dissolve
    menu greetings:
        "Hi!":
            jump hi
        "Hello":
            jump hello
        "Good Morning!":
            jump gm
    #insert different greetings
#Continuation
label con:
    scene room
    show profTablet with dissolve
    mat "I see that most of you guys have your own reason in choosing this course."
    mat "I hope you all make it through this school year and achieve the dreams that you all aspire."
    mat "That’s all for today, you may now take an early break."
    stop music fadeout 1

    scene black with fade
    show text "On his way to the cafeteria, he was approached by Ken, his classmate." with dissolve
    with Pause(2)
    hide text with dissolve
    #scene hallway with fade
    scene canteen with fade
    #show ken
    ken "Hey [name]! Want to go to the cafeteria together?"
    you "Uhh sure."
    #scene canteen with fade
    #Ken and MC saw Shayne sitting at a table, alone
    ken "Isn't that Shayne?"
    you "Yeah"
    ken "Come, let's join her."
    you "Sure."
    #scene table
    ken "Hello! I'm Ken, he's [name]. Can we join you?"
    "looks at [name]"
    shayne "Uhmmm.. Sure."
    #scene sitting
    ken "Is it true that you only chose ICT because your mom told you?"
    shayne "Y-yes."
    ken "That must've suck. Hey [name], say something."
    menu say:
        "Course that she likes":
            jump course
        "Are you okay...":
            jump okay
    #First part
    label course:
        you "Uhmmm.. What course did you plan to take?"
        shayne "I would love to take an art related course, but..."
        shayne "My mom told me that it wouldn’t lead me somewhere and I should just choose ICT because it is in demand."
    menu say2:
        "Are you okay...":
            jump okay2
    label okay:
        you "Are you okay with that?"
        you "I mean it must be hard for you"
        shayne "Well there’s nothing I can do really."
        shayne "I just have to learn how to love this course."
    menu say3:
        "Course that she likes":
            jump course2
    #second part
    label course2:
        you "Uhmmm.. What course did you plan to take?"
        shayne "I would love to take an art related course, but..."
        shayne "My mom told me that it wouldn’t lead me somewhere and I should just choose ICT because it is in demand."
        jump con2
    label okay2:
        you "Are you okay with that?"
        you "I mean it must be hard for you"
        shayne "Well there’s nothing I can do really."
        shayne "I just have to learn how to love this course."
        jump con2

#Continuation2
label con2:
    ken "Man, that sucks"
    screen whereto():
        modal True
        imagebutton:
            idle "images/Background/restroom.png"
            hover "images/Background/restroomHover.png"
            xalign 2 yalign 0.5
            focus_mask True
            action Jump("restroom")
        imagebutton:
            idle "images/Background/room.png"
            hover "images/Background/roomHover.png"
            xalign 1.0 yalign 0.5
            focus_mask True
            action Jump("classroom")
    show screen whereto() with fade
    you "Where should I go next?"

label restroom:
    hide screen whereto
    #scene restroom with fade
    scene black with fade
    show vincent with vpunch
    vincent "Tch"
    scene restroom outside with fade
    #show ken
    ken "Hey, we should go to our next class already."
    you "Let's go."
    jump classroom

label classroom:
    hide screen whereto
    scene black
    show text "insert mini scene here" with dissolve
    with Pause(1)
    hide text with dissolve
    scene room
    you "What a good start of school year."
    you "I should go home."

    # This ends the game.

    return
