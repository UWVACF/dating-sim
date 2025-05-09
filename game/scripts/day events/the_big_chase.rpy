label day_event_the_big_chase:
    scene hallway
    with default_fade
    n "You are on your way back from the restroom when you hear commotion from behind you. {w=0.5} You turn around to see a blue hampster sprinting down the hallway towards you." 
    n "Behind Hampter, a dark sphere with four legs closely follows it, its large mouth threatening to inhale Hampter."
    n "Behind the creature, two more pairs of legs run after the them, albeit with less elegance and slower speed."
    show hampter panic
    hampter "Help me!"
    # render in graphic of hampter(?) and pochi
    hide hampter

    menu: 
        n "What should you do?"
        "Help Hampter by scooping them up with your hands.":
            jump help_hampter
        "Remind Hampter that they can teleport, but stay well out of the way. You've seen what happened last time when Kacy tried to pet Hampter.":
            jump hamp_tele
        "Do nothing. According to the foundation employee guidelines, level 5 clearance personnels should not involve themselves in anomalies incidents.":
            jump ignore_hampter

    label help_hampter:
        n "You pick up Hampter without hesitation just as they reach you. {w=5} Thankfully, your hands remain intact, unlike Kacy's arm."
        n "Pochi growls at you and starts biting your ankles. Its bite hurts a lot as expected."
        # un-render graphic, so just back to the hallway
        n "The two figures with lab coats finally catch up close enough for you to identify them. It's Dr Chan and Dr Syg."
        show chan panic at appear(x_align = 0.33)
        show syg neutral at appear(x_align = 0.66)
        chan "Finally caught up...please hand me Pochi...it ate my hard drave."
        syg "I would like Pochi instead. I have been trying to catch it to sample it for my research."

        menu:
            n "Who do you hand Pochi to? (Pochi is still nibbling at your ankles.)"
            "Dr Chan needs his hard drive back.":
                jump chan_hard_drive
            "Dr Syg needs it for science.":
                jump syg_experiment

        label chan_hard_drive:
            player "For sure, Dr Chan!"
            n "You swing your leg in Dr Chan's direction and Pochi is set free your ankle, slamming into the ceiling halfway between you and Dr Chan. It squeaks alike a tub duck."
            chan "..."
            player "Sorry. The last time I did sports was in grade 9."
            n "Just as Dr Chan makes his way towards his hard drive, you see a mushroom pops up around the corner."
            n "Pochi must have seen it too, because it drops down from the ceiling suddenly and sprints towards it"
            show plutoes at appear(x_align = 0.5)
            n "Plutoes picks up Pochi, flashes everyone his enigmatic smile and leaves."
            hide plutoes
            chan upset "My hard drive..."
            syg neutral "..."
            chan neutral "Thank you for your...attempt to help. I will be on my way now."
            hide syg
            hide chan
            $ update_character_points({"chan": 1})
            $ update_character_points({"syg": -1})
            jump help_hampter_con
        
        label syg_experiment:
            player "Okay, Dr Syg."
            n "Dr Syg doesn't actually require you help, seeing how he has now outrun Dr Chan and has almost reached you."
            hide chan
            n "You decide to prove your worth by kicking Pochi off your leg towards Dr Syg."
            show plutoes at appear(x_align = 0.5)
            n "Pochi's trajectory was stopped as it was caught mid-air by Plutoes, who appeared out of seemly nowhere."
            n "He towers over you and takes out a red sharpie."
            plutoes "{cps=*0.75}{b}{color=#ff2d00}Thank you for finding my dog :) \n {i} -Signed Plutoes {/i}{/color}{/b}{/cps}"
            hide plutoes
            n "Plutoes tosses his marker aside and leaves with Pochi."
            syg "...I'll get it next time."
            n "Dr Syg gives you a nod before turning to leave."
            $ update_character_points({"syg": 1})
            $ update_character_points({"chan": -1})
            jump help_hampter_con

        label help_hampter_con:
            hampter happy "Thank you for helping me!"
            n "Hampter nuzzles against your palm before teleporting away."
            hide hampter
            n "...Why didn't they just teleport away from Pochi just now?"
            $ update_character_points({"hampter": 1})
            return

    label hamp_tele:
        player "Teleport, Hampter!"
        hampter surprise "!!!"
        n "You watch as Hampter disappears into thin air."
        n "Pochi stops running and stands in front of you. It doesn't have eyes, but you feel as if it is staring daggers at you."
        n "The sounds of footsteps draw closer and you can see who it is. It's Dr Chan and Plutoes."
        n "Pochi growls and teleports away, perhaps to go after Hampter, or to escape its chasers."
        show syg at appear(x_align = 0.33)
        show chan at appear(x_align = 0.66)
        n "Dr Chan stops in front of you and looks around bewilderedly. {w=0.7} Out of the corner of your eye, you see Pochi reappears behind Plutoes, who has purposely stopped a few steps behind Dr Chan."
        chan fury "Hey [player_name], did you see where Pochi went? That damn thing ate my hard drive."
        n "You see Plutoes takes out a huge white notepad and begins writing on it with his red sharpie."
        plutoes "{cps=*0.75}{b}{color=#ff2d00}Don't tell him :){/color}{/b}{/cps}"
        
        menu:
            n "Should you cover for Pochi?"
            "You're sure Pochi means no harm. And Dr Chan seems to be overreacting a bit.":
                jump chan_lie
            "No, this is a professional environment with no rooms for mischief.":
                jump expose_plutoes
            
        label chan_lie:
            player "I'm not sure, it teleported away to chase Hampter."
            #render ethy graphic at 0.5 transparancy
            show chan pensive
            chan unique "{size=+5}{b}AAAAAAA??????{/size} {w=0.7}{size=+3} A. {/size}{w=0.7} AA.{/b}"
            n "You hear confused screaming in your head. Chan must be hearing it too, because he stares at you suspeciously."
            player "Or maybe he wasn't going after Hampter?"
            n "The screaming stops."
            hide plutoes
            chan "Hm. It's alright, I've attached a tracker to my hard drive."
            n "You see Dr Chan takes out his device, then swiftly turns around. Only then you both realize that Plutoes is no longer there."
            chan fury "Dammit. Plutoes."
            hide chan
            $ update_character_points({"plutoes": 1})
            $ update_character_points({"chan": -1})
            return

        label expose_plutoes:
            player "It's behind Plutoes!"
            show plutoes upset
            #render green smog/spore/gas/whatever the heck plutoes releases across the screen
            hide plutoes
            n "Suddenly, you and Dr Chan were hit with a wave of green stuff in the air."
            chan panic "{i}cough cough cough{/i}"
            #^ chan and player if possible?
            chan "{i}cough- {/i}What was that?!"
            n "Unsurprisingly, Plutoes and Pochi are gone."
            chan fury "Why is this happening to me."
            chan unique "{size=+3}{b}AAA.{/b}{/size}"
            hide chan
            n "You watch as Dr Chan trudges away. At this point it might be easier for him to just rewrite whatever is in that hard drive."
            n "You turn around to contine on your way, only to see your disorted reflection on a glass door. {w=0.7}Someone has left a disapproving message in red sharpie on your face of {cps=*0.75}{b}{color=#ff2d00}:({/color}{/b}{/cps}"
            n "You debate whether to report this as workplace harassment."
            $ update_character_points({"chan": 1})
            return

    label ignore_hampter:
        n "You watch as Hampter gets sucked into the black hole. The full beast burps in satisfaction. Did you just witness murder?"
        n "The two people in lab coats get closer and you can make out that they are Dr Syg and Plutoes. What an odd combination."
        n "Pochi ducks behind you like a toodler playing hide and seek."
        show plutoes happy at appear(x_align = 0.33)
        show syg neutral at appear(x_align = 0.66)
        syg "Please grab Pochi for me, [player_name]. I need to recover Hampter, they are supposed to overlook my department temporarily."
        plutoes "{i}scribbles on floor{/i} {cps=*0.75}{b}{color=#ff2d00}Don't grab my dog :( I told him to kidnap Hampter, to free them from dangerous work at the Demonic department.{/color}{/b}{/cps}"

        menu:
            n "Who should you listen to?"
            "Grab Pochi - right your previous wrong of not helping poor Hampter.":
                jump grab_pochi
            "Do not grab Pochi. This cross-department conflict is out of your pay range.":
                jump spear_pochi
            
        label grab_pochi:
            n "You grab the struggling Pochi from behind you. It wags its tail to try to hit you, but you athletically dodges its attempts and quickly hands it to Dr Syg."
            show plutoes upset
            n "Just as Dr Syg touches Pochi, it teleports away, leaving behind a soaking, miserable Hampter in Dr Syg's palm."
            show hampter sad at appear(x_align = 0.5)
            plutoes "{i}scribbles on wall{/i} {cps=*0.75}{b}{color=#ff2d00} [player_name] is a hairy loser. {i}-signed [player_name] {/i}{/color}{/b}{/cps}"
            n "Plutoes leaves. You hope Dr Syg would vouch for you when the janitors report vandalism."
            hide plutoes
            syg pensive "Too bad I couldn't take its tail to sample..."
            hide hampter
            hide syg
            n "You watch Dr Syg walk away with a drained Hampter. You silently pray for Hampter's work at the Demonic department to go easy them and not add to their exhaustion."
            $ update_character_points({"syg": 1})
            return

        label spear_pochi:
            n "You do not do anything. Hold on, Dr Syg's level is technically above Plutoes'. Would this get you in trouble?"
            syg upset "I will have to report this as an incident if we don't recover Hampter."
            plutoes happy "{i}scribbles on his coat{/i} {cps=*0.75}{b}{color=#ff2d00} And I will give you a {i}clean {/i}haircut if you do grab Pochi.{/color}{/b}{/cps}"
            n "Okay, you are in trouble either way. It's so hard being an intern."
            n 'Just as you are about to drop to your knees and beg for forgiveness, Pochi teleports away with a loud "POP!". Perhaps it does have a tiny bit of sympathy in its non-existent heart.'
            syg "Hmph."
            hide syg
            n "Plutoes walks over to you and pats you on your shoulder in approval before leaving."
            hide plutoes
            n "You feel a small itch on your shoulder. A very colorful mushroom is planted. You better get it checked out and removed at the bio-hazard infirmary."
            $ update_character_points({"syg": -1})
            $ update_character_points({"plutoes": 1})
            return







