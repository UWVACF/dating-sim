label day_event_lamp:
    image soundwave = At("images/day events/soundwave overlay.png", base_overlay_transform)

    scene bg cubicle
    n "You return to your desk after a small walk."
    n "Time to get back to work!"
    n "You notice a new addition to your cubicle. A tall lamp stands in the corner of your already cramped space."
    n "Must be part of the new ergonomic assessment. It's just a bit too clunky for your liking."
    n "Still, it's better than nothing."
    n "You plug its cord into the outlet, then turn the switch on."
    
    show black_screen onlayer top
    with default_fade
    show black_screen as black_bg
    hide black_screen onlayer top
    show black_screen as black_between zorder 3:
        alpha 0.0
        block:
            linear 2 alpha 0.8
            linear 2 alpha 0.5
            repeat

    n "Huh. Why are even the office lights out?"
    n "You click on the switch again. But you can't feel the switch."
    n "In fact, you can't even {i}feel{/i} your fingers. Or your arm. Or yourself. Or anything."
    player "   "
    player "   "
    n "You can't even hear your own voice. This is kind of bad, isn't it?"
    n "But you can hear me! Your friendly narrator! Yes, I am self aware."
    n "You have a meeting in 20 minutes and you haven't finished preparing for it. You really can't afford to be stuck in perpetual darkness."
    n "Actually, how long has it been? You can't even count your own heartbeat to detemine this."
    n "Just as you're about to start panicking, you make out a faint...image of someone."
    show layer master:
        blur 30
    show alex pensive
    n "Is that...Founder Alex?"
    n "Oh right. You have a meeting with the Founder."
    alex "{color=#8eabbf}{size=-10}Hm. Is [player_name] not here?{/size}{/color}"
    player "    "
    n "Oh right. You don't have any vocal cords anymore."
    alex "{color=#8eabbf}{size=-10}Oh. He left his phone here. Thats odd.{/size}{/color}"
    alex "{color=#8eabbf}{size=-10}More break time for me!{/size}{/color}"
    show alex pensive at disappear
    n "Oh. He's gone."
    n "Well, at least you don't have to worry about the meeting."
    hide alex
    with default_fade
    n "You don't know how long it's been. An hour? A day? A week?"
    n "Time seems to have stopped in the eternal darkness."
    n "You try to recall the emergency protocol trainings you did during onboarding for anomalous situations."
    n "1. Distance yourself from the anomaly. Can't really do that."
    n "2. Seek help from the Wal security team. Can't really do that."
    n "3. Report to respective supervisor. You don't really know what department this falls under."
    n "4. ...What was it again?"
    n "Just as you try to scrape your brain for step 4, another...image come into existance."
    show firewal pensive
    venture_unknown "{color=#8eabbf}{size=-10}This is all we found at [player_pos_adj] cubicle.{/size}{/color}"
    wal1 "{color=#8eabbf}{size=-10}I see. That should rule out murder by robbery, since their device is here.{/size}{/color}"
    n "It's a Wal! The security team! You're saved!"
    wal1 "{color=#8eabbf}{size=-5}Hm. The device seems normal.{/size}{/color}"
    wal1 "{color=#8eabbf}{size=-5}We'll put it in the evidence archive, then.{/size}{/color}"
    n "Wait no! You can feel Wal No.1's image getting more distant. You have a feeling you will actually be stuck here {i}forever{/i} if Manager Wal puts you away."

    $ yelling_attempts = 0
    $ shake_strength = 0
    $ soundwaver_ol_alpha = 0
    label yell_loop:
        if yelling_attempts < 3:
            menu:
                "Yell for help"(on_hover = "    "):
                    jump yelling_loop
                "Yell for help"(on_hover = "    "):
                    jump yelling_loop
                "Yell for help"(on_hover = "    "):
                    jump yelling_loop
                "Yell for help"(on_hover = "    "):
                    jump yelling_loop

        elif yelling_attempts >= 3:
            menu:
                "Yell for help"(on_hover = "I'M HERE!!!"):
                    jump end_yell_loop
                "Yell for help"(on_hover = "I'M HERE!!!"):
                    jump end_yell_loop
                "Yell for help"(on_hover = "I'M HERE!!!"):
                    jump end_yell_loop
                "Yell for help"(on_hover = "I'M HERE!!!"):
                    jump end_yell_loop 
        else:
            jump end_yell_loop

    label yelling_loop:
        $ yelling_attempts +=1
        $ shake_strength = yelling_attempts * 3
        $ soundwaver_ol_alpha = yelling_attempts/10
        show soundwave onlayer top:
            alpha soundwaver_ol_alpha
        show layer master:
            blur 30
            shake(strength = shake_strength)
            repeat
        jump yell_loop 

    label end_yell_loop:
        show layer master:
            blur 30
        hide soundwave onlayer top
        n "{i}buzz buzz!{/i}"
        wal1 "{color=#8eabbf}Huh?{/color}"
        wal1 "{sc}I'm here{/sc} {color=#8eabbf}...sender: [player_name]?{/color}"
        wal1 "{color=#8eabbf}Is this a prank?{/color}"
        menu:
            "Continue reaching for Manager Wal"(on_hover = "NO IT'S NOT! I'M STUCK IN THE PHONE!"):
                jump im_stuck_in_the_phone

    label im_stuck_in_the_phone:
        wal1 surprise "{color=#8eabbf}Stuck...in the device?{/color}"
        wal1 "{color=#8eabbf}That would explain [player_pos_adj]- your disappearance.{/color}"
        wal1 pensive "{color=#8eabbf}It seems this is an anomalous incident. I shall have the wals search the archive for any realated records.{/color}"
        wal1 happy "{color=#8eabbf}Fear not, we will rescue you, [player_name].{/color}"
        n "You let out a sigh of relief. Or at least, try to."
        menu:
            "How long have I been missing?":
                jump how_long_have_i_been_missing

    label how_long_have_i_been_missing:
        wal1 neutral "{color=#8eabbf}Three days, I believe.{/color}"
        wal1 "{color=#8eabbf}You did not show up to the meeting with Founder Alex. But that was not reported until the next day, when HR noticed your absence during the morning headcount.{/color}"
        n "Uh Oh. That would be...2 presentations, 6 meetings, 10 cups of coffee that you missed?"
        n "To be honest, those presentations and meetings probably happened fine without you. You're just an insignificant intern, after all."
        n "You're more worried at whether your body can function without caffine for so long once you are out of here."
        menu:
            "How can I get out of here?":
                jump how_can_I_get_out_of_here

    label how_can_I_get_out_of_here:
        wal1 "{color=#8eabbf}We are currently working on that. Wals have been deployed to go through all the files in our anomaly archive to look for the anomaly responsible for this incident.{/color}"
        wal1 happy "{color=#8eabbf}Estimated time of completion: {i}226 days, 15 hours, 29 minutes, and 12 seconds.{/i}{/color}"
        n "226 days? Your internship will be over by then!"
        wal1 "{color=#8eabbf}{i}226 days, 15 hours, 29 minutes, and 5 seconds{/i} now.{/color}"
        venture_unknown "{color=#8eabbf}Perhaps I can offer some assistant.{/color}"
        n "You can feel another figure approach."
        show firewal neutral at move_to (x_align = 0.85)
        show venture happy at appear (x_align = 0.15)
        venture "{color=#8eabbf}Hello, [player_name].{/color}"
        wal1 upset "{color=#8eabbf}We appreciate your willingness to contribute, Dr. Venture. However, this is the purpose of 81928 wals.{/color}"

        if "fire" in seen_events:
            if put_wals_out_of_a_job == True:
                wal1 fury "{color=#8eabbf}[player_name] has already put 118072 wals out of a job recently. It would be greatly devastating if more suffer from unemployment. The poverty rates of wals will increase to 822%, while the homeless rates will be increased by-{/color}"
            else:
                wal1 panic "{color=#8eabbf}It would be greatly devastating if they are put out of unemployment. The poverty rates of wals will increase by 822\%, while the homeless rates will be increased by-{/color}"
        else:
            wal1 panic "{color=#8eabbf}It would be greatly devastating if they are put out of unemployment. The poverty rates of wals will increase to 822\%, while the homeless rates will be increased by-{/color}"
        
        venture surprise "{color=#8eabbf}Woah there. I don't plan on stealing jobs from the wals. I have simply taken an interest in this incident as it seems to relate to my field of research.{/color}"
        show firewal at move_to (x_align = 1.2)
        show venture neutral at move_to (x_align = 0.5)
        n "You feel Dr. Venture grab your conciousness from Manager Wal's hand."
        n "You feel as if someone is tapping on you. Words appear in your head."
        n "{b}Can you see this, [player_name]?{/b}"
        n "{b}This is Dr. Wayne \:\) \nI'm here to offer you...a better solution than waiting for a year in your phone!{/b}"
        n "{b}Do you remember how you got stuck in here?{/b}"
        menu:
            "You turned on a lamp.":
                jump lamp_lamp
        
        label lamp_lamp:
            n "{b}That's right! \nThe lamp that I misplaced at your cubicle.{/b}"
            menu:
                "So it was you?":
                    jump so_it_was_you

        label so_it_was_you:
            n "Dr. Venture pauses."
            n "{b}Anyways, I can get you out of there through Alchemical means. However, it does mean putting wals out of a job. So, what do you say?{/b}"
            wal1 upset "{color=#8eabbf}Dr. Venture, you are tampering with important evidential items! Please return it!{/color}"
            menu:
                "What do you need me to do?":
                    jump what_do_i_do

        label what_do_i_do:
            n "{b}It's simple! I can transmutate you from the device out into the real world again. But it requires some sacrifices, as alchemy abide by the rules of equivalent exchange.{/b}"
            n "{b}So I'll need you to tell me something that has the same value as your physical being. It can be anything - a physical item, a body part, or even your future.{/b}"
            wal1 upset "{color=#8eabbf}This is the last warning! Wal security will be called in 5...4...3...{/color}"
            n "{b}Quick! The wals are closing in! It can be anything!{/b}"
            menu:
                "Sacrifice an arm":
                    jump lamp_arm
                "Sacrifice a walbot":
                    jump lamp_walbot
                "Sacrifice your future":
                    jump lamp_future
                "Sacrfice something else that I haven't come up with yet":
                    jump lamp_last

            label lamp_arm:
                n "uhhhhhhhh"

        n "{color=#8eabbf}oof{/color}"
        
                
            






