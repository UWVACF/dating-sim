label day_event_yuri:
    scene bg lounge
    with default_fade
    n "You're making your way to the lounge to get a cup of coffee when you run into two department heads."
    n "It's Dr. Aikha and Dr. Deceased! You wonder what they're talking about."
    show deceased pensive at appear(x_align = 0.33)
    show aikha pensive at appear (x_align = 0.66)
    deceased "..."
    aikha "..."
    n "...They're just staring at each other. Are you interrupting something?"
    n "You slowly slink towards the coffee machine."
    deceased "So how was your day, Dr Ai?"
    aikha "It's been fine. My patients have been doing pretty well lately."
    aikha "Maybe you could come over to Path-Para to meet them some time?"
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
    aikha neutral "Huh. Dece. What {i}do{/i} you specialize in?"
    deceased happy "Oh! I'm glad you asked!"
    deceased "The variety of anomalies that exist in our world go far beyond what we've chosen to classify at the Foundation.{nw}"
    show black_screen:
        alpha 0.0
        linear 3.0 alpha 1.0
    deceased "Although we can easily split anomalies by their origins and functions..."
    show black_screen:
        linear 0.7 alpha 0.0
    n "..."
    deceased neutral "...all that being said, I'm basically half an expert in anomalous pathologies myself!"
    deceased "Although not as much as you, certainly. Ha. Ha."
    n "You wish for a commically large piano to drop on your head right about now. Unforunately, it doesn't come."
    aikha "Well, if you ever have time, you're free to come by and take a peak! I mean, I'm sure Aran would be happy to see you."
    deceased "Haha, yeah! Aran..."
    aikha "Unless you're preoccupied. You've been out a lot on field studies lately, so-"
    deceased "No!"
    aikha surprise "..."
    deceased "I mean... it's been kind of slow out there lately. I can set my assistants on it for a bit. I have time! I promise."
    aikha happy "Oh. Of course! I've been meaning to hang out more, but you never seemed to have time. Heh."
    deceased "That's alright. I mean... I'll always make time for you!"
    aikha ":D"
    deceased happy ":D"
    n "Barf."
    n "Well, you've already finished your coffee, so you leg it while you still can."
    player "I'll just... be going now..."
    aikha "Right! You're still here, [player_name]."
    if characters["deceased"]["points"] > 2:
        n "You see Dr. Deceased turn to look at you, goggles glinting gratefully. Score! You must've helped them out."
        n "Or maybe the lights are too bright in here? Anyway, you feel like you've done something right, so you take credit for it."
    else:
        deceased pensive "Wait, who is that?"
        n "No one important! Please leave [player_name] alone."
    aikha "Alrighty then! Meet at Path-Para at 1?"
    deceased happy "Sure thing!"    
    n "The two skip away, hand-in-hand."
    n "Well, sort of. Dr. Deceased is holding Dr. Aikha's coat sleeve, but it's the thought that counts right?"
    return
    
label wing_aikha: 
    n "You whip your head around to look for something- anything- to help."
    n "There's a fully loaded military-grade shotgun in an emergency glass case. Perfect!"
    player "Dr. Deceased! Watch this!"
    n "You smash it open, and- against all ethics and occupation preservation- open-fire on Dr Aikha."
    show aikha unique 
    aikha "AA- eughghghhhgh..."
    n "Is this working?"
    aikha "My spleen... MY EYES..."
    player "Which ones?!"
    deceased "Oh no! Dr. Aikha, it seems that 26 out of 57 of your surface level peepers have been shot!"
    n "Dr. Aikha is still convulsing on the ground. A couple layers of skin peel off as they melt to the floor."
    n "...{i}Did{/i} this work?!"
    deceased "It seems as a response to the external trauma, your body has compensated by turning into an amorphous entity!"
    deceased pensive "...Can this form be injured? Hold on."
    n "Dr. Deceased pulls out their company gun and shoots them."
    aikha "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII{nw}"
    n "You aren't sure if this is supposed to be how this goes."
    deceased "Wow! The bullet is completely absorbed! Dr. Aikha, you never told me what a fascinating biological structure you possess!"
    aikha_unknown "IIIIIIIIIIIIIIIIIIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{nw}"
    n "At this point, you're not really sure what your plan was." 
    n "If you're honest to yourself, this was mostly an excuse to vent your hatred of office romcoms." 
    deceased "Oh, this is wonderful. There's so much data to be collected!"
    deceased "Dr. Aikha, would you perhaps be free to run some more tests in my office?"
    aikha_unknown "EEIAUAGHEAGAUUGAGH??"
    deceased "Alright, great! Man, I've been looking forward to this opportunity for weeks!"
    n "You watch as Dr. Deceased scrubs what's left of Dr. Aikha(?) off the floor and carries it out of the lounge area."
    n "You're not sure, but from this angle, you think you can see a hint of a blush coming from the pile of eyes and flesh."
    player "..."
    player "In front of my coffee?!"
    return