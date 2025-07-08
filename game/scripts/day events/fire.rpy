label day_event_fire:
    image moonposter = "images/cgs/moonposter.png" 
    image greenbeam = "images/day events/green screen.png"
    image flashbang = "images/day events/white screen.png"
    image blueeeee = "images/day events/haze blue strong.png"
    $ put_wals_out_of_a_job = False

    scene bg hallway
    with default_fade

    n "You're about to take your lunch break when you receive a notification on your work phone."
    n "{i}\"HELLO [[INTERN], PLEASE REPORT TO [[HALLWAY 7B, OFFICE 16] FOR A GUIDED TOUR. FIREWAL MANAGEMENT.\"{i}"
    n "..."
    n "You're pretty sure this is an automated message but it's not within your pay grade to question invitations from superiors."
    show bg door
    n "You're making your way to the designated location when you notice the sound of rummaging in the vents."
    show layer master:
        matrixcolor SaturationMatrix(1.0)
        linear 1.0 matrixcolor SaturationMatrix(0.0) 
    n "Oh god."
    n "Is this the fated containment breach you negligently skimmed over the instructions for in your employee manual?"
    n "You're not equipped for this!"

# make this next dialogue dependant on the company gun event in the future
# this dialogue is now dependent on the company gun event - signed ryan
    if "company_issued_gun" not in seen_events:
        n "You've yet to receive your company-issued gun!"
# screen shake for pep talks! WHERE IS YOUR ANGER RAHHHHHH!!!!!!!!
# i politely refuse this request - signed ryan

    n "Okay."
    n "You got this!"
    if day_number == 1:
        n "Nevermind that it's your first day!"
    elif day_number == 2:
        n "You've been working here for 1 day!"
    else:
        n "You've been working here for [day_number - 1] days!"

    n "Surely whatever horrific anomaly this is must be harmless if there's no alarms going off!"
    show bg door:
        xcenter 0.95
        ycenter 0.0
        zoom 2.0
    n "You muster up the courage to look into the vent."
    show hampter happy 
    hampter "Oh! Hiiii [player_name]!"
    show layer master:
        matrixcolor SaturationMatrix(0.0)
        linear 1.0 matrixcolor SaturationMatrix(1.0) 
    n "Oh good... it's just Hampter."
    player "What are you doing in there, Hampter?"
    show hampter panic
    n "Hampter shuffles to hide something behind her back."
    show hampter happy 
    hampter "Just passing by! Nothing to see here!"
    n "..."
    n "I guess you can't judge other personnel for where they decide to take their lunch breaks."
    n "I mean... you were supposed to be on break before this meeting anyways."
    show hampter happy at disappear
    hide bg
    show bg hallway
    n "As you continue to your designated meeting spot, you hear a conversation."
    aikha_unknown "...So anyways, that's why I infected 1700 axolotls."
    firewal_unknown "Mmm. Understandable."

    show aikha neutral at appear(x_align = 0.33)
    show firewal neutral at appear(x_align = 0.66)

    aikha "It was all worth it in the end when- oh! Hey, new recruit! Whatcha doing here?"
    show firewal pensive
    n "Dr. Firewal checks his wrist cuff."
    firewal "...Apparently Wal No.927 invited [player_obj] here to show [player_obj] around."
    n "Wal... No.927?"
    aikha surprise "Huh? Then where is he-"
    with hpunch
    n "You hear an explosion from down the hall."
    n "You might have a hunch as to where your tour guide went..."
    hide aikha surprise
    hide firewal pensive
    show bg room hall
    n "You rush to the source of the sound, with Dr. Aikha and Dr. Firewal casually trailing behind you."
    show aikha neutral at appear(x_align = 0.0)
    show firewal neutral at appear(x_align = 1.0)
    n "They look indifferent. Guess this is a common occurence."
    show haze orange onlayer top:
        alpha 0.0
        linear 0.5 alpha 0.5
        block:
            ease 0.5 alpha 0.3
            ease 0.5 alpha 0.5
            repeat
    n "You stop in front of a blazing inferno."
    uriel_unknown "How do you not know what a birth certificate is?"
    show bg meeting hall
    hide aikha neutral
    hide firewal neutral
    show uriel panic:
        xalign 0.33
        yalign 1.0
    show helco neutral:
        xalign 0.66
        yalign 1.0
    n "You glance over to the nearby conference room and see a frustrated Uriel and confused Dr. Helco."
    helco surprise "Is that something all humans should know of?"
    n "You have more pressing matters right now."
    show bg room hall
    hide helco
    hide uriel
    n "As you turn back, you see a charred Hampter run through the flames."
    show hampter panic at appear(x_align = 0.5)
    hampter "It wasn't me!!! A Wal found me and just combusted! It wasn't my fault!"
    n "The frayed wires in Hampter's mouth suggest otherwise." 
    show aikha neutral at appear(x_align = 0.0)
    show firewal upset at appear(x_align = 1.0)
    n "Dr. Firewal sighs and taps the screen on his cuff a few times."
    with hpunch
    n "Suddenly, the wall behind you splits open, revealing a vast technology-filled lab."
    n "Huh. That's not on the floor plan."
    firewal "Manager Wal will handle this. Come on, Ai."
    show aikha panic
    show firewal upset:
        linear 1.5 xalign 0.1
    aikha "Huh? Nonono! Not again!"
    show firewal upset:
        linear 3.0 xalign 1.7
    show aikha panic:
        linear 3.0 xalign 1.7
    n "Dr. Firewal drags Dr. Aikha by the collar into his lab."
    aikha "NONONO! [player_name]! CALL MOON! CALL MOOOOOOOOOOON-"
    with hpunch
    n "The wall closes. Call... the moon? Like, the thing in the sky? "
    hide firewal
    hide aikha
