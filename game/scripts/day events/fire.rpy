label day_event_fire:
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
    aikha "Huh? Then where is he-"
    with hpunch
    n "You hear an explosion from down the hall."
    n "You might have a hunch as to where your tour guide went..."
    hide aikha neutral
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
    helco "Is that something all humans should know of?"
    n "You have more pressing matters right now."
    show bg room hall
    hide helco
    hide uriel
    n "As you turn back, you see a charred Hampter runs through the flames."
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
        linear 3.0 xalign 1.6
    show aikha panic:
        linear 3.0 xalign 1.5
    n "Dr. Firewal drags Dr. Aikha by the collar into his lab."
    aikha "NONONO! [player_name]! CALL MOON! CALL MOOOOOOOOOOON-"
    with hpunch
    n "The wall closes. Call... the moon? Like, the thing in the sky? "
    hide firewal
    hide aikha
# ADD WAL NO.1
    show firewal at appear(x_align = 0.0)
    n "A Wal bot sporting the tag, {i}\"Manager Wal\"{i}, appears with a clipboard."
    wal1 "It appears Wal No.927 combusted after seeing a whole server destroyed by Hampter." 
    wal1 "Do not panic! We will have Wals work to put out the fire."
    wal1 "We calculate that it will take 118098 Wals to completely extinguish the fire."
    n "...118098 Wals?"
    show firewal as dummy_wal:
        yalign 1.0
        xalign -0.5
        linear 2.0 xalign 1.5
    show layer master:
        pause 3.0
        shake

    n "You see a Wal run into the fire, attempt to punch it out, and combust from stress."
    show firewal as dummy_wal:
        yalign 1.0
        xalign -0.5
        linear 2.0 xalign 1.5
    show layer master:
        pause 3.0
        shake
    n "You see a second Wal attempt to do the same... and combust."
    show firewal as dummy_wal:
        yalign 1.0
        xalign -0.5
        linear 2.0 xalign 1.5
    show layer master:
        pause 3.0
        shake
    n "Then a third..."
    
    show firewal as dummy_wal:
        yalign 1.0
        xalign -0.5
        linear 2.0 xalign 1.5
    show layer master:
        pause 3.0
        shake
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


    label convince_the_conference:
        # convince everyone to help, uriel notes theres an extinguisher somewhere you go to grab it and come back to a really suspicious raincloud that has put out the fire. im guessing uriel would probably forget by now what happened due to stress
        # pleases uriel and helco, puts wals out of a job
        scene bg meeting hall
        show uriel at appear(x_align = 0.33)
        show helco at appear(x_align = 0.66)
        show layer master:
            pause 0.6
            block:
                pause 1.65
                shake
                repeat
        
        n "You intelligently decide to implore Dr. Helco and Uriel for their help."
        n "You knock on the door of the conference room-"
        uriel "Do you even have a citizenship anywhere?"
        n "...Might be a bad time, but you really need to help Wal right now. You knock again, louder."
        uriel "...? Is there a problem?"
        show layer master:
            shake(preset="strong")
        player "...That."
        n "Helco just stares blankly at you."
        uriel "Well, the Wals seem to have it handled."
        show layer master:
            shake(preset="strong")
        show layer master:
            pause 0.6
            block:
                pause 1.65
                shake
                repeat
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

    label helco_help:
        show layer master:
            pause 0.6
            block:
                pause 1.5
                shake
                repeat
        n "In spite of his apparent obliviousness, you decide to ask him for his help."
        player "Follow me. Uriel, could you grab the fire extinguisher in the meantime?"
        uriel "Got it."
        show uriel at disappear
        show bg room hall
        show helco:
            xalign 0.66
            yalign 1.0
        n "You lead Dr. Helco out of the room to where Manager Wal is still guiding Walbots into the fire."
        show firewal at appear(x_align = 0.0)
        show firewal as dummy_wal behind helco:
            yalign 1.0
            xalign -0.5
            linear 2.0 xalign 1.5
            repeat
        show layer master:
            pause 0.6
            block:
                pause 1.5
                shake
                repeat
        wal1 "Excellent work, Walbots! Fight valiantly in the name of THE WAL!"
        "Wal No.1093" "FOR THE WAL! FOR THE WAL!"
        player "What to do..."
        n "Helco glances around him and notices a nearby window."
        helco "Say, it's getting a little stuffy in here, [player_name]. Could you open the window for us?"
        n "The window? It's an odd request, but you have no better options."
        n "You walk over to the window and open-"
        n "Out of nowhere, a deluge of water blasts you in the face and floods the hallway."
        n "You come to your senses as the water clears from the hallway."
        player "Dr. Helco?"
        n "You look around and see Dr. Helco standing in a conveniently-sized dry spot next to the wall."
        helco "[player_name], the fire has been extinguished!"
        n "You turn "
        
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
    
    show layer master:
        pause 2.0
        block:
            pause 0.5
            shake
            repeat
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
    $ update_character_points({"firewal": 1, "aikha": -1, "chan": -1})
    return
