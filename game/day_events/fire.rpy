label day_event_fire:
    scene bg office
    with default_fade
    aikha "...so anyways, that's why I killed 1700 axolotls."
    firewal "Mmm."

    show aikha neutral at appear(x_align = 0.33)
    show firewal neutral at appear(x_align = 0.66)

    aikha "It was all worth it in the end when - oh! Hey, new recruit! Whatcha doing here?"
    firewal "I invited [player_obj] here to show [player_obj] around my department."
    firewal "It is 4:30 am as of writing this dialogue"
    firewal "I have no fucking clue what to write"
    aikha "I'm just gonna write whatever so I can work on implementation"
    firewal "Holy shit look at that [[thing]"
    firewal "That [[thing] is making me stressed I'm going to spontaneously combust"
    aikha "Oh no Dr. Firewal is spontaneously combusting"

    menu: 
        "What do you do?"
        "Put your full faith in Dr. Aikha and do absolutely nothing":
            jump do_nothing
        "I think there was a fire extinguisher down the hall...right?":
            jump find_extinguisher
    
    label do_nothing:
        "You vaguely recall reading an incident report that resembles this exact scenario."
        "Seems like history really does repeat itself."
        "Regardless, the last time an event like this happened, it only caused minor injury."
        "You conveniently forget the \"severe infrastructure and equipment damages\" comment in the report."
        "\"Dr. Aikha can handle this just fine!\" you think to yourself..."
        "...as Dr. Firewal explodes with the force of a hydrogen bomb."
        scene bg hospital
        with ComposeTransition(default_fade, before=Fade(0.2, 4.0, 0.0, color="#ffffff"))
        "When you come to, you're lying in a hospital bed."
        "The bright lights hurt your eyes, but you're able to barely make out two figures standing beside you."
        show aikha neutral at appear(x_align = 0.33)
        show jessie sad at appear(x_align = 0.66)
        aikha "How you doing, new recruit?"
        jessie "Are you hurting anywhere?"
        "You attempt to joke about how suffering an explosion point-blank does, in fact, hurt..."
        "...but it seems your vocal chords have been burned off."
        aikha "I'm sure [player_sub_be] fine!"
        aikha "That was nothing someone like [player_obj] can't handle, yeah?"
        "You fail to make any sort of sound in acknowledgement."
        jessie "Haha...yeah...nothing [player_sub] can't handle..."
        aikha "You'll be back on your feet in no time, [player_name]!"
        aikha "Just..."
        aikha "Stay away from mirrors for the time being..."
        "You make one last attempt at producing a sound before losing consciousness once more."
        scene bg hospital
        with default_fade
        "The bright eyes of the hospital ceiling blind your eyes yet again."
        "But miraculously...your body feels as good as new."
        show firewal neutral at appear
        firewal "Hey, [player_name], how're you feeling?"
        player "I feel great, but..."
        player "How did I recover so quickly?"
        firewal "You see...we used this little thing called:"
        firewal "\"Plot armour.\""
        player "..."
        "You feel grateful that Dr. Firewal checked up on you."
        "You feel closer with him."
        $ update_intimacy_points({"firewal": 2})
        return # NECESSARY (at least for first label)
    
    label find_extinguisher:
        player "I'm gonna grab the fire extinguisher!"
        "Unfortunately, it seems Dr. Aikha is too busy being on fire to hear you."
        hide aikha
        hide firewal
        "You rush out into the hall, beelining for the fire extinguisher"
        "Right after you break the glass and grab it, you hear a massive explosion coming from Dr. Firewal's office."
        "When the smoke clears, you see Dr. Aikha covered in ash, surrounded by debris."
        show aikha neutral at appear(x_align = 0.5)
        aikha "Hey, new recruit! What's that in your hands?"
        aikha "A fire extinguisher? Good thinking!"
        "Dr. Aikha takes the fire extinguisher and smashes it into whatever remains of the ceiling."
        "It was surprisingly effective at spreading the extinguisher foam all around the room."
        show firewal neutral at appear(x_align = 0.33)
        show aikha neutral:
            xalign 0.66
        with move
        firewal "You guys okay?"
        aikha "Yup! We're all good!"
        "You see a group of janitors already begin to repair the demolished office."
        "It seems they're used to this kind of thing happening regularly."
        "..."
        "Is that a moon?"
        firewal "Anyways, [player_name],"
        firewal "We'll have to do the tour some other day."
        firewal "I need to write another incident report..."
        "The absurdity of the situation hits you, and you feel closer with the two of them."
        $ update_intimacy_points({"firewal": 1, "aikha": 1})
        return
        