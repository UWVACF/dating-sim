label day_event_the_big_chase:
    scene hallway
    with default_fade
    n "You are on your way back from the restroom when you hear commotion from behind you. {w=0.5} You turn around to see a blue hamster sprinting down the hallway towards you." 
    n "Behind Hampter, a dark sphere with four legs closely follows it, his large mouth threatening to inhale Hampter."
    n "Behind the creature, two more pairs of legs run after them, albeit with less elegance and slower speed."
    show hampter panic
    hampter "Help me!"
    # render in graphic of hampter(?) and pochi
    hide hampter

    menu: 
        n "What should you do?"
        "Help Hampter by scooping them up with your hands.":
            jump help_hampter
        "Remind Hampter that they can teleport, but stay well out of the way. You saw what happened last time when Kacy tried to pet Hampter.":
            jump hamp_tele
        "Do nothing. According to the foundation employee guidelines, level 5 clearance personnel should not involve themselves in anomaly incidents.":
            jump ignore_hampter

    label help_hampter:
        n "You pick up Hampter without hesitation just as they reach you. {w=5} Thankfully, your hands remain intact, unlike Kacy's arm."
        n "Pochi growls at you and starts biting your ankles. His bite hurts a lot, as expected."
        # un-render graphic, so just back to the hallway
        n "The two figures in lab coats finally catch up close enough for you to identify them. It is Dr. Chan and Dr. Syg."
        show chan panic at appear(x_align = 0.33)
        show syg neutral at appear(x_align = 0.66)
        chan "Finally caught up...please hand me Pochi...he ate my hard drive."
        syg "I would like Pochi instead. I've been trying to catch him to sample it for my research."

        menu:
            n "Who do you hand Pochi to? (Pochi is still nibbling at your ankles.)"
            "Dr. Chan needs his hard drive back.":
                jump chan_hard_drive
            "Dr. Syg needs it for science.":
                jump syg_experiment

        label chan_hard_drive:
            player "For sure, Dr. Chan!"
            n "You swing your leg in Dr. Chan's direction, flinging Pochi from your ankle, slamming into the ceiling halfway between you and Dr. Chan. He squeaks like a rubber duck."
            chan "..."
            player "Sorry. The last time I did sports was in grade nine."
            n "Just as Dr. Chan makes his way towards his hard drive, you see a mushroom pop up around the corner."
            n "Pochi must have seen it too, because he drops down from the ceiling suddenly and sprints towards it"
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
            player "Okay, Dr. Syg."
            n "Dr. Syg doesn't actually require your help, seeing how he has now outrun Dr. Chan."
            hide chan
            n "You decide to prove your worth by kicking Pochi off your leg towards Dr. Syg."
            show plutoes at appear(x_align = 0.5)
            n "Pochi's trajectory is stopped as it is caught mid-air by Plutoes, who appeared out of seemingly nowhere."
            n "He towers over you and takes out a red sharpie."
            plutoes "{cps=*0.75}{b}{color=#ff2d00}Thank you for finding my dog :) \n {i} -Signed Plutoes {/i}{/color}{/b}{/cps}"
            n "Plutoes tosses his marker aside and leaves with Pochi."
            hide plutoes
            syg "...I'll get it next time."
            n "Dr. Syg gives you a nod before turning to leave."
            $ update_character_points({"syg": 1})
            $ update_character_points({"chan": -1})
            jump help_hampter_con

        label help_hampter_con:
            hampter happy "Thank you for helping me!"
            n "Hampter nuzzles against your palm before teleporting away."
            hide hampter
            n "...Why didn't she just teleport away from Pochi just now?"
            $ update_character_points({"hampter": 1})
            return

    label hamp_tele:
        player "Teleport, Hampter!"
        hampter surprise "!!!"
        n "You watch as Hampter disappears into thin air."
        n "Pochi stops running and stands in front of you. He doesn't have eyes, but you feel as if he is staring daggers at you."
        n "The sound of footsteps draws closer and you can see who it is. It's Dr. Chan and Plutoes."
        n "Pochi growls and teleports away, perhaps to go after Hampter, or to escape his chasers."
        show syg at appear(x_align = 0.33)
        show chan at appear(x_align = 0.66)
        n "Dr. Chan stops in front of you and looks around bewilderedly. {w=0.7} Out of the corner of your eye, you see Pochi reappear behind Plutoes, who has purposely stopped a few steps behind Dr. Chan."
        chan fury "Hey [player_name], did you see where Pochi went? That damn thing ate my hard drive."
        n "You see Plutoes takes out a huge white notepad and begin writing on it with his red sharpie."
        plutoes "{cps=*0.75}{b}{color=#ff2d00}Don't tell him :){/color}{/b}{/cps}"
        
        menu:
            n "Should you cover for Pochi?"
            "You're sure Pochi means no harm. And Dr. Chan seems to be overreacting a bit.":
                jump chan_lie
            "No, this is a professional environment with no room for mischief.":
                jump expose_plutoes
            
        label chan_lie:
            player "I'm not sure, he teleported away to chase Hampter."
            #render ethy graphic at 0.5 alpha
            chan unique "{size=+5}{b}AAAAAAA??????{/size} {w=0.7}{size=+3} A. {/size}{w=0.7} AA.{/b}"
            n "You hear confused screaming in your head. Chan must be hearing it too, because he stares at you suspiciously."
            player "Or maybe he wasn't going after Hampter?"
            n "The screaming stops."
            hide plutoes
            chan "Hm. It's alright, I've attached a tracker to my hard drive."
            n "You see Dr. Chan takes out his device, then swiftly turns around. Only then you both realize that Plutoes is no longer there."
            chan fury "Dammit. Plutoes."
            hide chan
            $ update_character_points({"plutoes": 1})
            $ update_character_points({"chan": -1})
            return

        label expose_plutoes:
            player "He's behind Plutoes!"
            show plutoes upset
            #render green smog/spore/gas/whatever the heck plutoes releases across the screen
            hide plutoes
            n "Suddenly, you and Dr. Chan are hit with a wave of green stuff in the air."
            chan panic "{i}cough cough cough{/i}"
            #^ chan and player if possible?
            chan "{i}cough- {/i}What was that?!"
            n "Unsurprisingly, Plutoes and Pochi are gone."
            chan fury "Why is this happening to me?!"
            chan unique "{size=+3}{b}AAA.{/b}{/size}"
            hide chan
            n "You watch as Dr. Chan trudges away. At this point it might be easier for him to just rewrite whatever was in that hard drive."
            n "You turn around to continue on your way, only to see your distorted reflection on a glass door. {w=0.7}Someone has left a disapproving message in red sharpie on your face: {cps=*0.75}{b}{color=#ff2d00}:({/color}{/b}{/cps}"
            n "You debate whether to report this as workplace harassment."
            $ update_character_points({"chan": 1})
            return

    label ignore_hampter:
        n "You watch as Hampter gets sucked into the black hole. The full beast burps in satisfaction. Did you just witness murder?"
        n "The two people in lab coats get closer and you can make out that they are Dr. Syg and Plutoes. What an odd combination."
        n "Pochi ducks behind you like a toddler playing hide and seek."
        show plutoes happy at appear(x_align = 0.33)
        show syg neutral at appear(x_align = 0.66)
        syg "Please grab Pochi for me, [player_name]. I need to recover Hampter, they're supposed to oversee my department temporarily."
        plutoes "{i}scribbles on floor{/i} {cps=*0.75}{b}{color=#ff2d00}Don't grab my dog :( I told him to kidnap Hampter, to free her from the dangerous work in the Demonic department.{/color}{/b}{/cps}"

        menu:
            n "Who should you listen to?"
            "Grab Pochi. Right your previous wrong of not helping poor Hampter.":
                jump grab_pochi
            "Do not grab Pochi. This cross-department conflict is out of your pay range.":
                jump spare_pochi
            
        label grab_pochi:
            n "You grab the struggling Pochi from behind you. He wags his tail to try to hit you, but you athletically dodge his attempts and quickly hand he to Dr. Syg."
            show plutoes upset
            n "Just as Dr. Syg touches Pochi, he teleports away, leaving behind a soaking, miserable Hampter in Dr. Syg's palm."
            show hampter sad at appear(x_align = 0.5)
            plutoes "{i}scribbles on wall{/i} {cps=*0.75}{b}{color=#ff2d00} [player_name] is a hairy loser. {i}-signed [player_name] {/i}{/color}{/b}{/cps}"
            n "Plutoes leaves. You hope Dr. Syg will vouch for you when the janitors report vandalism."
            hide plutoes
            syg pensive "Too bad I couldn't take his tail to sample..."
            hide hampter
            hide syg
            n "You watch Dr. Syg walks away with a drained Hampter. You silently pray that Hampter's work at the Demonic department is easy and won't add to her exhaustion."
            $ update_character_points({"syg": 1})
            return

        label spare_pochi:
            n "You do not do anything. Hold on, Dr. Syg's level is technically above Plutoes'. Would this get you in trouble?"
            syg upset "I will have to report this as an incident if we don't recover Hampter."
            plutoes happy "{i}scribbles on his coat{/i} {cps=*0.75}{b}{color=#ff2d00} And I will give you a {i}clean {/i}haircut if you do grab Pochi.{/color}{/b}{/cps}"
            n "Okay, you are in trouble either way. It's so hard being an intern."
            n 'Just as you are about to drop to your knees and beg for forgiveness, Pochi teleports away with a loud "POP!". Perhaps he does have a tiny bit of sympathy in his non-existent heart.'
            syg "Hmph."
            hide syg
            n "Plutoes walks over to you and pats you on your shoulder in approval before leaving."
            hide plutoes
            n "You feel a small itch on your shoulder. A very colorful mushroom is planted. You better get it checked out and removed at the bio-hazard infirmary."
            $ update_character_points({"syg": -1})
            $ update_character_points({"plutoes": 1})
            return







