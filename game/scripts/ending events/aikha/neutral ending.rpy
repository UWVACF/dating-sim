label ending_event_neutral_ending:
    fadeout = "image/day events/black screen.png"

    scene bg hallway
    n "Your internship ends today."
    n "You wait nervously outside the HR office, waiting to be called in."
    n "Today will either be your last day at the Foundation, or the start of your new thrilling career."
    egg "[player_name], please come in."

    show bg meeting room

    # rank personnel by points here to determine who shows up

    n "You enter the chilled meeting room."
    show egg at appear
    egg "Congratulations on completing your internship, [player_name]."
    egg "Unfortunately, today will be your last day here."
    n "Ah. You have expected this. Still, you can't help but feel a bit disappointed."
    egg "Because you have been recommended for multiple department-specific position in offsite facilities."
    n "You stare at the Egg in disbelief. He smiles back at you sedately, as he always does."
    n "You have an urge to pop his york."
    show egg at move_to(x_align = 0.0)
    show aikha at appear(x_align = 0.35)
    show firewal at appear(x_align = 0.7)
    show helco at appear(x_align = 1.05)

    # do I write if statements for the all the personnel....

    menu:
        n "Which department do you want to work under?" #is there some way to list all of the choices, but only the top 3 show up ##### or we can scrap this whole choosing thing 
        "Path-pare":
            jump choice1
        "Technology":
            jump choice2
        "Extraterrestrial":
            jump choice3
    
    label choice1:
        aikha happy "That's great! Welcome aboard, new recruit!"
        show fadeout:
            alpha 0.0
            linear 1 alpha 1.0
        
        n "You started your years long career under the Path-para department."
        n "You conducted experiments in labs, collected samples in the field, participated in anomaly containment, and got infected 97 times."
        n "On the 98 time, you unfortunately did not survive. You died a slow, painful death after the anomalous disease overtook your body."
        n "THE END"
        
    label choice2:
        firewal pensive "You would make a great addition to the Wals, [player_name]."
        show fadeout:
            alpha 0.0
            linear 1 alpha 1.0

        n "You started your years long position under the Technological department."
        n "You did wonder, with so many wals already, why would you be needed?"
        n "You found your answer the next day after being relacated at THE WAL head quarters."
        n "You have one job: solve reCAPTCHA for the Walbots."
        n "You spend your netxt 70 years solving captchas in front of a computer that Dr. Firewal provided you."
        n "THE END"

    label choice3:
        helco pensive "I look forward to working with you, Y...[player_name]."
        show fadeout:
            alpha 0.0
            linear 1 alpha 1.0
        
        n "You started you months long job under the Extraterrestrial department."
        n "Unfortunately, you don't actually get to go to space."
        n ""

## temp credits ##

    scene bg hallway

    n "We would like to thank..."

    show aikha unique at appear
    n "{b}Aikha{/b} 'I love spreadsheets' \nFor being the best manaiger, making amazing backgrounds, and polishing sprites!"
    show aikha at disappear

    show ryz unique at appear
    n "{b}Ryan{/b} \"dr lord it coach prof renpyan On his way! write that down\" \nFor coding us funny events full-time at his co-op, on the bus to AN, and probably in his sleep."
    hide aikha
    show ryz at disappear

    show helco panic at appear
    n "{b}Eol{/b} 'stabotage' \nFor always writing simple events into multi-ending complex ones, and tripling the amount of fun but also the amount of work."
    hide ryz
    show helco x at disappear


    show uriel surprise at appear
    n "{b}UFO{/b} '{i}insert 26 pokanom puns here{/i}' \nFor writing a lot of great puns and being our dedicated narrator everytime we do a read through."
    hide helco
    show uriel at disappear

    show deceased happy at appear
    n "{b}Deceased{/b} 'What the sigma' \nFor writing and delivering us great UI from the other side of the planet."
    hide uriel
    show deceased at disappear

    show alex happy at appear
    n "{b}Alex{/b}    GLORY TO THE GREAT FOUNDER \nFor bringing to life the gorgeous sprites of himself, Deceased, Paul, B6, ."
    hide deceased
    show alex at disappear

    show lee unique at appear
    n "{b}Lee{/b} \nFor making the beautiful sprites of themselves, Helco, Syg, ."
    hide alex
    show lee at disappear

    show firewal neutral at appear
    show firewal as wal1 at appear(x_align = 0.2)
    show firewal as wal2 at appear(x_align = 0.8)
    n "{b}Wal{/b} \nFor creating the stunning sprites of himself, Aikha, ."
    hide lee
    show firewal at disappear
    show wa11 at disappear
    show wal2 at disappear

    show b6 at appear
    n "{b}Zak{/b} \nFor drawing the cool sprites of Ryz."
    hide firewal
    hide wal1
    hide wal2
    show b6 at disappear

    show meme at appear
    n "{b}Meem{/b} \nFor making the wonderful sprites of Jessie,."
    hide b6
    show meme at disappear

    #show hampter at appear(x_align = 0.3)
    #show jessie at appear(x_align = 0.7)
    #n "{b}Hampter and Jessie{/b} \nFor drawing our cute chibis!"
    #hide meme
    #show hampter at disappear
    #show jessie at disappear

    #show paul x at appear
    #n "{b}Chris{/b} \nFor making very fire goofy ahh club beats."
    #hide hampter
    #hide jessie
    #show paul x at disappear

    show plutoes unique at appear
    n "{b}Pluto{/b} 'lone alpha' \nFor being a writing consultant especially for Plutoes."
    hide b6 #paul
    show plutoes at disappear

    #show jakob x at appear
    #n "{b}Jakob{/b} 'Mr. President' \nFor letting us use his name as the default player_name (we never asked actually)."
    #hide plutoes
    #show jakob at disappear

    show chan unique at appear(x_align = -0.25)
    n "{b}John{/b} 'and Ethy' \nFor major world building of VACF."
    hide plutoes #jakob
    show chan at disappear

    show syg neutral at appear(x_align = 0.0)
    show caffi neutral at appear(x_align = 0.5)
    show venture neutral at appear(x_align = 1.0)
    n "{b}Syg, Caffi, Moon, Maz,{/b} \nFor being part of VACF and bringing its lore to life."
    hide chan
    show syg at disappear
    show caffi at disappear
    show venture at disappear

    n "And YOU \nFor joining us today!"
    hide syg
    hide caffi
    hide venture
