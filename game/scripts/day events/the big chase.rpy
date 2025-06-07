label day_event_the_big_chase:
    scene bg hallway
    with default_fade
    n "You're on your way back from the restroom when you hear a commotion from behind you. You turn around to see a blue hamster sprinting down the hallway towards you." 
    show hampter panic
    n "Behind Hampter, a dark sphere with four legs scrambles after her, his mouth open wide, threatening to suck her in."
    n "Following closely behind are two more figures you can't quite make out."
    # render in graphic of hampter(?) and pochi
    hampter "Help me!"
    hide hampter

    menu: 
        n "What should you do?"
        "Help Hampter by scooping her up.":
            jump help_hampter
        "Remind Hampter that she can teleport, but stay well out of the way. No point getting too involved.":
            jump hamp_tele
        "Do nothing. According to the foundation employee guidelines, level 5 clearance personnel should not involve themselves in anomaly incidents.":
            jump ignore_hampter

    label help_hampter:
        n "You pick up Hampter just as she reaches you."
        n "Pochi growls at you and starts biting at your ankles. It hurts. A lot."
        # un-render graphic, so just back to the hallway
        n "The two other figures finally catch up to you. You recognize them as Dr. Chan and Dr. Syg."
        show chan panic at appear(x_align = 0.33)
        show syg neutral at appear(x_align = 0.66)
        chan "Finally... caught... up..."
        chan "Can you please... hand him over...? Pochi, I mean." 
        player "Huh? Why?"
        chan pensive "He ate my hard drive."
        syg "I'd like him instead, if that's alright. Dr. Jessie has been refusing me for ages. Something about \"ethical procedures\" and \"anomaly rights.\" Nonsense, I'm sure."
        n "Better act fast. If you don't, Pochi's going to chew through your ankles."

        menu:
            n "Who do you give him to?"
            "Dr. Chan needs his hard drive back. Better help the poor guy.":
                jump chan_hard_drive
            "Dr. Syg needs it. For...\"science.\"":
                jump syg_experiment

        label chan_hard_drive:
            player "Here, Dr. Chan!"
            n "You swing your leg in Dr. Chan's direction, flinging Pochi from your ankle. He slams into the ceiling and falls, squeaking like a rubber duck."
            chan surprise "..."
            player "...Sorry! The last time I did sports was in high school."
            n "Just as Dr. Chan makes his way towards Pochi, you see a mushroom pop up around the corner."
            n "Pochi must have seen it too, because he sprints towards it."
            show plutoes happy at appear(x_align = 0.5)
            n "Plutoes picks up Pochi, flashes everyone an enigmatic smile and leaves."
            show plutoes at disappear
            chan upset "My hard drive..."
            syg neutral "..."
            chan neutral "Thank you, though. For your... attempt to help. I'll be going now."
            chan sad "{size=-10}(Ten months of incident reports... Gone...){/size}"
            show chan at disappear
            syg fury "Tch. Fine. I'll get him eventually."
            hide syg
            $ update_character_points({"chan": 1})
            $ update_character_points({"syg": -1})
            $ update_character_points({"plutoes": -1})
            jump help_hampter_con
        
        label syg_experiment:
            player "Okay, Dr. Syg."
            chan sad "..."
            show chan at disappear
            n "You decide to prove your worth by kicking Pochi off your leg towards Dr. Syg."
            hide chan
            show plutoes at appear(x_align = 0.5)
            n "Out of nowhere, Plutoes appears and catches Pochi as he's sailing through the air."
            n "He promptly leaves without saying a word."
            show plutoes at disappear
            syg "...I'll get him next time. Thanks for the help, anyway."
            n "Dr. Syg gives you a nod before turning to leave."
            show syg at disappear
            $ update_character_points({"syg": 1})
            $ update_character_points({"chan": -1})
            $ update_character_points({"plutoes": -1})
            jump help_hampter_con

        label help_hampter_con:
            hampter happy "Thank you for helping me!"
            n "Hampter nuzzles against your palm before teleporting away."
            hide hampter
            $ update_character_points({"hampter": 1})
            return

    label hamp_tele:
        player "...Can't you teleport, Hampter?"
        hampter surprise "!!!"
        n "You watch as Hampter disappears into thin air."
        n "Pochi skids to a stop in front of you. He doesn't have eyes, but you feel as if he's staring daggers into your soul."
        n "The sound of footsteps draws closer, and you can see who it is. It's Dr. Chan and Plutoes."
        n "Pochi growls and teleports away. Maybe to go after Hampter. Or escape from these two."
        show plutoes at appear(x_align = 0.33)
        show chan at appear(x_align = 0.66)
        n "Dr. Chan stops in front of you and looks around, bewildered."
        n "Out of the corner of your eye, you see Pochi reappear behind Plutoes, standing a few steps behind Dr. Chan."
        chan fury "Hey [player_name], did you see where Pochi went? That damn thing ate my hard drive."
        n "You see Plutoes take out a sign."
        plutoes talk "{b}{color=#ff2d00}dont tell him -signed plutoes{fast}{/color}{/b}"
        
        menu:
            n "Should you cover for Pochi?"
            "You're sure Pochi means no harm. Dr. Chan's overreacting.":
                jump chan_lie
            "No, this is a professional environment with no room for mischief. Expose the criminal!":
                jump expose_plutoes
            
        label chan_lie:
            show plutoes
            player "I'm not sure. I think he teleported away."
            show chan unique
            ethy "{sc}{size=+5}{b}AAAAAAA??????{/size} {w=0.7}{size=+3} A. {/size}{w=0.7} AA.{/b}{sc}"
            n "You hear confused screaming in your head. Dr. Chan must be hearing it too, because he stares at you suspiciously."
            player "Or maybe he wasn't going after Hampter?"
            show plutoes happy
            n "Plutoes nods at you, grinning."
            chan "Hm. It's alright, I've attached a tracker to the hard drive. I'll find him eventually."
            show plutoes happy at disappear
            n "You see Dr. Chan take out his device, then swiftly turn around. Only then do you both realize that Plutoes is no longer there."
            chan fury "Dammit, Plutoes!"
            show chan at disappear
            n "Well. That's that. Go get a coffee or something. You need it."
            $ update_character_points({"plutoes": 1})
            $ update_character_points({"chan": -1})
            $ update_character_points({"syg": -1})
            return

        label expose_plutoes:
            player "He's behind Plutoes!"
            show plutoes upset
            show haze green onlayer top:
                alpha 0.0
                linear 0.2 alpha 1.0
            show plutoes unique
            n "Suddenly, you and Dr. Chan are hit with a wave of noxious fumes."
            show plutoes unique at disappear
            show chan panic
            chan panic "{i}cough cough cough{/i}"
            show haze green onlayer top:
                linear 1.5 alpha 0.0
            chan "{i}cough- {/i}What was that?!"
            n "Unsurprisingly, Plutoes and Pochi are gone."
            chan fury "What the hell's happening?!"
            show chan unique
            ethy "{sc}{size=+3}{b}AAA.{/b}{/size}{sc}"
            show chan at disappear
            n "You watch as Dr. Chan trudges away. At this point, it might be easier for him to just rewrite whatever was in that hard drive."
            $ update_character_points({"chan": 1})
            $ update_character_points({"syg": -1})
            $ update_character_points({"plutoes": -1})
            hide chan
            hide plutoes
            hide haze green onlayer top
            return

    label ignore_hampter:
        n "You watch as Hampter gets sucked into a black hole."
        player "???"
        n "The beast burps, padding around in satisfaction. Did you just witness a murder?"
        n "The two figures get closer, and you recognize them as Dr. Syg and Plutoes. What an odd combination."
        n "Pochi ducks behind you like a kid that just broke an expensive vase."
        show plutoes happy at appear(x_align = 0.3)
        show syg neutral at appear(x_align = 0.6)
        syg "Please grab Pochi for me, [player_name]. I need to recover Hampter. She's supposed to oversee my department temporarily."
        n "Plutoes pulls out a sign from behind his back."
        plutoes talk "{b}{color=#ff2d00}hey bud gimme my dog back i was just tryna save the hairball from the demonis demon department -signed plutoes{fast}{/color}{/b}"

        menu:
            n "No time for questions. Who should you listen to?"
            "Grab Pochi. Right your previous wrong of not helping poor Hampter.":
                jump grab_pochi
            "Spare Pochi. This cross-department conflict is above your pay grade.":
                jump spare_pochi
            
        label grab_pochi:
            n "You grab Pochi, who immediately begins to struggle. He tries to hit you with his tail, but you avoid his attempts and manage to hand him over to Dr. Syg."
            show plutoes upset
            n "Pochi teleports away as soon as Dr. Syg tries to grab him, leaving behind a soaking, miserable Hampter in his palm."
            show hampter sad at appear(x_align = 0.5)
            n "Plutoes smiles menacingly at you, then leaves. You feel an itch near your ear and scratch it."
            show plutoes upset at disappear
            syg pensive "One day..."
            n "Your own voice rings in your ear, spewing slurs."
            n "{sc}{color=#009900}%%&*(@#&$%%!@#(*&(@%%%%*&!@$!*&*#*$!&%%!*&$$*!@&{/color}{/sc}"
            syg '...'
            syg "You should get that checked out. I think Plutoes planted something in your ear."
            n "{sc=1.5}{i}{color=#009900}\"Babe, i just\ni jus dont think its working out\nEngine 3 failure abort ship abort ship\nI just dont think we r meant for each other\nBeep BEEP BEEP\nOverheat OVERHEAT\"{/color}{/i}{sc}"
            show hampter at disappear
            show syg pensive at disappear
            n "You watch Dr. Syg walk away with a drained Hampter. You contemplate whether removing your ear or going deaf would get you more company compensation claims."
            $ update_character_points({"syg": 1})
            $ update_character_points({"plutoes": -1})
            $ update_character_points({"chan": -1})
            $ update_character_points({"hamp": -1})
            hide hampter
            hide syg
            hide plutoes
            return

        label spare_pochi:
            n "You don't do anything."
            n "Hold on, Dr. Syg's clearance level is technically above Plutoes'. Wouldn't this get you in trouble?"
            syg upset "I'll have to report this as an incident if we don't recover Hampter."
            n "Plutoes sneezes before skateboarding away. Pochi is nowhere to be found."
            n "...Was that was your imagination? Either way, you feel an itch in your ear."
            player "What the-"
            syg neutral "What happened, [player_name]?"
            show haze green onlayer top:
                alpha 0.0
                linear 0.2 alpha 1.0
            player "{sc}{color=#009900}F!&*@%%#! YOU $%%&*!%%@&*#%%@%%#${/color}{/sc}"
            n "You feel the spontaneous urge to skateboard away."
            n "But before you get the chance..."
            hide haze green onlayer top
            show black_screen zorder 50
            with hpunch
            n "...Dr. Syg sucker-punches you in the face."
            $ update_character_points({"syg": -1})
            $ update_character_points({"plutoes": 1})
            $ update_character_points({"chan": -1})
            $ update_character_points({"hamp": -1})
            return