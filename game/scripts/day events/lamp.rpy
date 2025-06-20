label day_event_lamp:
    image soundwave = At("images/day events/soundwave overlay.png", base_overlay_transform)
    image flashbang = "images/day events/white screen.png"
    $ lamp_moneyy = False
    $ lamp_memoriess = False

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
    show black_screen as black_between zorder 50:
        alpha 0.0
        block:
            linear 2 alpha 0.8
            linear 2 alpha 0.5
            repeat

    n "Huh. Why did the office lights go out?"
    n "You click on the switch again. But you can't feel the switch."
    n "In fact, you can't even {i}feel{/i} your fingers. Or your arm. Or yourself. Or anything."
    player "   "
    player "   "
    n "You can't even hear your own voice. This is kind of bad, isn't it?"
    n "But you can hear me! Your friendly narrator! Yes, I am self aware."
    n "You have a meeting in 20 minutes and you haven't finished preparing for it. You really can't afford to be stuck in perpetual darkness."
    n "Actually, how long has it been? You can't even count your own heartbeats to determine this."
    n "Just as you're about to start panicking, you make out a faint...image of someone."
    show layer master:
        blur 10
    show alex pensive
    n "Is that...Founder Alex?"
    n "Oh right. You have a meeting with the Founder."
    alex "{color=#8eabbf}{size=-10}Hm. Is [player_name] not here?{/size}{/color}"
    player "    "
    n "Oh, yeah. You don't have any vocal cords anymore."
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
    wal1 "{color=#8eabbf}{size=-10}I see. That should rule out murder for robbery, since their device is here.{/size}{/color}"
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
            blur 10
            shake(strength = shake_strength)
            repeat
        jump yell_loop 

    label end_yell_loop:
        show layer master:
            blur 10
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
        wal1 pensive "{color=#8eabbf}It seems this is an anomalous incident. I shall have the wals search the archive for any related records.{/color}"
        wal1 happy "{color=#8eabbf}Fear not, we'll rescue you, [player_name].{/color}"
        n "You let out a sigh of relief. Or at least, try to."
        menu:
            "How long have I been missing?":
                jump how_long_have_i_been_missing

    label how_long_have_i_been_missing:
        wal1 neutral "{color=#8eabbf}Three days, I believe.{/color}"
        wal1 "{color=#8eabbf}You didn't show up to the meeting with Founder Alex. But that wasn't reported until the next day, when HR noticed your absence during the morning headcount.{/color}"
        n "Uh oh. That'd be...2 presentations, 6 meetings, 10 cups of coffee that you missed?"
        n "To be honest, those presentations and meetings probably happened fine without you. You're just an insignificant intern, after all."
        n "You're more worried as to whether your body can function without caffiene for long once you're out of here."
        menu:
            "How can I get out of here?":
                jump how_can_I_get_out_of_here

    label how_can_I_get_out_of_here:
        wal1 "{color=#8eabbf}We're currently working on that. Wals have been deployed to go through all the files in our anomaly archive to look for the anomaly responsible for this incident.{/color}"
        wal1 happy "{color=#8eabbf}Estimated time of completion: {i}226 days, 15 hours, 29 minutes, and 12 seconds.{/i}{/color}"
        n "226 days? Your internship will be over by then!"
        wal1 "{color=#8eabbf}{i}226 days, 15 hours, 29 minutes, and 5 seconds{/i} now.{/color}"
        venture_unknown "{color=#8eabbf}Perhaps I can offer some assistance.{/color}"
        n "You can feel another figure approach."
        show firewal neutral at move_to (x_align = 0.85)
        show venture happy at appear (x_align = 0.15)
        venture "{color=#8eabbf}Hello, [player_name].{/color}"
        wal1 upset "{color=#8eabbf}We appreciate your willingness to contribute, Dr. Venture. However, this is the purpose of 81928 wals.{/color}"

        if "fire" in seen_events:
            if put_wals_out_of_a_job == True:
                wal1 fury "{color=#8eabbf}[player_name] has already put 118072 wals out of a job recently. It'd be greatly devastating if more suffer from unemployment. The poverty rates of wals will increase to 822%, while the homeless rates will be increased by-{/color}"
            else:
                wal1 panic "{color=#8eabbf}It'd be greatly devastating if they're put out of unemployment. The poverty rates of wals will increase by 822\%, while the homeless rates will be increased by-{/color}"
        else:
            wal1 panic "{color=#8eabbf}It'd be greatly devastating if they're put out of unemployment. The poverty rates of wals will increase to 822\%, while the homeless rates will be increased by-{/color}"
        
        venture surprise "{color=#8eabbf}Woah there. I don't plan on stealing jobs from the wals. I've simply taken an interest in this incident as it seems to relate to my field of research.{/color}"
        show firewal at move_to (x_align = 1.2)
        show venture neutral at move_to (x_align = 0.5)
        n "You feel Dr. Venture grab your consciousness from Manager Wal's hand."
        n "You feel as if someone is tapping on you. Words appear in your head."
        n "{b}Can you see this, [player_name]?{/b}"
        n "{b}This is Dr. Wayne \:\) \nI'm here to offer you a...better solution than waiting for a year in your phone!{/b}"
        n "{b}Do you remember how you got stuck in here?{/b}"
        menu:
            "I turned on a lamp.":
                jump lamp_lamp
        
        label lamp_lamp:
            n "{b}That's right! \nThe lamp that I misplaced at your cubicle.{/b}"
            menu:
                "So it was you?":
                    jump so_it_was_you

        label so_it_was_you:
            n "Dr. Venture pauses."
            n "{b}Well techically, it wasn't misplaced. More of a prank.{/b}"
            menu:
                "EXCUSE ME? WHAT THE FU-":
                    jump lamp_what_the

        label lamp_what_the:
            n "{b}Anyways, I can get you out of there through Alchemical means. However, it does mean putting wals out of a job. So, what do you say?{/b}"
            wal1 upset "{color=#8eabbf}Dr. Venture, you're tampering with important evidential items! Please return it!{/color}"
            menu:
                "What do you need me to do?":
                    jump what_do_i_do

        label what_do_i_do:
            n "{b}It's simple! I can transmutate you from the device out into the real world again. But it requires some sacrifices, as alchemy abides by the rules of equivalent exchange.{/b}"
            n "{b}So I'll need you to tell me something that has the same value as your physical being. It can be anything - an item, a body part, or even intangible things.{/b}"
            wal1 upset "{color=#8eabbf}This is the last warning! Wal security will be called in 5...4...3...{/color}"
            n "{b}Quick! The wals are closing in! It can be anything!{/b}"
            show firewal at disappear
            jump lamp_sacrifice

        label lamp_sacrifice:
            menu:
                "Sacrifice"(on_hover = "a kidney"): 
                    jump lamp_kidney
                "Sacrfice"(on_hover = "your entire fortune"): ########fail
                    jump lamp_money
                "Sacrifice"(on_hover = "your memories"): ########fail
                    jump lamp_memories
                "Sacrifice"(on_hover = "a walbot"):  #wal -1
                    jump lamp_walbot

            label lamp_kidney:
                n "You have no idea why, but your kidney is the first thing that comes to mind."
                n "{b}Got it! I'll get you out in a second!{/b}"
                show venture at disappear
                n "The image of Dr. Venture fades away. You're once again left in the dark."
                n "Did the wal bots get him? Or is he beginning the transmutation?"
                show flashbang onlayer top:
                    alpha 0.0
                    easeout 0.4 alpha 1.0
                scene bg lab 
                hide firewal
                show flashbang onlayer top:
                    alpha 1.0
                    easein 0.4 alpha 0.0
                show venture happy at appear(x_align = 0.5)
                n "Suddenly, you can see light again."
                n "You awaken lying in a transmutation circle, your hand tightly clutching your phone."
                venture "Told you I could get you out!"
                n "You are about to thank Dr. Venture when you feel a sharp pain on your right below your rib cage."
                n "You fall over and roll on the ground in agony."
                venture neutral "Ah. That must be the kidney."
                venture "Sorry, I'm not exactly a qualified doctor. But don't worry, the laws of alchemy dictate that you won't die!"
                player "You misunderstood, Dr. Venture."
                player "This pain...it's bearable."
                n "Dr. Venture looks at you with concern."
                n "You appreciate his concern, but you know that he doesn't understand the pain of losing a kidney."
                n "You could've sold that organ yourself for 100k."
                n "But now it's just gone, taken by the void."
                n "Hold on, you recall Dr. Venture mention something about misplacing a lamp."
                n "Your despair turns into fury, and you feel light-headed, either from the anger or the blood you lost."
                player "Dr. Ven-"
                show firewal at appear(x_align = 0.25)
                show venture at move_to(x_align = 0.85)
                show venture surprise
                wal1 upset "DR. VENTURE."
                wal1 "Please return the phone! It's very important in order for us to save [player]!"
                venture "Actually, I got [player] out."
                n "Manager Wal turns around and stares down at you, who's still on the floor in the fetus position."
                wal1 neutral "Oh."
                wal1 "I see then. Thank you for your aid."
                wal1 pensive "I shall go back to investigating the cause of this incident. Don't worry, for this won't happen again, as the anomaly has already been recontained-"
                show venture sad
                player "Dr. Venture did it."
                wal1 "?"
                player "He was the one who placed the lamp at my cubicle."
                venture "Now, [player], I can understand that you're still in shock-"
                player "I have evidence."
                n "You take out your phone, which contains all the messages between you and Dr. Venture while you were trapped in it."
                venture neutral "..."
                venture happy "Alright, you got me good."
                venture "I'll take care of all the incident report writing, Firewal."
                wal1 "Affirmative, since you're the party responsible. I'll also submit a report to the Founder about this."
                wal1 "[player], I'll need to borrow your device to present evidence. But it'll be returned shortly, since the investigation is over."
                show firewal at disappear
                n "Manager Wal exits, leaving you and Dr. Venture. Dr. Venture smiles at you."
                hide firewal
                venture "It was a lot of fun today."
                venture "A shame that you sabotaged my game."
                venture "But I'll just try something different next time."
                show venture at disappear:
                    xalign 0.85
                n "Next time?"
                n "You shudder to think about losing your other kidney. If it comes down to it, you might consider just staying in the void."
                $ update_character_points({"firewal": 1, "venture": -1})
                return

            label lamp_money:
                if lamp_moneyy == False:
                    n "Well, if you can't get out of here, you wouldn't really need money, would you?"
                    n "Might as well give that a try. You can always make it back. Afterall, the pay was the only reason you applied for this job."
                    n "{b}Got it! I'll get you out in a second!{/b}"
                    n "You wait."
                    n "To your dismay, you are still stuck in darkness after a {i}bit{/i} more than the second passed."
                    n "{b}Sorry [player], the transmutation failed. It seems that your entire fortune isn't valuable enough.{/b}"
                    n "Wow. Way to rub that in."
                    n "At least you get to keep your 28 bucks!"
                    n "If you get out of here, that is."
                    $ lamp_moneyy = True
                    jump lamp_sacrifice
                else:
                    n "You already tried that."
                    n "You're broke, okay? Now try something else."
                    jump lamp_sacrifice

            label lamp_memories:
                if lamp_memoriess == False:
                    n "{b}Got it! I'll get you out in a second!{/b}"
                    n "You reminisce one last time."
                    n "That really good instant ramen last week."
                    n "That good book with an insane plot twist you read a few months ago. Oh good, you can read it fresh again."
                    n "Those countless nights during university, staying up to rush assignments...to be fair, you already forgot everything you've learned."
                    n "You remember your childhood, all those time you embarassed youself in front of your kindergarden crush..."
                    n "...You have a remarkably good memory, I must say."
                    n "You feel peace, knowing that you'll no longer be huanted by some of these memories when you can't sleep at night."
                    n "..."
                    n "You can still explicitly remember it all. Why is it not working?"
                    venture pensive "Hey so uh...the transmutation failed."
                    venture "It seems that your memories aren't valuable enough to you."
                    n "Dang it."
                    $ lamp_memoriess = True
                    jump lamp_sacrifice
                else:
                    n "You already tried this."
                    n "If even you don't want some of these memories, why do you think the alchemy process would want them?"
                    jump lamp_sacrifice

            label lamp_walbot:
                n "Technically, Dr. Venture never specified that you must {i}own{/v} the subject of equivalent exchange."
                n "And the most valuable thing in the proximity right now is a walbot that is trying to grab the phone from Dr. Venture."
                n "Infused with the greatest AI technology, made from expensive and rare metals, and forged by the great Dr. Firewal. What could be more valuable than that??"
                show venture happy
                n "{b}Got it! I'll get you out in a second!{/b}"
                show firewal as sacrifice_wal:
                    alpha 0.0
                    alpha 1.0
                    appear(x_align = 1.3)
                    move_to(x_align = 0.7, duration = 1)
                n "A walbot comes into view, charging straight at Dr. Venture."
                show flashbang onlayer top:
                    alpha 0.0
                    easeout 0.4 alpha 1.0
                scene bg lab 
                hide firewal
                show flashbang onlayer top:
                    alpha 1.0
                    easein 0.4 alpha 0.0
                show venture happy at appear(x_align = 0.5)
                n "Suddenly, you can see light again."
                n "You lie in Dr. Venture's lab within a transmutation circle."
                n "You turn your head to see a walbot next to you. Or rather, what remains of a walbot - the signature golden arm that resembles the one its creator has."
                venture "Welcome back, [player_name]!"
                venture "I gotta say, that was an interesting choice for a transmutation material. Thanks to you, I got inspired for a new direction in my research."
                player "...Glad I could help."
                venture neutral "Anyways, you can keep that as a souvenir. I don't really need more gold."
                show venture at disappear
                n "You pick up the golden arm. It weighs down in your hand."
                n "It buzzes in retaliation. Following the source of the buzzing, you realize that its wrist cuff can still be activated."
                n "Curious, you click on it. A flashing red screen shines in your face."
                n "{b}{color=#eb4034}{size=+15}THE WAL{/size} \nHAS BEEN ALERTED OF THIS TRANSGRESSION{/color}{/b}"
                n "Well. It's your life or this bot's. You're sure Dr. Firewal would understand."
                n "...Right..?"
                $ update_character_points({"firewal": -1, "venture": 1})
                return

        
                
            