# ADD WAL NO.1
    show firewal:
        alpha 0.0
        xzoom -1.0
        alpha 1.0
        appear(x_align = 0.0)
    n "A Wal bot sporting the tag, {i}\"Manager Wal\"{/i}, appears with a clipboard."
    wal1 "It appears Wal No.927 combusted after seeing a whole server destroyed by Hampter." 
    wal1 "Do not panic! We will have Wals work to put out the fire."
    wal1 "We calculate that it will take 118098 Wals to completely extinguish the fire."
    n "...118098 Wals?"
    show firewal as dummy_wal:
        xzoom -1.0
        yalign 1.0
        xalign -0.5
        linear 2.0 xalign 1.5
    $ shake_screen(delay=3)

    n "You see a Wal run into the fire, attempt to punch it out, and combust from stress."
    show firewal as dummy_wal:
        xzoom -1.0
        yalign 1.0
        xalign -0.5
        linear 2.0 xalign 1.5
    $ shake_screen(delay=3)
    n "You see a second Wal attempt to do the same... and combust."
    show firewal as dummy_wal:
        xzoom -1.0
        yalign 1.0
        xalign -0.5
        linear 2.0 xalign 1.5
    $ shake_screen(delay=3)
    n "Then a third..."
    
    show firewal as dummy_wal:
        xzoom -1.0
        yalign 1.0
        xalign -0.5
        linear 2.0 xalign 1.5
    $ shake_screen(delay=3)
    n "How... long is this going to take?"

    menu: 
        n "You should step in."
        "Call... the moon?":
            jump call_moon
        "Convince the others to help.":
            jump convince_the_conference
        "Let the Wals manage it.":
            jump wal_management
   
    label call_moon:
        # call moon, aikha is pleased, wal no.1 reports the wal unemployment to firewal... no context and gets you in trouble with firewal
        n "You have no idea how to \"call the moon\". Perhaps you can ask someone who's more informed."
        hide firewal
        hide dummy_wal
        show moonposter:
            zoom 0.4 
            xalign 0.5 
            yalign 0.1
        n "You jog down the hallways in search of other people when a poster on the wall catches your eye. It reads, {b}{i}When in doubt? SHOUT! SHOUT! SHOUT!{/b}{/i}"
        hide moonposter
        n "Might as well give it a try. Worst come to worst, you just look like a lunatic yelling in the hallway."
        player "{b}{size=+5}MOON!{/size}{/b}"
        "Wal No.571" "{sc}{size=+10}{b}FOR THE WAL! FOR THE WAL!{/b}{/size}{/sc}"
        n "Well, at least you're not the only lunatic in this hallway. You decide to try again."
        player "{b}{size=+10}MOON!{/size}{/b}"
        n "Nobody answers you. You're beginning to think that the poster on the wall is there to trick gullible interns like you."
        n "You decide to try one last time."
        player "{b}{size=+15}MOON!{/size}{/b}"
        pause 3
        n "Well, guess this isn't working-"
        $ shake_screen()
        moon "{size=+20}HELLO. WHAT SEEMS TO BE THE PROBLEM?{/size}"
        $ shake_screen()
        moon "{size=+20}OH. I SEE. IT'S A FIRE.{/size}"
        $ shake_screen()
        moon "{size=+20}DEAR INTERN, COULD YOU STEP BACK A BIT?{/size}"
        n "You comply. You peek out the window and see a faint green glow on the moon."
        show greenbeam onlayer top:
            alpha 0
            easeout 0.6 alpha 1.0
            easeout 0.4 alpha 0
        pause 0.6
        n "Then a giant bright beam shoots from the moon and through the window..."
        show bg meeting hall
        show greenbeam onlayer top:
            alpha 1.0
        show uriel panic:
            xalign 0.33
            yalign 1.0
        show helco neutral:
            xalign 0.66
            yalign 1.0
        show greenbeam onlayer top:
            easeout 0.6 alpha 0
        pause 0.6
        n "...and through the two unfortunate Department Heads who have just walked out of their meeting."
        hide helco
        hide uriel
        show bg room hall
        show greenbeam onlayer top:
            alpha 1
            easeout 0.4 alpha 0
        pause 0.6
        n "The beam hits the fire."
        show flashbang onlayer top:
            alpha 0.0
            linear 0.7 alpha 1.0
            linear 0.7 alpha 0.0
        pause 0.1
        hide haze orange onlayer top
        n "Huh. That works."
        hide flashbang onlayer top
        hide greenbeam onlayer top
        player "{size=+15}...Thanks Moon!{/size}"
        $ shake_screen()
        moon "{size=+20}NO PROBLEM! LET ME KNOW IF THERE'S ANOTHER MESS TO CLEAN! :D{/size}"
        show bg meeting hall
        show uriel unique:
            xalign 0.33
            yalign 1.0
        show helco sad:
            xalign 0.66
            yalign 1.0
        n "You see a half distinegrated Uriel and an unusual expression on Dr. Helco's face."
        helco "{i}ughhhhhhhh{/i}"
        player "Dr. Helco? Are you okay?"
        helco "..."
        helco neutral "Yes. Yes I'm fine. Was that green beam...your doing?"
        player "Oh, I called Moon to help with the fire."
        helco neutral "...I see."
        show helco at disappear
        n "You watch as Dr. Helco hurries off. You feel a little bad."
        hide helco
        uriel panic "Huh..?"
        uriel neutral "Ah. It must have been the fire."
        uriel "Dammit. I liked this shirt."
        show uriel at disappear
        n "Uriel walks off, a little dazed."
        hide uriel
        n "...Well, that's sorted."
        n "You also turn around to leave when you feel a cold hand grab your shoulder."

        # TODO: change offset
        show bg room hall
        show firewal fury
        show firewal fury as wal1:
            xalign -0.1
            yalign 1.3
        show firewal fury as wal2:
            xalign 0.1
            yalign 1.3
        show firewal fury as wal3:
            xalign 0.3
            yalign 1.3
        show firewal fury as wal4:
            xalign 0.7
            yalign 1.3
        show firewal fury as wal5:
            xalign 0.9
            yalign 1.3
        show firewal fury as wal6:
            xalign 1.1
            yalign 1.3

        wal1 "You've just put 118072 wals out of a job, [player_name]."
        wal1 "THE WAL will hear about this transgression."
        hide firewal
        hide wal1
        hide wal2
        hide wal3
        hide wal4
        hide wal5
        hide wal6
        n "They all march into a wall in union."
        n "You feel the wrath of several million walbots. You contemplate whether you should sleep with a fire extinguisher tonight."

        $ put_wals_out_of_a_job = True
        # you put wals out of a job, angry wals
        $ update_character_points({"firewal": -2, "helco": 0, "uriel": 0, "aikha": 2, "moon": 1})
        return

    label convince_the_conference:
        # convince everyone to help, uriel notes theres an extinguisher somewhere you go to grab it and come back to a really suspicious raincloud that has put out the fire. im guessing uriel would probably forget by now what happened due to stress
        # pleases uriel and helco, puts wals out of a job
        scene bg meeting hall
        show uriel at appear(x_align = 0.33)
        show helco at appear(x_align = 0.66)
        $ shake_screen(delay=0.6, interval=1.5, repeat=True)
        
        n "You intelligently decide to implore Dr. Helco and Uriel for their help."
        n "You knock on the door of the conference room-"
        uriel "Do you even have any citizenship anywhere?"
        n "...Might be a bad time, but you really need to help Wal right now. You knock again, louder."
        uriel "...? Is there a problem?"
        $ shake_screen(preset="strong")
        player "...That."
        n "Helco just stares blankly at you."
        uriel "Well, the Wals seem to have it handled."
        $ shake_screen(preset="strong")
        "Wal No.571" "FOR THE WAL! FOR THE WAL!"
        n "From down the hall, you see Manager Wal give you an enthusiastic thumbs up."
        uriel "...On second thought, maybe this could go faster."
        uriel "I believe there was a fire extinguisher in hallway 7C, between offices 5 and 6."
        helco "Oh! This is a fire!"
        player "...Yup!"
        n "He goes back to staring at you absentmindedly."
        player "Hey, Dr. Helco?"
        helco "Yes?"
        menu:
            n "What should you do?"
            "Find the fire extinguisher yourself, and enlist the two of them to watch over the fire.":
                jump fire_extinguisher
            "Accept Dr. Helco's help, and enlist Uriel to find the fire extinguisher.":
                jump helco_help
        
    label fire_extinguisher:
        n "Let's just go for the fire extinguisher. At least we know it'll do something."
        player "I'll get the fire extinguisher. Can you two just watch the fire and make sure the fire doesn't get worse?"
        uriel "That should be fine. Just get back quickly."
        n "Helco gives you a thumbs up as you turn to leave."
        scene bg room hall
        # fire extinquisher cg
        n "You find a glaring box anchored on the wall that reads: \n{b}SUPER EXTINGUISHER \nDO NOT USE UNLESS ABSOLUTELY NECESSARY{/b}"
        n "You sure hope this is powerful enough to put out that fire. With the time your weak stamina took to get here, the fire probably got 10 times as big."
        # hide cg
        n "You break the glass case and take out the extinguisher and run back towards the blazing heat."
        scene bg meeting hall
        show uriel:
            xalign 0.33
            yalign 1.0
        show helco pensive:
            xalign 0.66
            yalign 1.0
        with default_fade
        player "Uriel! I got the extinguisher!"
        uriel "Great! Go use it!"
        player "...Me? But I have no firefighting training."
        show helco happy
        uriel "Well, neither do I. Plus, the last time I used that...I can't remember what happended."
        n "Helco gives you an enthusiastic thumbs up, again."
        n "Geez. These department heads really know how to avoid responsibility. Still, you suppose this is what differentiates them from regular employees like you."
        hide uriel at disappear
        hide helco at disappear
        scene bg room hall
        show firewal:
            xzoom -1.0
            xalign 0.0
            yalign 1.0
        show firewal as dummy_wal:
            xzoom -1.0
            yalign 1.0
            xalign -0.5
            linear 2.0 xalign 1.5
            repeat
        $ shake_screen(delay=0.6, interval=1.5, repeat=True)
        n "You muster up the courage and walk up to the fire surrounded by the Wals."
        
        menu:
            wal1 "Oh, [player_name], please don't approach the area, it's dangerous-"
            "Pull the pin off the extinguisher.":
                jump fire_extinguish

        label fire_extinguish:
            show firewal talk
            n "You ignore Manager Wal and pull off the pin while aiming it towards the fire."
            n "You see something come out of the nozzle. The substance is a strange crystal blue. It envelops you."
            show blueeeee onlayer top:
                alpha 0.0
                linear 0.3 alpha 0.55
            n "You feel your entire body now coated in a cooling blue film, like an extra layer of skin. It is so cool that you can no longer feel the heat of the fire."
            n "You shake the now empty extinguisher. Well, that didn't do shit."
            n "Suddenly, your legs move forwards uncontrollably towards the flames. It's as if a strong force is pulling your muscles and moving them by your skin."
            n "Wait, skin?"
            player "Wait wait wait wait help-!"
            firewal "[player_name]? Could you please step away?"
            show blueeeee onlayer top:
                alpha 0.55
                easein 0.3 alpha 1.0
            pause 0.3
            scene bg room hall 
            $ shake_screen()
            show haze orange onlayer top:
                alpha 0.0
            show blueeeee onlayer top:
                alpha 1.0
                pause 0.1
                easein 0.3 alpha 0.55
            n "Your blue skin ignores Manager Wal and hurls you into the fire."
            hide haze orange onlayer top
            n "The fire is almost instantly quenched. Part of your new blue skin extends to cover and smother out any remaining flickers."
            show firewal:
                xalign 0.5
                yalign 1.0
            firewal surprise "Oh."
            firewal "You used the SUPER EXTINGUISHER?"
            player "{b}{color=#5b7cc7}Yes, I did.{/color}{/b}"
            firewal "Ah. Did you not see it reads DO NOT USE UNLESS ABSOLUTELY NECCESSARY?"
            n "You feel a chill down your spine."
            player "{b}{color=#5b7cc7}{cps=*0.6}Was this not an emergency?{/cps}{/color}{/b}"
            firewal "No, us Wals could've taken care of it. That extinguisher isn't to be used unless {i}ABSOLUTELY NECCESSARY{/i}."
            n "You feel the coldness in his words."
            firewal pensive "Requesting backup! Apprehension and medical units!"
            player "{b}{color=#5b7cc7}{cps=*0.4}What's going on?{/cps}{/color}{/b}"
            n "You feel very cold. As if your skin is turning into ice."
            firewal upset "The extinguisher you used has an anomaly in it. The anomaly thrives by absorbing heat."
            player "{b}{color=#5b7cc7}{cps=*0.2}Is that so..?{/cps}{/color}{/b}"
            firewal "And after the heat from the fire is absorbed, the next closest heat source is you."
            n "Your eyes slowly close as Manager Wal speaks the last words."
            scene bg sickbay
            show blueeeee onlayer top:
                linear 0.3 alpha 0.0
            with default_fade
            n "You awaken in the foundation infirmary."
            hide blueeeee onlayer top
            show uriel at appear
            uriel "Oh, you have awoken."
            uriel happy "Thanks for putting out the fire! And...using the extinguisher."
            uriel "No wonder I do not remember what happened the last time I used it."
            uriel neutral "The Wals are less pleased with you than I am, since they have to clean up the anomaly you released even though it was not ABSOLUTELY NECCESSARY."
            player "So when {i}exactly{/i} is ABSOLUTELY NECCESSARY?"
            show uriel surprise
            n "Uh oh. You don't like that new look on Uriel's face."
            uriel fury "It is clearly stated in the foundation code, as well as the onboarding trainings. You should have seen it!"
            uriel upset "Since you do not know, I shall recite it for you."
            uriel "{cps=*2}Code 2: Emergency classfications and counter measures. Emergencies that occurs at the foundation can normally be classified into 5 catagories. They are level 1(mild), level 2 (moderate), level 3 (threat), level 4 (severe), and level 5 (dangerous).{/cps}{cps=*4} Level 5 can be further divided into just dangerous, or ABSOLUTELY DANGEROUS. All equipment used to tackle emergencies have a corresponding classification tag for which emergency level it can be used in. {/cps}{cps=*6}This is decided through the evaluation of risk, cost, danger of situations and technical skills required. The fire today would at most only be classified as a high level 2 emergency-{/cps}"
            n "Your brain decides that this amount of information is too much to handle and overloads."
        $ update_character_points({"firewal": -1, "helco": 0, "uriel": 2, "aikha":-1, "moon": 0})
        return

    label helco_help:
        $ shake_screen(delay=0.6, interval=1.5, repeat=True)
        n "In spite of his apparent obliviousness, you decide to ask him for his help."
        player "Follow me. Uriel, could you grab the fire extinguisher in the meantime?"
        uriel "Got it."
        show uriel at disappear
        scene bg room hall
        n "You lead Dr. Helco out of the room to where Manager Wal is still guiding Walbots into the fire."
        show firewal:
            alpha 0.0
            xzoom -1.0
            alpha 1.0
            appear(x_align = 0.0)
        show firewal as dummy_wal:
            xzoom -1.0
            yalign 1.0
            xalign -0.5
            linear 2.0 xalign 1.5
            repeat
        $ shake_screen(delay=0.6, interval=1.5, repeat=True)
        wal1 "Excellent work, Walbots! Fight valiantly in the name of THE WAL!"
        "Wal No.1093" "FOR THE WAL! FOR THE WAL!"
        player "What to do..."
        scene bg room hall
        show helco 
        n "Helco glances around him and notices a nearby window."
        helco "Say, it's getting a little stuffy in here, [player_name]. Could you open the window for us?"
        n "The window? It's an odd request, but you have no better options."
        show helco at disappear
        n "You walk over to the window and open-"
        hide helco
        $ shake_screen(preset="rumble", repeat=True, persist=9999)
        show haze orange onlayer top:
            linear 0.5 alpha 0.0
        n "Out of nowhere, a deluge of water blasts you in the face and floods the hallway."
        $ shake_screen(duration=0)
        n "You come to your senses as the water clears from the hallway."
        player "Dr. Helco?"
        show helco happy at appear(x_align = 1.0)
        n "You look around and see Dr. Helco standing in a conveniently-sized dry spot next to the wall."
        helco neutral "[player_name], the fire has been extinguished!"
        n "You turn to see the place where the fire used to be, along with quite a few drenched Wals."
        show firewal fury at appear(x_align = 0.3)
        show firewal fury as wal1:
            xalign 0.1
            yalign 1.3
        show firewal fury as wal2:
            xalign 0.5
            yalign 1.3
        wal "You've just put 118072 Wals out of a job, [player_name], and we will need to be thoroughly dried before we can be assigned any more tasks."
        wal "This will be reported to THE WAL and you'll face the consequences."
        show firewal fury at disappear
        show firewal fury as wal1 at disappear
        show firewal fury as wal2 at disappear
        n "They make their ways into the wall, and you are left with a giant puddle of later where the fire and Wals once were."
        hide firewal
        hide wal1
        hide wal2
        show uriel at appear(x_align = 0.2)
        uriel "Oh, it is already out. Good, I was not sure that this could deal with a fire that big."
        player "...Yea. But we also drenched some Wals."
        helco "I'm sure they'll be fine. They won't survive fighting the fire, anyways."
        show uriel at disappear
        show helco at disappear
        n "You wonder if Dr. Helco will be willing to help you put out a fire again when you get set ablazed by the Wals."
        hide uriel
        hide helco
        $ update_character_points({"firewal": -2, "helco": 1, "uriel": 0, "aikha":-1, "moon": 0})
        return
        
    label wal_management:
    show firewal as dummy_wal:
        yalign 1.0
        block:
            xalign -0.5
            linear 2.0 xalign 1.5
            repeat
    show firewal as dummy_wal_2:
        yalign 1.0
        pause 1.0
        block:
            xalign -0.5
            linear 2.0 xalign 1.5
            repeat
    
    $ shake_screen(delay=2, interval=0.5, repeat=True)
    n "Actually, nah. Surely these Wals got it under control!"
    n "I mean. They're already 0.005%% done!"
    n "0.0059%% done now..."
    n "....Sunk cost fallacy..."
    n "Oh, look at that! Your break is over. Better... get going..."
    show haze orange onlayer top:
        linear 1.0 alpha 0.0
    scene hallway
    with default_fade
    hide firewal
    hide dummy_wal
    hide dummy_wal_2
    show layer master
    n "Before you clock out for the day, you receive a ping on your phone."
    hide haze orange onlayer top
    n "{i}\"THE FIRE IN [[HALLWAY 7B] HAS BEEN PUT OUT.\"{/i}"
    n "Well that's reassuring, I suppose."
    n "{i}\"CASUALTY: 100290 WALS.\"{/i}"
    n "Oh! That's less than expected... that's good."
    n "{i}\"ESTIMATED DAMAGE: $200 MILLION.\"{/i}"
    n "Oh... no."
    n "You'd better hope Chan doesn't find out about this."
    n "You hear a ping behind you."
    show chan panic
    n "You suspect it might be a little too late for that..."
    $ update_character_points({"firewal": 2, "helco": 0, "uriel": 0, "aikha":2, "moon": 0})
    return


# have the three options as call... moon?, convince everyone to help, let the wals manage it
# let the wals manage it, wal no1: OK THE FIRE IS PUT DOWN: casualty 100290 wals estimate damage to the area: 200 Million narrator: au-AUGH maybe dont let chan see this one… helco: who's writing the incident report... Chan exits one of the charred offices: Just put in the pile with the rest of them... I'll get to it eventually...
# pleases wal, disappoints aikha