# have the three options as call... moon?, convince everyone to help, let the wals manage it
# let the wals manage it, wal no1: OK THE FIRE IS PUT DOWN: casualty 100290 wals estimate damage to the area: 200 Million narrator: au-AUGH maybe dont let chan see this one… helco: who's writing the incident report... Chan exits one of the charred offices: Just put in the pile with the rest of them... I'll get to it eventually...
# pleases wal, disappoints aikha

# Past this is a scrap...
    menu: 
        n "What do you do?"
        "Put your full faith in Dr. Aikha and do absolutely nothing":
            jump do_nothing
        "Grab the fire extinguisher that you (probably) saw earlier before":
            jump find_extinguisher
    
    label do_nothing:
        n "You vaguely recall reading an incident report that resembles this exact scenario."
        n "Seems like history really does repeat itself."
        n "Regardless, the last time an event like this happened, it only caused minor injury."
        n "You conveniently forget the \"severe infrastructure and equipment damages\" comment in the report."
        n "\"Dr. Aikha can handle this just fine!\" you think to yourself..."
        n "...as Dr. Firewal explodes with the force of a hydrogen bomb."
        scene bg hospital
        with ComposeTransition(default_fade, before=Fade(0.2, 4.0, 0.0, color="#ffffff"))
        n "When you come to, you're lying in a hospital bed."
        n "The bright lights hurt your eyes, but you're able to barely make out two figures standing beside you."
        show aikha neutral at appear(x_align = 0.33)
        show jessie sad at appear(x_align = 0.66)
        aikha "How you doing, new recruit?"
        jessie "Are you hurting anywhere?"
        n "You attempt to joke about how suffering an explosion point-blank does, in fact, hurt..."
        n "...but it seems your vocal chords have been burned off."
        aikha "I'm sure [player_sub_be] fine."
        aikha "That was nothing someone like [player_obj] can't handle, yeah?"
        player "{sc=1.5}{size=-10}*euuuuuuuuughhhhh*{/size}{/sc}"
        jessie "Haha...yeah...nothing [player_sub] can't handle..."
        aikha "You'll bounce back in no time, [player_name]."
        aikha "Just..."
        aikha "Check in to change your wrappings from time-to-time."
        $ update_character_points({"aikha": 2})
        return # NECESSARY (at least for first label)
    
    label find_extinguisher:
        player "I'm gonna grab the fire extinguisher!"
        n "Unfortunately, it seems Dr. Aikha is too busy being on fire to hear you."
        hide aikha
        hide firewal
        n "You rush out into the hall, heading straight for the fire extinguisher."
        n "Right after you grab it, you hear a massive explosion coming from Dr. Firewal's office."
        n "When the smoke clears, you see Dr. Aikha covered in ash, surrounded by debris."
        show aikha neutral at appear()
        aikha "Hey, new recruit! What's that in your hands?"
        aikha "A fire extinguisher? Good thinking!"
        n "Dr. Aikha takes the fire extinguisher and smashes it into whatever remains of the ceiling."
        n "It was surprisingly effective at spreading the extinguisher foam all around the room."
        show firewal neutral at appear(x_align = 0.33)
        show aikha neutral:
            xalign 0.66
        with move
        firewal "You guys okay?"
        aikha "Yup! We're all good!"
        n "You see a group of janitors already beginning to repair the demolished office."
        n "It seems they're used to this kind of thing happening regularly."
        n "..."
        n "Is that the moon?"
        firewal "Anyways, [player_name],"
        firewal "We'll have to do the tour some other day."
        firewal "I need to write another incident report..."
        $ update_character_points({"firewal": 1, "aikha": 1})
        return
        
