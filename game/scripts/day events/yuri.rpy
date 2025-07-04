label day_event_yuri:
    image overlay_ai = "images/day events/overlay ai 1.png"
    image redblur = "images/day events/red blur.png"
    scene bg lounge
    with default_fade
    n "You're making your way to the lounge to get a cup of coffee when you run into two department heads."
    n "It's Dr. Aikha and Dr. Deceased! You wonder what they're talking about."
    show deceased: #pensive
        alpha 0.0
        xzoom -1.0
        alpha 1.0
        appear(x_align = 0.2)
    show aikha upset at appear (x_align = 0.8)
    deceased "..."
    aikha "..."
    n "...They're just staring at each other. Are you interrupting something?"
    n "You slowly slink towards the coffee machine."
    deceased "So how was your day, Ai?" #idk some othe expression
    aikha surprise "It's been fine. My patients have been doing pretty well lately."
    aikha neutral "Maybe you could come over to Path-Para to meet them some time?"
    deceased "Yeah! That would be..."
    deceased "..."
    aikha "..."
    player "..."
    n "...Is this some sad attempt at office romance?"
    n "Well! You have no clue what's going on, and you suspect those two don't either." 
    
    menu:
        n "Maybe you can help them out?"
        "Wingman for Dr. Deceased.":
            jump wing_dece
        "Wingman for Dr. Aikha.":
            jump wing_aikha

label wing_dece:
    player "Hey, Dr. Aikha! I heard that there're some really cool... um... diseases! That Dr. Deceased has been researching!"
    aikha surprise "Oh. Is that so? But I thought Dece specialized in..."
    aikha pensive "Huh. Dece. What {i}do{/i} you specialize in?"
    deceased happy "Oh! I'm glad you asked!"
    deceased "The variety of anomalies that exist in our world go far beyond what we've chosen to classify at the Foundation.{nw}"
    show black_screen zorder 50:
        alpha 0.0
        linear 3.0 alpha 1.0
    deceased "Although we can easily split anomalies by their origins and functions..."
    show aikha upset
    show black_screen zorder 50:
        linear 0.7 alpha 0.0
    n "..."
    deceased neutral "...all that being said, I'm basically half an expert in anomalous pathologies myself!"
    deceased "Although not as much as you, certainly. Ha. Ha." #panic
    n "You wish for a commically large piano to drop on your head right about now. Unforunately, it doesn't come."
    aikha happy "Well, if you ever have time, you're free to come by and take a peak! I mean, I'm sure Aran would be happy to see you."
    deceased "Haha, yeah! Aran..."
    aikha surprise "Unless you're preoccupied. You've been out a lot on field studies lately, so-"
    deceased "No!" #surprise
    aikha "..."
    deceased "I mean... it's been kind of slow out there lately. I can set my assistants on it for a bit. I have time! I promise."
    aikha happy "Oh. Of course! I've been meaning to hang out more, but you never seemed to have time. Heh."
    deceased happy "That's alright. I mean... I'll always make time for you!"
    aikha ":D"
    deceased ":D"
    player ":("
    n "Barf."
    n "Well, you've already finished your coffee, so you leg it while you still can."
    player "I'll just... be going now..."
    aikha neutral "Right! You're still here, [player_name]."
    #if characters["deceased"]["points"] > 2:
    #    n "You see Dr. Deceased turn to look at you, goggles glinting gratefully. Score! You must've helped them out."
    #    n "Or maybe the lights are too bright in here? Anyway, you feel like you've done something right, so you take credit for it."
    #else:
    #    deceased pensive "Wait, who is that?"
    #    n "No one important! Please leave [player_name] alone."
    show deceased neutral
    n "The two turn to look at you for the first time since you've entered the lounge."
    deceased "Oh. I didn't see you there."
    n "They seem slightly annoyed at your presence. You feel as if their eyes are staring daggers at you behind those opaque googles."
    aikha happy "...Anyways! Meet at Path-Para at 1?"
    deceased happy "Sure thing!"    
    show aikha at disappear
    show deceased at disappear
    n "The two skip away, hand-in-hand."
    hide aikha
    hide deceased
    n "Well, sort of. Dr. Deceased is holding Dr. Aikha's coat sleeve, but it's the thought that counts, right?"
    $ update_character_points({"aikha": 2, "deceased": -1})
    return
    
label wing_aikha: 
    n "You whip your head around to look for something- anything- to help."
    n "There's a fully loaded military-grade shotgun in an emergency glass case. Perfect!"
    player "Dr. Deceased! Watch this!"
    # show deceased surprise
    n "You smash it open, and - against all ethics and occupational preservation - open-fire on Dr. Aikha."
    $ shake_screen(duration=0.3, strength=5, repeat=3)
    show redblur:
        alpha 0.0
        block:
            linear 0.2 alpha 0.3
            linear 0.1 alpha 0.0
            repeat 3
    show overlay_ai zorder 50:
        alpha 0.0
        block:
            linear 0.8 alpha 1.0
            linear 0.8 alpha 0.0
            repeat
    show aikha unique 
    aikha "AA- eughghghhhgh..."
    show aikha unique:
        xalign 0.8
        linear 1.3 yalign 5.0
    n "Is this working?"
    aikha "My spleen... MY EYES..."
    player "Which ones?!"
    deceased "Oh no! Dr. Aikha, it seems that 26 out of 57 of your surface level peepers have been shot!" #surprise
    n "Dr. Aikha is still convulsing on the ground. A couple layers of skin peel off as they melt to the floor."
    n "...{i}Did{/i} this work?!"
    deceased neutral "It seems as a response to the external trauma, your body has compensated by turning into an amorphous entity!"
    deceased "...Can this form be injured? Hold on." #pensive
    n "Dr. Deceased pulls out their company gun and shoots {i}it{/i}."
    with hpunch
    show aikha unique:
        xalign 0.8
        linear 1.3 yalign 8.0
    aikha "{sc}IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII{/sc}{nw}"
    n "You aren't sure if this is supposed to be how this goes."
    deceased happy "Wow! The bullet has been completely absorbed! Dr. Aikha, you never told me what a fascinating biological structure you possess!"
    aikha "{sc}IIIIIIIIIIIIIIIIIIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{sc}{nw}"
    n "At this point, you're not really sure what your plan was." 
    n "If you're being honest with yourself, this was mostly an excuse to vent your hatred of office romcoms." 
    deceased happy "Oh, this is wonderful. There's so much data to be collected!"
    deceased "Dr. Aikha, would you perhaps be free to run some more tests in my office?"
    aikha fury "{sc}EEIAUAGHEAGAUUGAGH??{/sc}"
    deceased "Alright, great! Man, I've been looking forward to this opportunity for weeks!"
    hide aikha
    hide deceased
    hide overlay_ai zorder 50
    #potential cg??? idk man, deceased carrying a piles of flesh and eyeballs???/
    n "You watch as Dr. Deceased scrubs what's left of Dr. Aikha(?) off the floor and carries it out of the lounge area."
    n "You're not sure, but from this angle, you think you can see a hint of blush coming from the pile of eyes and flesh."
    player "..."
    player "In front of my coffee?!"
    $ update_character_points({"aikha": -1, "deceased": 2})
    return