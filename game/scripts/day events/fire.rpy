label day_event_fire:
    scene bg hallway
    with default_fade

    n "You're about to take your lunch break when you receive a notification on your work phone."
    n "{i}\"HELLO [[INTERN], PLEASE REPORT TO [[HALLWAY 7B, OFFICE 16] FOR A GUIDED TOUR. FIREWAL MANAGEMENT.\"{i}"
    n "..."
    n "You're pretty sure this is an automated message but it's not within your pay grade to question invitations from superiors."

    n "You're making your way to the designated location when you notice the sound of rummaging in the vents."
    show layer master:
        matrixcolor SaturationMatrix(1.0)
        linear 1.0 matrixcolor SaturationMatrix(0.0) 
# make screen black and white if possible? i assume its not so maybe black overlay
    n "Oh god."
    n "Is this the fated containment breach you negligently skimmed over the instructions for in your employee manual?"
    n "You're not equipped for this!"

# make this next dialogue dependant on the company gun event in the future
    if "company_issued_gun" not in seen_events:
        n "You've yet to receive company-issued gun!"
# screen shake for pep talks! WHERE IS YOUR ANGER RAHHHHHH!!!!!!!!

    n "Okay."
    n "You got this!"
    if day_number == 0:
        n "Nevermind that it's your first day!"
    elif day_number == 1:
        n "You've been working here for [day_number] day!"
    else:
        n "You've been working here for [day_number] days!"

    n "Surely whatever horrific anomaly this is must be harmless if there's no alarms going off!"
    n "You muster up the courage to look into the vent."
    show hampter happy 
    hampter "Hiiii [player_name]!"
    show layer master:
        matrixcolor SaturationMatrix(0.0)
        linear 1.0 matrixcolor SaturationMatrix(1.0) 
    n "Oh good... it's just Hampter."
    player "What are you doing in there, Hampter?"
    show hampter panic
    n "Hampter shuffles to hide something behind her back."
    show hampter happy 
    hampter "It's my snack time!"
    n "..."
    n "I guess you can't judge other personnel for where they decide to take their lunch breaks."
    n "I mean... you were supposed to be on break before this meeting anyways."
    show hampter happy at disappear
    n "As you continue to your designated meeting spot, you hear a conversation."
# make it ??? for names
    aikha_unknown "...So anyways, that's why I infected 1700 axolotls."
    firewal_unknown "Mmm. Understandable."

    show aikha neutral at appear(x_align = 0.33)
    show firewal neutral at appear(x_align = 0.66)

    aikha "It was all worth it in the end when- oh! Hey, new recruit! Whatcha doing here?"
# show firewal pensive
    show firewal pensive
    n "Dr. Firewal checks his wrist cuff."
    firewal "...Apparently Wal No.927 invited [player_obj] here to show [player_obj] around."
    n "Wal... No.927?"
    aikha "Huh? Then where is he-"
    with hpunch
    n "You hear an explosion from down the hall."
# Please make the screen shake
    n "You might have a hunch as to where your tour guide went..."
    n "You rush to the source of the sound!"
    n "Dr. Aikha and Dr. Firewal casually trail behind... guess this is somewhat common."

# a crowd has gathered around the fire, uriel and helco added
# seems like a charred hampter is the culprit
# firewal presses a few buttons on his cuff, a wall splits open showing a vast lab narrator "huh thats not in the emergency escape route floor plan", drags Dr. aikha by the collar and leaves with them aikha shouts while being dragged away "CALL MOON CALL MOON!!!" the narrator is like... "call the moon? or a person named moon? What?"
# something something helco is staring at the fire
# wal no.1 shows up to "manage" the fire which is actually just throwing wal bots into the fire, causing a stress fire loop. "it seems like wal no.927 combusted after seeing a whole server destroyed by hampter. do not worry! we have wal bots working to put out the fire. we calculate that it will take 118098 wals to completely extinguish the fire."
# have the three options as call... moon?, convince everyone to help, let the wals manage it
# call moon, aikha is pleased, wal no.1 reports the wal unemployment to firewal... no context and gets you in trouble with firewal
# convince everyone to help, uriel notes theres an extinguisher somewhere you go to grab it and come back to a really suspicious raincloud that has put out the fire. im guessing uriel would probably forget by now what happened due to stress
# pleases uriel and helco, puts wals out of a job
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
        
