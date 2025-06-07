transform shock:
    alpha 0.0
    linear 0.05 alpha 1.0
    linear 1.0 alpha 0.0

label day_event_in_the_dark:
    scene bg lounge
    with default_fade

    n "It's coffee time! Coffee coffee coffee coffee"

    show lee at appear(x_align = 0.33)
    show helco at appear(x_align = 0.66)
    n "You run into some familiar faces in the lounge."
    lee "Heya, Helco! Do you want a glow-in-the-dark sticker?"
    helco "Hmm? What's that?"
    lee "It's a sticker that glows in the dark! See? Oh, hey newbie! Do you want one too?"

    show screen qte(time = 2.0, act=Jump("itd_lights_go_out"), hidden=True)
    menu:
        n "Do you want a glow in the dark sticker?"
        "Of course!":
            jump itd_lights_go_out
        "No thanks.":
            jump itd_lights_go_out
    
label itd_lights_go_out:
    hide screen qte

    show black_screen zorder 10:
        alpha 1.0
        0.15
        alpha 0.0
        0.35
        alpha 1.0
    n "Suddenly, the lights flicker and go out."
    n "You hear Dr. Lee start retching."
    helco "Looks like an anomaly broke out. We should go examine it."
    hide lee
    hide helco
    n "You walk forwa-"
    with hpunch
    player "Was that table always there??"
    lee "W-Wait, hang on!"
    hide black_screen

    show lee at appear(x_align = 0.5):
        matrixcolor TintMatrix("#ff7070")
    show black_screen behind lee, yellow_screen
    n "Dr. Lee becomes one with their stickers and starts glowing in the dark."
    lee "There! Can you see now?"
    player "Oh, neat!"
    lee "Haha, thanks! Sorry it's not that strong, but Helco and I can both see in the dark, so we'll guide you."
    player "...Are you okay?"
    lee "Y-yeah!"
    n "Dr. Lee throws up."
    helco "The anomaly sucks in all electromagnetic radiation in a radius around it. It's only natural that Dr. Lee, who's inherently radioactive, is experiencing adverse symptoms."
    player "All electromagnetic radiation, huh?"
    n "You pull your phone out and tap the screen. Sure enough, it doesn't power on."
    lee "...Hang on, this anomaly wasn't in the database. How do you know so much about this?"
    helco panic "..."
    helco "Shall we go?"
    n "He quickly exits the room."
    n "You decide to pursue the question later. You begin walking out the..."
    $ itd_correct_room = False
    menu:
        n "...Where were you?"
        "Dr. Lee's office.":
            n "Right! Dr. Lee's office!"
            n "Then, the door should be around here-"
        "Dr. Helco's office.":
            n "Right! Dr. Helco's office!"
            n "Then, the door should be around there-"
        "The lounge.":
            n "Right! The lounge!"
            n "The door should be this way, then."
            $ itd_correct_room = True
        "The hallway.":
            n "Right! You were in the hallway."
            n "Well, let's go this way-"
    
    if not itd_correct_room:
        with hpunch
        n "...You walk into a wall."
        n "Oops. Turns out you were in the lounge."
    
    n "You exit into the hallway behind a faintly glowing Dr. Lee. You really hope you don't walk into Dr. Helc-"
    with hpunch
    helco "Ow!"
    player "Sorry!"
    n "You walked into Dr. Helco."
    n "You're a bit tired of walking into things, but you decide it's best to not ask Dr. Lee to glow brighter. They're already not doing too well as is."
    lee panic "..."
    player "Say, Dr. Lee?"
    lee panic "...?"
    player "Maybe you should sit this one out. Dr. Helco and I can handle this."
    lee panic "Yeah... Maybe..."
    n "You guide Dr. Lee back into the lounge and help them sit onto one of the chairs."
    n "You'll miss the glow, but their health comes first and foremost."
    show lee panic at disappear
    n "You turn to leave the lounge and-"
    hide lee
    with hpunch
    n "...walk into a wall. This joke's getting a little old."
    n "You stumble your way back to Dr. Helco, who was patiently waiting for you."
    helco "It seems the anomaly is this way. Let's go."
    n "You follow the sounds of Dr. Helco's footsteps as he speedwalks down the hallway."
    helco "You see, the anomaly needs to draw in electricity to survive. Therefore, we can lure it towards us by standing nearby with electronic devices."
    helco "Once it gets close enough, we can cause a short-circuit by throwing a device at it, after which we quickly apprehend and contain it."
    player "How do you know so much about this anomaly?"
    helco "Not important. This way!"
    n "You begin to hear the buzzing of electricity. The noise only grows stronger as you continue down the various hallways."
    n "Dr. Helco stops you outside what you assume to be a room. The buzzing is almost deafening."
    helco "In this room. Wait here."
    n "You hear the sound of a door opening and closing."
    n "..."
    n "You hear a distant thud from within the room."
    n "..."
    n "Huh. The buzzing seems to be growing even louder."
    n "You turn around-"
    show yellow_screen:
        alpha 0.0
        linear 0.05 alpha 1.0
        linear 1.0 alpha 0.0
        
    n "...and see a surge of electricity in the wall behind you."
    "???" "{sc}{color=#ffff77}Bzzt! Bzzt!{/color}{/sc}"
    
    n "You see yellow and blue sparks surround a figure. It's too dark to make out, but that's not exactly important."
    show screen qte(time = 5.0, act=Jump("itd_timeout"))
    menu:
        n "You should do something. Fast. Like right now."
        "Run into the room Dr. Helco was in.":
            hide screen qte
            jump itd_room
        "Run away.":
            hide screen qte
            jump itd_run_away
        "Charge at the anomaly.":
            hide screen qte
            jump itd_charge
    
    label itd_room:
        n "You fumble desperately for the handle of the door behind you. The moment you find it, you wrench the door open and shut yourself inside."
        helco "Oh, hello [player_name]! What's-"
        player "That electric anomaly thing is outside and like holy hell I almost DIED I didn't know what else to do so I came into this room help me Dr. Helco help me please I just want to go home"
        helco "Ah! So the anomaly is outside. Stay here, I will be quick."
        n "You once again hear the door open and close."
        n "You feel a wave of relief wash over you..."
        show yellow_screen:
            shock
        n "...Or was that fear? Probably fear. You feel a wave of fear wash over you."
        n "You quickly exit the room."
        player "Dr. Helco?"
        helco "Odd... it's not being attracted. Oh, hello!"
        player "What are you trying to do?"
        helco "I'm doing as I said before: throwing devices at it. Oddly enough, however, these telephones don't seem to attract it. Could you take a look?"
        n "You feel Dr. Helco place something in your hands. You turn it around in your palms and realize."
        player "Dr. Helco, this is a phone {i}case{/i}."
        helco "..."
        player "..."
        helco "...Ah!"
        player "Have you just been throwing phone cases at the anomaly? Where did you even get this many cases?"
        helco "Nevermind that! Behind you!"
        show yellow_screen:
            shock
        n "The anomaly phases through the wall behind you. You scamper backwards to keep it far away."
        n "You remember Dr. Helco's lecture and realize what you need to do."

        $ itd_times_run_away = 0
        $ itd_times_thrown_wallet = 0
        label itd_final_choice:
            menu:
                n "Do it."
                "Run away.":
                    if itd_times_run_away == 0:
                        n "What? No!"
                    elif itd_times_run_away == 1:
                        n "Nope."
                    elif itd_times_run_away == 2:
                        n "Nuh uh!"
                    elif itd_times_run_away == 3:
                        n "Not happening."
                    elif itd_times_run_away == 4:
                        n "No."
                    else:
                        n "STAND YOUR GROUND!"
                    $ itd_times_run_away += 1
                    jump itd_final_choice
                    
                "Throw your wallet.":
                    if itd_times_thrown_wallet == 0:
                        n "You throw your wallet at the anomaly."
                        n "..."
                        n "You are now $16 poorer."
                    elif itd_times_thrown_wallet == 1:
                        n "You already did that."
                    elif itd_times_thrown_wallet == 2:
                        n "Hmm, where did your wallet go? I wonder!"
                    elif itd_times_thrown_wallet == 3:
                        n "You rummage your pockets and find..."
                        n "...a backup wallet??"
                    elif itd_times_thrown_wallet == 4:
                        n "You throw your backup wallet at the anomaly."
                        n "Again, nothing happens."
                    elif itd_times_thrown_wallet == 5:
                        n "You're not finding a {i}backup{/i} backup wallet."
                    elif itd_times_thrown_wallet == 6:
                        n "..."
                        n "Regrettably, you find a backup backup wallet."
                    elif itd_times_thrown_wallet == 7:
                        n "You throw your backup backup wallet at the anomaly."
                        n "..."
                        n "It did nothing. Good work, soldier!"
                    elif itd_times_thrown_wallet % 2 == 0:
                        n "You're fresh out of wallets."
                    else:
                        n "Three wallets is deranged enough."
                    
                    $ itd_times_thrown_wallet += 1
                    jump itd_final_choice
                
                "Throw your phone.":
                    n "You hurl your phone at the anomaly."
                    n "Your phone gets caught in what appears to be the center of the anomaly. You feel the sting of electricity in the air intensify."
                    n "After releasing a torrent of sparks..."
                    show yellow_screen:
                        shock
                    n "...it explodes."
                    show bg hallway
                    show helco at center
                    show black_screen:
                        alpha 0.0
                        0.1
                        alpha 1.0
                        0.2
                        alpha 0.0
                    
                    helco "Excellent! You did it!"
                    $ update_character_points({"helco": 1})
                    jump itd_conclusion

    label itd_run_away:
        n "You turn on your heel and sprint down the hallway. It doesn't matter that you can't see where you're going. You just need to get away."
        n "You brave a glance behind your and see the figure hot on your tail. Uh oh."
        n "This would be a terribly unfortunate time to run into a wall."
        n "Nah, kidding. That joke's old."
        n "You miraculously manage your way through the winding hallways without hurling yourself into a wall. Another glance behind informs you that the anomaly has seemingly stopped chasing you."
        n "You don't know where it went, but you decide not to take any chances. You find the nearest room and lock yourself in."
        n "With nothing else to do, you decide to wait."
        n "..."
        with default_fade
        n "You don't know how long it's been. It's definitely been at least a few hours."
        n "However, you're too scared to leave the room, so you decide to stay put."
        n "Just a bit longer."
        scene bg some room
        show black_screen
        with default_fade
        n "After what seems like an eternity..."
        show black_screen:
            alpha 0.0
            0.1
            alpha 1.0
            0.2
            alpha 0.0
        n "...the lights finally flicker back on."
        n "You cautiously open the door and peek outside. No threats detected."
        show bg hallway
        n "You make your way down the hall, back towards where you heartlessly abandoned Dr. Helco."
        show helco 
        helco "Oh, hello!"
        jump itd_conclusion

    label itd_conclusion:
        n "With the lights on, you can now clearly see the anomaly's figure lying on the floor. It's a " # guys what does it appear to be
        player "We should contain it before it gets up again."
        n "You don't even get to finish your sentence before Dr. Helco starts " # guys what does he do to capture the anomaly
        n "He seems remarkably skilled at this..."
        show bg containment room
        show helco happy
        with default_fade
        n "With the anomaly now securely contained, you silently applaud yourself for a job well done."
        show helco happy at disappear
        n "However, you still need to deal with the elephant in the room."
        hide helco
        menu:
            n "...Or do you?"
            "Ask Dr. Helco about the anomaly.":
                n "You muster up the courage to ask the question you've been meaning to ask."
                n "But it looks like he's already left. Damn."
            "Keep silent.":
                n "You decide it's not worth it. You leave Dr. Helco alone."
                n "Either way, it seems like he's already left."
        n "Slightly disappointed, you begin your way to the financial department to see if they can reimburse you for your phone." # insert better cooler funnier awesomer joke here
        if itd_times_thrown_wallet > 0:
            n "And your wallet."
        return
    
    label itd_charge:
        n "What in the world are you do- {nw}"
        show yellow_screen:
            shock
        jump itd_hospital

    label itd_timeout:
        n "Now's really not the time for hesitat- {nw}"
        show yellow_screen:
            shock
        jump itd_hospital
        
    label itd_hospital:
        scene bg hospital
        with default_fade
        n "You wake up to the blinding lights on the hopsital ceiling."
        helco "Are you alright, [player_name]?"
        player "Apart from a few minor burns and scratches, I actually feel fine."
        helco "Wonderful news!"
        player "What happened to the anomaly!"
        helco happy "Oh, I already contained it. There is no need to worry. I can assure you it will not be breaking out again."
        n "He stares at you slightly ominously. You probably shouldn't press further."
        n "However, it seems your lack of survival instincts has become clear to Dr. Helco. You should probably review those decision making skills some time."
        $ update_character_points({"helco": -1})
        return